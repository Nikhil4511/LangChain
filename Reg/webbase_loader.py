from langchain_community.document_loaders import WebBaseLoader

url = "https://www.cricbuzz.com/live-cricket-scores/151532/wi-vs-ind-1st-odi-west-indies-tour-of-india-2026"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)