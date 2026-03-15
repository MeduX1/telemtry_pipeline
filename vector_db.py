import chromadb
from chromadb.utils import embedding_functions

vector_db= chromadb.PersistentClient(path = './chroma_db')

sentence_transformers = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = vector_db.get_or_create_collection(
    name = 'medicalnotes',
    embedding_function = sentence_transformers
)

documents = [
    "Patient presents with sharp, stabbing chest pain radiating to the left arm, exacerbated by deep breathing.",
    "Patient complains of a mild headache and runny nose for the past 3 days. No fever.",
    "Severe abdominal pain in the lower right quadrant, accompanied by nausea and vomiting.",
    "Routine checkup. Patient reports feeling fine. Vitals are normal."
]

metadatas = [{"patient_id": "PT-001"}, {"patient_id": "PT-002"}, {"patient_id": "PT-003"}, {"patient_id": "PT-004"}]
ids = ["note_1", "note_2", "note_3", "note_4"]

print("🧠 Embedding and saving documents to ChromaDB... (This may take a few seconds the first time to download the model)")

collection.upsert(
    documents = documents ,
    metadatas =metadatas ,
    ids = ids
)

print("✅ Documents saved into the Vector Vault!")

query_text = "Possible mild headache"
print(f"\n🔍 Searching for cases matching: '{query_text}'")

result = collection.query(
    query_texts = [query_text],
    n_results = 1
)

print(f"Top match found {result['documents'][0][0]}")
print(f"👤 Belongs to: {result['metadatas'][0][0]['patient_id']}")
print(f"📏 Mathematical Distance: {result['distances'][0][0]} (Lower is better)")









