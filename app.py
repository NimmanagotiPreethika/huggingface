import streamlit as st
import requests

# Function to fetch a random joke from the JokeAPI
def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    joke_data = response.json()
    if joke_data["type"] == "single":
        return joke_data["joke"]
    elif joke_data["type"] == "twopart":
        return f"{joke_data['setup']} \n{joke_data['delivery']}"
    else:
        return "No joke today! Please try again later."

# Streamlit app
def main():
    st.title("Joke Generator")
    st.subheader("Generate Random Jokes")
    
    # Button to fetch a new joke
    if st.button("Tell me a joke!"):
        joke = fetch_joke()
        st.write(joke)

if __name__ == "__main__":
    main()
