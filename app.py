import streamlit as st
import requests
import uuid

# --- App Title and Description ---
st.set_page_config(page_title="AI Career Counsellor", page_icon="🤖")
st.title("🤖 AI Virtual Career Counsellor")
st.write("Welcome! I'm here to help you explore career paths in Tech, Arts, and Commerce. Ask me something like, 'What jobs are there in tech?' or 'I'm interested in creative careers.'")

# --- Session State Initialization ---
# This is to store the conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Use a unique session ID for the conversation
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Handle User Input ---
if prompt := st.chat_input("What would you like to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Get Bot Response from Rasa ---
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("...") # Thinking indicator

        try:
            # The URL for the Rasa REST webhook
            rasa_url = "http://localhost:5005/webhooks/rest/webhook"
            
            # The payload to send to Rasa
            payload = {
                "sender": st.session_state.session_id,
                "message": prompt
            }
            
            # Send the request to the Rasa server
            response = requests.post(rasa_url, json=payload)
            response.raise_for_status() # Raise an exception for bad status codes
            
            bot_responses = response.json()
            
            full_response = ""
            if bot_responses:
                # Concatenate all bot messages into one string
                full_response = "\n".join([r.get("text", "") for r in bot_responses])
            else:
                full_response = "I'm sorry, I didn't get a response. Please try again."

            message_placeholder.markdown(full_response)
            # Add bot response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except requests.exceptions.RequestException as e:
            message_placeholder.error(f"Failed to connect to Rasa server: {e}")
            st.session_state.messages.append({"role": "assistant", "content": f"Error: Could not connect to the bot. Is the Rasa server running?"})
            