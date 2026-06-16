from pypdf import PdfReader
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def load_syllabus_json():

    with open(
        "data/syllabus.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def extract_pdf_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def generate_syllabus_json(text):

    prompt = f"""
Extract the syllabus into valid JSON.

Format:

{{
  "subjects": [
    {{
      "name": "Subject Name",
      "topics": [
        "Topic 1",
        "Topic 2"
      ]
    }}
  ]
}}

Only return JSON.
No explanation.

Syllabus:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    text = extract_pdf_text(
        "data/syllabus.pdf"
    )

    json_output = generate_syllabus_json(
        text[:12000]
    )

    json_output = json_output.replace(
        "```json",
        ""
    )

    json_output = json_output.replace(
        "```",
        ""
    ).strip()

    with open(
        "data/syllabus.json",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(json_output)

    print(
        "Saved to data/syllabus.json"
    )