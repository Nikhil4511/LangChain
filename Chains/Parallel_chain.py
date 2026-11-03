from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI(model='gpt-4o-mini')
model2 = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

prompt1 = PromptTemplate(
    template='Generate short and notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answer from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and into a single document \n --> {notes} and {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain =  RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model2 | parser

})

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain

text = """
As India prepared for their title defence ahead of the 2015 World Cup Down Under, with the catch phrase 'Won't give it back' doing the rounds, Virat Kohli was touted to be a key performer for India. The Indians had a terrible run in Australia, having failed to win a single match in the Test series as well as the succeeding ODI tri-series. Kohli started off in signature fashion, with a typically stroke-filled hundred against Pakistan as India maintained their unbeaten run against their arch-rivals in ICC events. As India stormed into the semi-finals unbeaten, Kohli's form continued to take an uncharacteristic dip, culminating in a painstaking 1 in the semi-final loss against the co-hosts and eventual champions, Australia.

Kohli, the then full-time Test captain, toured Sri Lanka with a young side without the services of Mahendra Singh Dhoni, wary of the Sri Lankan spinners' fabled 4th innings con-job. After losing the first Test, Kohli's India recorded a dramatic come-from-behind win in the series, going on to win 2-1. Kohli continued to build on his auspicious start to Test captaincy as he led them to a rout of the South Africans on a series of rank-turners all around India. He had a quiet series with the bat, as the more stoic batsmen of his team took over. Nonetheless, the triumph took India to the No. 1 spot in the ICC Test rankings for the first time since they forfeited it to England after the forgettable white-wash in 2011.
"""
result = chain.invoke({'text':text})

print(result)