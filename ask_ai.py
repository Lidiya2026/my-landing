import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "sk-your-api-key-here":
    print("❌ Ошибка: вставьте реальный API-ключ в файл .env")
    exit(1)

client = OpenAI(api_key=api_key)

project_description = (
    "веб-приложение для HR-аналитики, которое загружает два Excel-файла "
    "(справочник сотрудников и история кадровых изменений), "
    "автоматически сопоставляет данные и строит таблицу перемещений сотрудников "
    "между отделами с визуализацией изменений и выявлением аномалий"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": f"Придумай 3 креативных названия для моего проекта: {project_description}"
        }
    ]
)

print("✅ Ответ от OpenAI:")
print(response.choices[0].message.content)
