#use llama index to load in PDF documents and embed them

#Creating the vectors
from sentence_transformers import SentenceTransformer
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

load_dotenv()

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(EMBED_MODEL)
EMBED_DIM = 3072

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)          #look for the pdf and load it
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

def embed_texts(texts: list[str]) -> list[list[float]]:
    embeddings = model.encode(texts)
    return embeddings.tolist()