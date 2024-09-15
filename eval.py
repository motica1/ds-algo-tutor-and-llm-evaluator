import openai
from langsmith.wrappers import wrap_openai

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# # Load environment variables
load_dotenv()

url = "https://zerotomastery.io/cheatsheets/data-structures-and-algorithms-cheat-sheet/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text = [p.text for p in soup.find_all("p")]
full_text = "\n".join(text)

openai_client = wrap_openai(openai.Client())

def answer_ds_algo_question_oai(inputs: dict) -> dict:
    """
    Generates answers to user questions based on a provided website text using OpenAI API.

    Parameters:
    inputs (dict): A dictionary with a single key 'question', representing the user's question as a string.

    Returns:
    dict: A dictionary with a single key 'output', containing the generated answer as a string.
    """

    # System prompt
    system_msg = (
        f"Answer user questions in 2-3 sentences about this context: \n\n\n {full_text}"
    )

    # Pass in website text
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": inputs["question"]},
    ]

    # Call OpenAI
    response = openai_client.chat.completions.create(
        messages=messages, model="gpt-4o-mini"
    )

    # Response in output dict
    return {"answer": response.dict()["choices"][0]["message"]["content"]}
  
  
from langsmith.evaluation import evaluate, LangChainStringEvaluator

# Evaluators
qa_evalulator = [LangChainStringEvaluator("cot_qa")]
dataset_name = "week1_prj_evaluation_data_structure_algo_tutor"

experiment_results = evaluate(
    answer_ds_algo_question_oai,
    data=dataset_name,
    evaluators=qa_evalulator,
    experiment_prefix="week1_prj_evaluation_data_structure_algo_tutor_exp1"
    )