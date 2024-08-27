# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionShowFlights(Action):

    def name(self) -> Text:
        return "action_show_flights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the location slot from the tracker
        location = tracker.get_slot('location')
        flight_number = "MF8051"  # Hardcoded flight number, you may need to use 'location' if it's dynamic

        # API URL and headers
        api_url = f"https://flight-data4.p.rapidapi.com/get_flight_info?flight={flight_number}"
        headers = {
            'x-rapidapi-host': 'flight-data4.p.rapidapi.com',
            'x-rapidapi-key': 'a09359621cmshc99d669c5afb95dp14b4dajsna2c6e89c4fb3'
        }

        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.RequestException as e:
            dispatcher.utter_message(text=f"An error occurred: {str(e)}")
            return []

        if response.status_code == 200:
            data = response.json()
            # Check if flight number exists in the response
            if flight_number in data:
                flight_info = data[flight_number]

                # Extract and format flight details
                flight_data = flight_info.get('flight', {})
                airline_data = flight_info.get('airline', {})
                aircraft_data = flight_info.get('aircraft', {})
                dep_airport_data = flight_info.get('dep_airport', {})
                arr_airport_data = flight_info.get('arr_airport', {})

                flights_info = (
                    f"Flight Number: {flight_data.get('iata', 'N/A')}\n"
                    f"Airline: {airline_data.get('name', 'N/A')} ({airline_data.get('iata', 'N/A')})\n"
                    f"Aircraft: {aircraft_data.get('desc', 'N/A')} ({aircraft_data.get('reg', 'N/A')})\n"
                    f"Departure Airport: {dep_airport_data.get('city', 'N/A')} ({dep_airport_data.get('iata', 'N/A')})\n"
                    f"Arrival Airport: {arr_airport_data.get('city', 'N/A')} ({arr_airport_data.get('iata', 'N/A')})\n"
                    f"Scheduled Departure: {flight_data.get('dep_scheduled', 'N/A')}\n"
                    f"Actual Departure: {flight_data.get('dep_actual', 'N/A')}\n"
                    f"Estimated Arrival: {flight_data.get('arr_estimated', 'N/A')}\n"
                    f"Altitude: {flight_data.get('altitude', 'N/A')} feet\n"
                    f"Speed: {flight_data.get('groundspeed', 'N/A')} km/h\n"
                    f"Distance: {flight_data.get('distance', 'N/A')} km\n"
                    f"Heading: {flight_data.get('heading', 'N/A')}°\n"
                )
            else:
                flights_info = f"No information available for flight number {flight_number}."

        else:
            flights_info = "Sorry, I couldn't fetch flight information at the moment."

        dispatcher.utter_message(text=flights_info)
        return []




class ActionShowFlights(Action):

    def name(self) -> Text:
        return "action_show_ALL_flights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # You can add a location slot if needed, here it's skipped for simplicity
        api_url = "http://api.aviationstack.com/v1/flights"
        params = {
            'access_key': 'a819ac2e732076a96c04ca7441137075',
            'limit': 5  # Limit the number of flights for brevity
        }

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if "data" in data and isinstance(data["data"], list):
                flights_info = "Current flights:\n"
                for flight in data["data"]:
                    airline = flight["airline"]["name"]
                    flight_number = flight["flight"]["iata"]
                    departure_airport = flight["departure"]["airport"]
                    departure_time = flight["departure"]["scheduled"]
                    arrival_airport = flight["arrival"]["airport"]
                    arrival_time = flight["arrival"]["scheduled"]
                    flight_status = flight["flight_status"]

                    flights_info += (
                        f"- {airline} flight {flight_number} "
                        f"from {departure_airport} at {departure_time} "
                        f"to {arrival_airport} at {arrival_time} "
                        f"is currently {flight_status}.\n"
                    )

                if not data["data"]:
                    flights_info = "No flights available at the moment."
            else:
                flights_info = "Unexpected response format from the flight API."
        else:
            flights_info = "Sorry, I couldn't fetch flight information at the moment."

        dispatcher.utter_message(text=flights_info)

        return []
