import streamlit as st 
import google.generativeai as genai
from time import sleep
 
# Input your API key here (keep it secure in a real project) 
api_key = "YOUR_API_KEY_HERE"
 
# Configure the Gemini Pro API with the API key
genai.configure(api_key=api_key)  

# Set up generation configuration for the model  
generation_config = {
    "temperature": 1,  
    "top_p": 0.95,
    "top_k": 40,  
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain" ,
}

# Initialize the model (make sure this model name is available in the API)
model_name = "gemini-1.5-flash"  # Replace with your specific model name
 
# Load custom CSS for styling
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

# Display logo (Optional)
st.image('assets/logo.png', width=200)

# Title
st.title("Gemini Pro Chatbot")
st.write("Interact with the chatbot by typing your message below:")

# Chat History stored in memory
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display the chat history
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        st.markdown(f"<div class='chat-user'>User: {message['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bot'>Chatbot: {message['text']}</div>", unsafe_allow_html=True)

# User input field
user_input = st.text_input("Enter your message:", "")

# Display response on button click
if st.button("Send Message"):
    if user_input:
        # Add user input to chat history
        st.session_state.chat_history.append({'role': 'user', 'text': user_input})

        # Simulate chatbot response
        with st.spinner("Chatbot is thinking..."):
            sleep(2)  # Simulate delay
            try:
                # Send the input message to the model
                response = genai.generate_text(
                    model=model_name,
                    prompt=user_input,
                    **generation_config
                )

                chatbot_response = response.result
            except Exception as e:
                chatbot_response = f"Error: {e}"

        # Add chatbot response to chat history
        st.session_state.chat_history.append({'role': 'chatbot', 'text': chatbot_response})

        # Update the page with the new chat history
        st.experimental_rerun()
    else:
        st.error("Please enter a message before submitting.")
