import streamlit as st
import os
from utils import generate_math_solution

# Page configuration
st.set_page_config(
    page_title="Vikash Gupta (12321380) - Math Problem Solver",
    page_icon="🧮",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .title-container {
        background-color: #1E88E5;
        padding: 2rem 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .chat-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .user-message {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #1E88E5;
    }
    .assistant-message {
        background-color: #F5F5F5;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #4CAF50;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #1E88E5;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        background-color: #1E88E5;
        color: white;
        border-radius: 10px;
    }
    /* Animation for the loader */
    .loader {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(0,0,0,.1);
        border-radius: 50%;
        border-top-color: #1E88E5;
        animation: spin 1s ease-in-out infinite;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    /* Math symbols decoration */
    .math-symbol {
        font-size: 24px;
        font-weight: bold;
        display: inline-block;
        margin: 0 5px;
        color: #1E88E5;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
""", unsafe_allow_html=True)

# API key from environment variable or directly provided
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "KgkyAsK33bPBZ8FVRbmIjvJAJH7SVhpW")

# Initialize session state for chat history if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Application title and description
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.markdown('<h1 style="font-size: 2.5rem;">Vikash Gupta (12321380)</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="font-size: 1.8rem;">Advanced Math Problem Solver</h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Two-column layout
col1, col2 = st.columns([2, 1])

with col2:
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    ### How to Use
    1. **Enter your math problem** in the chat box
    2. **Wait for the solution** to be generated
    3. **Review the step-by-step explanation**
    4. **Ask follow-up questions** if needed
    
    ### Example Problems
    - Solve x² - 4 = 0
    - Find the derivative of sin(x)²
    - Integrate x³ + 2x² + 3x
    - What is the limit of (1+x)^(1/x) as x→0?
    - Solve the system: 2x + y = 5, x - y = 1
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add decorative math elements
    st.markdown('<div style="text-align: center; margin-top: 2rem;">', unsafe_allow_html=True)
    st.latex(r'''
    \begin{align}
    e^{i\pi} + 1 &= 0 \\
    \int_{-\infty}^{\infty} e^{-x^2} dx &= \sqrt{\pi} \\
    \frac{d}{dx}[e^x] &= e^x
    \end{align}
    ''')
    
    # Add floating math symbols
    st.markdown('''
    <div style="text-align: center; margin-top: 1rem;">
        <span class="math-symbol">∑</span>
        <span class="math-symbol" style="animation-delay: 0.5s;">∫</span>
        <span class="math-symbol" style="animation-delay: 1s;">π</span>
        <span class="math-symbol" style="animation-delay: 1.5s;">√</span>
        <span class="math-symbol" style="animation-delay: 2s;">∞</span>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col1:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat messages with custom styling
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

# Add a separator before the input
st.markdown('<hr style="margin: 1.5rem 0; border-color: #E0E0E0;">', unsafe_allow_html=True)

# User input with custom styling
st.markdown('<div style="margin-bottom: 1rem; font-weight: bold;">Enter your math problem:</div>', unsafe_allow_html=True)
user_prompt = st.chat_input("Type your math problem here...", key="math_problem_input")

# Process user input
if user_prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Display user message with custom styling
    st.markdown(f'<div class="user-message">{user_prompt}</div>', unsafe_allow_html=True)
    
    # Display thinking message
    thinking_placeholder = st.empty()
    thinking_placeholder.markdown(
        '<div style="padding: 1rem; background-color: #F5F5F5; border-radius: 10px; margin-bottom: 1rem; border-left: 5px solid #FFA726;">'
        '<i>Solving your math problem...</i> <div class="loader"></div>'
        '</div>', 
        unsafe_allow_html=True
    )
    
    try:
        # Call the Mistral API to solve the math problem
        solution = generate_math_solution(user_prompt, MISTRAL_API_KEY)
        
        # Update thinking message with solution
        thinking_placeholder.markdown(f'<div class="assistant-message">{solution}</div>', unsafe_allow_html=True)
        
        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": solution})
        
    except Exception as e:
        error_message = f"Error: {str(e)}"
        thinking_placeholder.markdown(
            f'<div style="padding: 1rem; background-color: #FFEBEE; border-radius: 10px; '
            f'margin-bottom: 1rem; border-left: 5px solid #F44336;">{error_message}</div>', 
            unsafe_allow_html=True
        )
        st.session_state.messages.append({"role": "assistant", "content": error_message})

st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container div

# Control panel
st.markdown('<div style="margin-top: 1.5rem; display: flex; justify-content: center;">', unsafe_allow_html=True)
if st.button("🗑️ Clear Chat History", key="clear_button"):
    st.session_state.messages = []
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Footer with gradient
st.markdown("""
<div class="footer">
    <div style="font-size: 1.2rem; font-weight: bold;">Vikash Gupta (12321380)</div>
    <div style="font-size: 0.9rem; margin-top: 0.5rem;">Powered by Mistral AI | Advanced Math Problem Solver</div>
</div>
""", unsafe_allow_html=True)
