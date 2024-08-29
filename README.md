# Rasa-Based Travel Chatbot
## Overview
This Rasa-based Travel Chatbot is designed to assist users in planning their trips efficiently and conveniently. The chatbot provides personalized travel recommendations, including flight and bus suggestions, and offers real-time flight tracking to keep users informed about their journeys. The goal of this project is to deliver a seamless and user-friendly experience by leveraging modern AI technologies and APIs.

## Features
### 1.  Personalized Flight and Bus Suggestions
#### What It Does: The chatbot recommends flight and bus options based on the user's preferences, such as destination, departure time, and budget. It provides direct links to airlines or bus companies, making it easy for users to book their travel.
#### Why It’s Used: Personalized recommendations enhance user experience by tailoring options to individual needs, saving time and effort in travel planning. Rasa's powerful NLP capabilities enable the chatbot to understand user inputs and provide relevant suggestions.
### 2. Real-Time Flight Tracking
#### What It Does: The chatbot fetches live flight data or specific flight details using APIs, allowing users to track their flights in real-time. This feature ensures that users stay informed about their flight status, including delays, cancellations, or gate changes.
#### Why It’s Used: Real-time information is crucial for travelers to make informed decisions and avoid inconveniences. The integration of flight tracking APIs allows the chatbot to provide accurate and up-to-date information directly within the chat interface.
## Technology Stack
### 1. Rasa
#### Reason for Use: Rasa is an open-source machine learning framework for building AI chatbots that can handle complex conversations. It’s chosen for its flexibility, extensive support for custom actions, and ability to handle contextual conversations, making it ideal for a travel assistant that needs to understand and respond to a wide range of user queries.
#### How It Works: Rasa uses Natural Language Understanding (NLU) to interpret user inputs and Natural Language Generation (NLG) to generate responses. The framework allows for training custom models to improve the chatbot's accuracy in recognizing user intents and entities.
### 2. APIs for Flight Tracking
#### Reason for Use: APIs provide access to live flight data, which is essential for the real-time tracking feature. They are used to query flight information based on user inputs, such as flight numbers or destinations.
#### How It Works: The chatbot sends requests to flight tracking APIs, retrieves the data, and presents it to the user in an easily understandable format. This integration ensures that users receive the most accurate and timely information about their flights.
### 3. Custom Actions in Rasa
#### Reason for Use: Custom actions are used to handle specific tasks that go beyond standard conversation flows, such as fetching flight details or generating personalized travel recommendations.
#### How It Works: When a user request requires information retrieval or processing (e.g., checking flight status), the chatbot triggers a custom action. This action performs the necessary operations, such as calling an API or processing user input, and then returns the result to the user.
### 4. Frontend Interface
#### Reason for Use: While the core of the chatbot is managed by Rasa, the frontend interface could be built using frameworks like React or integrated into existing platforms to provide a user-friendly way for users to interact with the chatbot.
#### How It Works: The frontend sends user messages to the Rasa server, which processes the input and sends back the appropriate response. The frontend displays this response to the user, maintaining a seamless conversation flow.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AsawirShafiq/Travel-Chatbot-RASA.git
cd Travel-Chatbot-RASA
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Set up API Keys
You can obtain various free API keys on a simple google search.

### 4. Train the RASA Model
```bash
rasa train
```

### 5. Run the custom actions in a separate terminal.
```bash
rasa run actions
```

### 6. Run the chatbot on the shell
```bash
rasa shell
```
