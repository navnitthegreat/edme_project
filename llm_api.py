import os
from dotenv import load_dotenv
from concept_keywords import keyword_dict

load_dotenv()
# Assume Anthropic API code could go here

def get_concepts(question: str):
    # Simple rule-based fallback
    question_lower = question.lower()
    matched = [v for k, v in keyword_dict.items() if k in question_lower]
    if matched:
        return list(set(matched))

    # Optionally, call LLM here
    prompt = f'Given the question: "{question}", identify the historical concept(s) this question is based on.'
    # result = call_llm_api(prompt)  # <- your Anthropic call goes here
    # return parse_result(result)

    return ["General Knowledge"]  # fallback


def build_prompt(question: str) -> str:
    return f"""Given the question: "{question}", identify the historical concept(s) this question is based on.

Return a comma-separated list of concepts relevant to the question."""
