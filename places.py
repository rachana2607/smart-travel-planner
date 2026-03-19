from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    temperature=0.7,
    model="llama-3.3-70b-versatile",   # Updated model
    api_key=os.getenv("GROQ_API_KEY")
)

def get_places(city):

    prompt = f"""
List 5 famous tourist places in {city}.
Return only the place names in separate lines.
"""

    try:
        response = llm.invoke(prompt)

        places = response.content.split("\n")

        cleaned_places = []

        for p in places:
            p = p.replace("-", "").strip()
            if p != "":
                cleaned_places.append(p)

        return cleaned_places[:5]

    except:
        return []