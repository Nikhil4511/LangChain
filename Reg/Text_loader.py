from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt",'utf-8')

docs = loader.load()
print(docs)
