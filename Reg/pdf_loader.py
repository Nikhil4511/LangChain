from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r"C:\Users\npal1\Desktop\Nikhil\coding\Gen-AI-langChain\Reg\Nikhil_DataAnalyst_Resume_.pdf","utf-8")

docs = loader.load()

print(docs)