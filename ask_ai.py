import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "sk-...":
    raise ValueError("Укажи реальный OPENAI_API_KEY в файле .env")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": (
                "Придумай 3 креативных названия для моего проекта: "
                "лендинг-страница для HR-сервиса по управлению переводами сотрудников."
            ),
        }
    ],
)

print(response.choices[0].message.content)
