from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4o-mini')

result = llm.invoke("Write fifty words on india")

print(result)




# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

# response = llm.invoke("Explain LangChain in simple words.")

# print(response.content)