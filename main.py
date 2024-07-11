from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

from qdrant_client import models
from qdrant_client.http.models import VectorParams, Distance

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from openai import OpenAI

openai_client = OpenAI()

def small_embedding(text,model="text-embedding-3-small"):
  text = text.replace("\n", " ")
  return openai_client.embeddings.create(input = [text], model=model,dimensions=128).data[0].embedding

def large_embedding(text, model="text-embedding-3-large"):
  text = text.replace("\n", " ")
  return openai_client.embeddings.create(input = [text], model=model,dimensions=1024).data[0].embedding

loaders = [
    PyPDFLoader("/content/TEGI0570.pdf"),
]

docs = []
chunk_size=1050
chunk_overlap = 50

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
    )

for loader in loaders:
    docs.extend(loader.load())

splits = r_splitter.split_documents(docs)

len(splits)

client = QdrantClient(":memory:")
COLLECTION_NAME = "multi_stage_db"

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={
        "small-embedding": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            datatype=models.Datatype.FLOAT16
        ),

        "large-embedding": models.VectorParams(
            size=1024,
            distance=models.Distance.COSINE,
            datatype=models.Datatype.FLOAT16
        ),

    },

)

for i in range(0,len(splits)):
  client.upsert(
      collection_name=COLLECTION_NAME,
      points=[
          models.PointStruct(
              id=i,
              vector={
                  "small-embedding":small_embedding(splits[i].page_content),
                  "large-embedding":large_embedding(splits[i].page_content),

              },


          )
      ],
  )

query_text = "what are  measurement and Mismeasurement of Risk "

small_vector = small_embedding(query_text)
large_vector = large_embedding(query_text)

result = client.query_points(
    collection_name= COLLECTION_NAME,
    prefetch=models.Prefetch(
        query=small_vector,
        using="small-embedding",
        limit=50,
    ),
    query=large_vector,
    using="large-embedding",
    limit=5,
)

result

ids = [item.id for item in result.points]

for i in ids:
  print(splits[i].page_content)
  print('\n')
  print('-'*75)

