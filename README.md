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

## Deployment Instructions for Streamlit Cloud

1. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub repository
4. Fill in the following deployment information:
   - Repository: Your GitHub repository
   - Branch: main
   - Main file path: app.py

5. **Important**: Add your API key as a secret
   - Click on "Advanced settings"
   - Under "Secrets", add the following:
     ```
     MISTRAL_API_KEY = "your-mistral-api-key"
     ```

6. Click "Deploy"
7. Your app is now deployed and accessible via the provided URL!

## Dependencies
- streamlit
- python-dotenv
- requests

## Local Development
To run the application locally:
1. Clone the repository
2. Create a `.env` file with `MISTRAL_API_KEY=your-api-key`
3. Run `streamlit run app.py`