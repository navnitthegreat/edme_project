import argparse
from csv_reader import read_csv
from llm_api import get_concepts
import csv
import os

def process_questions(subject):
    input_path = os.path.join("resources", f"{subject}_questions.csv")
    output_path = f"output_concepts.csv"

    questions = read_csv(input_path)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Question Number", "Question", "Concepts"])

        for q in questions:
            qnum, qtext = q["Question Number"], q["Question"]
            concepts = get_concepts(qtext)
            print(f"Question {qnum}: {concepts}")
            writer.writerow([qnum, qtext, "; ".join(concepts)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", required=True)
    args = parser.parse_args()
    process_questions(args.subject)
