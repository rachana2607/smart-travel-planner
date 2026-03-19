from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    temperature=0.7,
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_itinerary(city, weather, places, hotels, days):

    places_list = ", ".join(places)
    hotels_list = ", ".join(hotels)

    prompt = PromptTemplate(
        input_variables=["city", "weather", "places", "hotels", "days"],
        template="""
You are a smart travel assistant.

Create a {days}-day travel itinerary for a trip to {city}.

Weather: {weather}

Places to visit: {places}

Hotels available: {hotels}

Distribute the places across {days} days.

Format example:

Day 1:
- Visit place
- Visit place

Day 2:
- Visit place
- Visit place

Continue until Day {days}.
"""
    )

    final_prompt = prompt.format(
        city=city,
        weather=weather,
        places=places_list,
        hotels=hotels_list,
        days=days
    )

    response = llm.invoke(final_prompt)

    return response.content