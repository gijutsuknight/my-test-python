print("Start")
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load document
loader = TextLoader("example.txt", encoding="utf-8")
documents = loader.load()   # List[Document]

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_documents(documents)

print(f"Loaded docs: {len(documents)}")
print(f"Chunks created: {len(chunks)}")
print(chunks[0].page_content[:200])
print(chunks[0].metadata)


print("End")