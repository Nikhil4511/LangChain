#sk-ant-api03-Fg7fZK3Ql8Lys_qj6UVnr0BXAXVqHxLhLe0D5kSYuI7oEao5tVoME1AhwHOXRzrGbjI1-XBLifwQlfEtnhNHg-yTQFvQAA

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')
result = model.invoke("what is the capital of india")
print(result.content)