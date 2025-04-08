# Math Problem Solver

An interactive Streamlit application for solving math problems using Mistral AI.

## Team Members
- Vikash Gupta (12321380)
- Khushdeep Saini (12316852)
- Satyam Upadhyay (12318963)

## Features
- Interactive chat interface for solving math problems
- Toggle between full solutions and hints
- Support for various math topics (Algebra, Calculus, Trigonometry, Statistics)
- Clean, responsive UI

## 🚨 Important: Mistral API Key Required
This application requires a valid Mistral AI API key to function properly. You must obtain and configure your API key for both local development and Streamlit Cloud deployment.

### Getting a Mistral API Key:
1. Go to [Mistral AI Console](https://console.mistral.ai/)
2. Sign up for an account if you don't have one
3. Navigate to the API keys section in your account
4. Create a new API key

## Deployment Instructions for Streamlit Cloud

### Step 1: Prepare Your Repository
Ensure your repository contains:
- app.py
- utils.py
- .streamlit/config.toml
- requirements.txt (or streamlit_requirements.txt)

### Step 2: Deploy on Streamlit Cloud
1. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub repository
4. Fill in the deployment information:
   - Repository: Your GitHub repository
   - Branch: main
   - Main file path: app.py

### Step 3: Configure Secrets (CRITICAL STEP)
1. After entering basic deployment info, click on "Advanced settings"
2. Under "Secrets", add the following exactly as shown:
   ```
   MISTRAL_API_KEY = "your-actual-mistral-api-key"
   ```
   Replace "your-actual-mistral-api-key" with your real Mistral API key

### Step 4: Complete Deployment
1. Click "Deploy"
2. Wait for the deployment to complete
3. Your app is now accessible via the provided Streamlit Cloud URL!

## Troubleshooting
- If you see a "401 Unauthorized" error, your API key is either invalid or not properly configured
- Ensure the API key is entered exactly as provided by Mistral AI, with no extra spaces
- If issues persist, try generating a new API key from the Mistral AI console

## Local Development
To run the application locally:
1. Clone the repository
2. Create a `.env` file in the root directory with:
   ```
   MISTRAL_API_KEY=your-api-key
   ```
3. Install required packages:
   ```
   pip install streamlit python-dotenv requests
   ```
4. Run the application:
   ```
   streamlit run app.py
   ```

## Dependencies
- streamlit
- python-dotenv
- requests