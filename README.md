# 🦜🔗 Gen-AI-LangChain

A hands-on collection of small, focused LangChain examples covering the core building blocks of Generative AI applications: LLMs and chat models, prompts, output parsers, chains, runnables, embeddings, document loaders and text splitters.

Each folder is one topic, and each script is a short, runnable demo.

## 📁 Project Structure

```
Gen-AI-langChain/
├── LLMs/                  # Plain LLM calls (OpenAI, Gemini)
├── ChatModels/            # Chat models: OpenAI, Gemini, Anthropic, Hugging Face (API + local)
├── Prompt/                # PromptTemplate, ChatPromptTemplate, message types, chatbot, Streamlit UI
├── Structured_Output/     # TypedDict and with_structured_output
├── Chains/                # Simple, sequential, parallel and conditional chains
├── Runnable/              # RunnableSequence, RunnableParallel, RunnableBranch
├── EmbeddingModel/        # OpenAI embeddings
├── Reg/                   # Document loaders: Text, PDF, CSV, directory, web
├── Text-Spliter/          # Length-based and semantic text splitting
├── stroutputparser.py     # StrOutputParser example
├── stringoutputparaser.py # Same task without a parser (manual chaining)
├── Jsonoutputparser.py    # JsonOutputParser example
├── structureoutputparser.py # StructuredOutputParser + ResponseSchema
├── requirements.txt
└── .env                   # API keys (never commit this)
```

## 🧠 Topics Covered

| Topic | What it shows | Files |
|---|---|---|
| **LLMs** | Calling a text-completion LLM | `LLMs/` |
| **Chat Models** | Same question across providers (OpenAI, Gemini, Claude, Hugging Face) | `ChatModels/` |
| **Prompts** | `PromptTemplate`, `ChatPromptTemplate`, System/Human/AI messages, chat history, Streamlit front end | `Prompt/` |
| **Output Parsers** | `StrOutputParser`, `JsonOutputParser`, `StructuredOutputParser`, `PydanticOutputParser` | root `.py` files |
| **Structured Output** | `TypedDict` schemas | `Structured_Output/` |
| **Chains** | Simple, sequential, parallel (notes + quiz) and conditional (sentiment-based reply) chains | `Chains/` |
| **Runnables** | `RunnableSequence`, `RunnableParallel`, `RunnableBranch`, `RunnablePassthrough` | `Runnable/` |
| **Embeddings** | `text-embedding-3-large` document embeddings | `EmbeddingModel/` |
| **Document Loaders** | `TextLoader`, `PyPDFLoader`, `CSVLoader`, `DirectoryLoader`, `WebBaseLoader` | `Reg/` |
| **Text Splitters** | `CharacterTextSplitter`, semantic chunking | `Text-Spliter/` |

## ⚙️ Setup

**Prerequisites:** Python 3.10+ and API keys for the providers you want to try.

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/Gen-AI-langChain.git
cd Gen-AI-langChain

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
pip install langchain-community langchain-text-splitters pypdf streamlit   # used by loaders, splitters and UI demos
```

### 🔑 Environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_gemini_key
ANTHROPIC_API_KEY=your_anthropic_key
HUGGINGFACEHUB_ACCESS_TOKEN=your_hf_token
```

You only need the keys for the providers used by the scripts you run.

## ▶️ Running the Examples

Run scripts from their own folder, since some use relative file paths:

```bash
python Chains/simpleChain.py
python Chains/Parallel_chain.py
python Runnable/runnable_branch.py
python EmbeddingModel/embedding_open_ai.py

# Streamlit UI
streamlit run Prompt/prompt_UI.py

# Interactive chatbot (type "exit" to quit)
python Prompt/Chatbot.py

# Document loaders
cd Reg && python Text_loader.py
```

## 🧩 Example: a simple chain

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"],
)

chain = prompt | ChatOpenAI() | StrOutputParser()
print(chain.invoke({"topic": "cricket"}))
```

## 🛠️ Tech Stack

- [LangChain](https://python.langchain.com/) (`langchain`, `langchain-core`, `langchain-community`)
- OpenAI, Google Gemini, Anthropic Claude and Hugging Face integrations
- `python-dotenv` for configuration
- Streamlit for the demo UI
- `numpy`, `scikit-learn` for ML utilities

## 📝 Notes

- Some files are work-in-progress learning scripts (e.g. empty placeholders or paths to fill in). Update file paths and model names to ones available to you.
- Model names change often; check each provider's docs for current ones.

## 🔒 Security

Never commit `.env` or hard-coded API keys. Add this to `.gitignore`:

```
.env
.venv/
__pycache__/
```

## 🤝 Contributing

Suggestions and improvements are welcome. Open an issue or submit a pull request.
