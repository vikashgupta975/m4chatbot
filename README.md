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

## 🔥 Quick Deployment Guide
This app has been configured for **hassle-free deployment**! The API key is already hardcoded for demonstration purposes, so you can deploy it directly without configuring secrets.

### One-Click Deployment Steps:
1. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub repository
4. Set Main file path to: `app.py`
5. Click "Deploy"

That's it! Your app will work immediately with the built-in demo API key.

## For Production Use
While the demo API key works for quick deployments, for production use, it's recommended to use your own API key:

### Getting a Mistral API Key:
1. Go to [Mistral AI Console](https://console.mistral.ai/)
2. Sign up for an account if you don't have one
3. Navigate to the API keys section in your account
4. Create a new API key

### Adding Your Own API Key (Optional):
1. After entering basic deployment info, click on "Advanced settings"
2. Under "Secrets", add the following:
   ```
   MISTRAL_API_KEY = "your-actual-mistral-api-key"
   ```
   Replace "your-actual-mistral-api-key" with your real Mistral API key
3. This will override the demo key with your own key

## Additional Information

### Application Architecture
The application uses a flexible API key system:
1. First tries to use Streamlit Cloud secrets
2. Then checks for environment variables
3. Falls back to a built-in demo key as a last resort

This ensures the application works regardless of deployment method.

### Troubleshooting
- If you encounter rate limits, consider adding your own API key
- The demo key is shared, so it may occasionally be rate-limited
- Check the Mistral AI documentation for current rate limits

### Local Development
To run the application locally:
1. Clone the repository
2. Optional: Create a `.env` file with your own API key:
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