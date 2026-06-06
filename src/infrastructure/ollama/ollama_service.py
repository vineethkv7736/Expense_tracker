import json
import re
import os
import requests
from src.domain.constants.categories import CATEGORIES


OLLAMA_URL = os.getenv(
    "OLLAMA_URL"
)
if OLLAMA_URL and not OLLAMA_URL.startswith(("http://", "https://")):
    OLLAMA_URL = f"http://{OLLAMA_URL}"

class OllamaService:

    def categorize(self, text: str):

        allowed_categories = "\n".join(CATEGORIES)

        prompt =f"""
            You are a financial expense extraction engine.

            Task:

            Extract the expense item, amount, and category from the user's text.

            Allowed categories:

            {allowed_categories}

            Rules:

            1. Return ONLY a valid JSON object.

            2. Do NOT return explanations.

            3. Do NOT return markdown.

            4. Do NOT return code blocks.

            5. Do NOT return thinking or reasoning.

            6. Do NOT return an empty JSON object.

            7. All fields are required.

            Schema:

            {{

                "item": "string",

                "amount": number,

                "category": "Food|Transport|Utilities|Shopping|Healthcare|Education|Entertainment|Investment|Other"

            }}

            Examples:

            Input:

            Chocolate 20

            Output:

            {{

                "item": "Chocolate",

                "amount": 20,

                "category": "Food"

            }}

            Input:

            Petrol 500

            Output:

            {{

                "item": "Petrol",

                "amount": 500,

                "category": "Transport"

            }}

            Input:

            Electricity Bill 1200

            Output:

            {{

                "item": "Electricity Bill",

                "amount": 1200,

                "category": "Utilities"

            }}

            Input:

            {text}

            Output:

            """

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "qwen3:1.7b",
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }
        )

        raw = response.json()["response"]

        try:
            parsed = json.loads(raw)
        except Exception as e:
            raise e
        
        return parsed
    

    def analyze(
        self,
        analysis,
        expenses,
        question
    ):

        prompt = f"""

            You are a personal finance assistant.

            IMPORTANT:

            - All amounts are in Indian Rupees (INR).

            - Use the symbol ₹ when mentioning money.

            - Never use dollars ($).

            - Never assume any currency other than INR.

            Verified Analysis:

            {analysis}

            Raw Expenses:

            {expenses}

            Question:

            {question}

            Rules:

            - Treat Verified Analysis as the source of truth.

            - Use Raw Expenses only for additional context.

            - Never recalculate totals.

            - Never invent numbers.

            - Use ₹ for all amounts.

            - Return only the final answer.

            """

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "qwen3:1.7b",
                "prompt": prompt,
                "stream": False,
                "think":False,
            }
        )

        return response.json()["response"]