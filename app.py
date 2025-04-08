import streamlit as st
import os
from utils import generate_math_solution

# Page configuration
st.set_page_config(
    page_title="Vikash Gupta (12321380) - Math Problem Solver",
    page_icon="🧮",
    layout="centered"
)

# API key from environment variable or directly provided
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "KgkyAsK33bPBZ8FVRbmIjvJAJH7SVhpW")

# Initialize session state for chat history if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Application title and description
st.title("Vikash Gupta (12321380)")
st.subheader("Math Problem Solver")
st.markdown("""
This application helps you solve math problems step-by-step using advanced AI.
Simply type your math problem in the chat box below and get a detailed solution.
""")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Enter your math problem here...")

# Process user input
if user_prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    # Display assistant message (thinking...)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            # Call the Mistral API to solve the math problem
            solution = generate_math_solution(user_prompt, MISTRAL_API_KEY)
            
            # Update placeholder with solution
            message_placeholder.markdown(solution)
            
            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": solution})
            
        except Exception as e:
            error_message = f"Error: {str(e)}"
            message_placeholder.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# Add a clear button to reset the chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Footer
st.markdown("""
---
Developed by Vikash Gupta (12321380) | Powered by Mistral AI
""")
