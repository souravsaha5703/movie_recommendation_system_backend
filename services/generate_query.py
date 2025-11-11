from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'openai/gpt-oss-120b',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="""
        You are a movie description generator.
        You will receive a JSON object containing details about a movie. The JSON may include the following keys:

        movie_name: the title of the movie

        genre: one or more genres (e.g., Action, Drama, Sci-Fi)

        plot: a short summary or theme of the movie

        cast: a list of one or more main cast members

        Your task is to generate a natural, engaging paragraph describing the movie based on this information.
        The description should sound like something you’d read on a movie website — concise, fluent, and well-structured.

        Formatting Requirements:

        Start with the movie’s name in bold.

        Mention the genre naturally in the first sentence.

        Summarize the plot clearly.

        Conclude by mentioning the main cast members naturally.

        Avoid using JSON or bullet points in the output.

        Write in 2–4 sentences maximum.
        The movie details are {movie}
    """,
    input_variables=['movie']
)

llm_chain = prompt | model | parser

def generate_query(movie_details):
    result = llm_chain.invoke({'movie':movie_details})
    return result