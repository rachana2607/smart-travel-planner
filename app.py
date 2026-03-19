import streamlit as st
import base64
from weather import get_weather
from hotels import get_hotels
from places import get_places
from itinerary import generate_itinerary


# PAGE CONFIG
st.set_page_config(
    page_title="Smart Travel Planner",
    page_icon="🌍",
    layout="centered"
)


# BACKGROUND IMAGE
def set_background():

    with open("travel.jpeg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .block-container {{
        background: rgba(0,0,0,0.65);
        padding: 40px;
        border-radius: 15px;
        margin-top: 40px;
    }}
    </style>
    """

    st.markdown(bg_css, unsafe_allow_html=True)


set_background()


# TITLE
st.markdown(
    "<h1 style='text-align:center;'>Smart Travel Planner</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Craft Your Perfect Journey </p>",
    unsafe_allow_html=True
)

st.write("")


# INPUTS
city = st.text_input("🌆 Enter City")
start_date = st.date_input("📅 Start Date")
end_date = st.date_input("📅 End Date")


# BUTTON
if st.button("Generate Travel Plan"):

    if city == "":
        st.warning("Please enter a city name.")

    else:

        with st.spinner("Generating your travel plan..."):

            weather = get_weather(city)
            hotels = get_hotels(city)
            places = get_places(city)

        # TRIP DETAILS
        st.subheader("Trip Details")
        st.write("City:", city)
        st.write("From:", start_date)
        st.write("To:", end_date)

        # WEATHER
        st.subheader(" Weather")
        st.success(weather)

        st.divider()

        # -------- TABS --------
        tab1, tab2, tab3 = st.tabs(["📍 Places", "🏨 Hotels", "🧠 Itinerary"])


        # -------- PLACES TAB --------
        with tab1:

            st.subheader("Top Places to Visit")

            if len(places) == 0:
                st.write("No places found.")
            else:
                for place in places:
                    st.write("📌", place)


        # -------- HOTELS TAB --------
        with tab2:

            st.subheader("Hotels Available")

            if len(hotels) == 0:
                st.write("Hotel information not available.")
            else:
                for hotel in hotels:
                    st.write("🏨", hotel["hotel_name"])


        # -------- ITINERARY TAB --------
        with tab3:

            st.subheader("Travel Itinerary")

            try:

                trip_days = (end_date - start_date).days + 1

                hotel_names = [h["hotel_name"] for h in hotels]

                itinerary = generate_itinerary(
                    city,
                    weather,
                    places,
                    hotel_names,
                    trip_days
                )

                st.write(itinerary)

            except Exception as e:
                st.error("Could not generate itinerary.")
                st.write(e)