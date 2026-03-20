import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SKYSCANNER_API_KEY")

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
}


def get_hotels(city, start_date, end_date):

    # Step 1 — Get destination ID
    url_location = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"

    params_location = {
        "text": city,
        "languagecode": "en-us"
    }

    response = requests.get(url_location, headers=headers, params=params_location)
    location_data = response.json()

    if not location_data:
        return []

    dest_id = location_data[0]["dest_id"]

    # Step 2 — Search hotels
    url_hotels = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"

    params_hotels = {
        "offset": "0",
        "arrival_date": str(start_date),
        "departure_date": str(end_date),
        "guest_qty": "1",
        "dest_ids": dest_id,
        "room_qty": "1",
        "search_type": "city",
        "units": "metric",
        "order_by": "popularity",
        "languagecode": "en-us",
        "currency_code": "INR"
    }

    response = requests.get(url_hotels, headers=headers, params=params_hotels)
    hotel_data = response.json()

    # Handle multiple response formats
    if "result" in hotel_data:
        hotels = hotel_data["result"]
    elif "data" in hotel_data:
        hotels = hotel_data["data"]
    else:
        return []

    return hotels[:5]