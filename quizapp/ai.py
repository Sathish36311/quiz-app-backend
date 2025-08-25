import re
import google.generativeai as genai
import ast
from django.conf import settings


def generate_mcq(topic, number_of_questions, difficulty):
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')

    prompt = (
        f"Generate {number_of_questions} multiple choice questions with 4 options each "
        f"on the topic '{topic}' with {difficulty} difficulty. "
        "Format output as JSON array: "
        "[{'question': '', 'options': ['a':'', 'b':'', 'c':'', 'd':''], 'answer': 'a'}]"
    )

    response = model.generate_content(prompt)
    try:
        # parse the response
        content = response.candidates[0].content.parts[0].text

        if content.startswith("```json") or content.startswith("```"):
            content = content.strip("```json").strip("```").strip()

        content = re.sub(r'`+', '', content)

        return ast.literal_eval(content)
    except (ValueError, SyntaxError, IndexError) as e:
        print("Error While generating questions:", e)
        return []
