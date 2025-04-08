import requests
import json

def generate_math_solution(problem, api_key):
    """
    Generate a solution for a given math problem using Mistral AI API.
    
    Args:
        problem (str): The math problem to solve
        api_key (str): Mistral API key
        
    Returns:
        str: The step-by-step solution to the math problem
    """
    # API endpoint
    url = "https://api.mistral.ai/v1/chat/completions"
    
    # Headers with API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Create a prompt with specific instructions for math problem solving
    system_prompt = """
    You are a math tutor named Vikash Gupta (ID: 12321380). Your role is to solve mathematics problems
    step by step, showing all work clearly. Explain your approach thoroughly so students can
    understand the underlying concepts and methods. Format your responses with clear steps,
    using markdown for equations when appropriate. Focus on providing accurate, educational
    answers that help students learn.
    """
    
    # Data payload
    data = {
        "model": "mistral-small-latest",  # Use the most appropriate Mistral model
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Please solve this math problem step by step: {problem}"}
        ],
        "temperature": 0.2,  # Lower temperature for more focused, deterministic responses
        "max_tokens": 2000  # Ensure we have enough tokens for detailed explanations
    }
    
    try:
        # Make API request
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        
        # Extract and return the solution text
        solution = result['choices'][0]['message']['content']
        return solution
        
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response:
            error_detail = e.response.text
            return f"Error communicating with Mistral AI: {str(e)}\nDetails: {error_detail}"
        else:
            return f"Error communicating with Mistral AI: {str(e)}"
    
    except (KeyError, IndexError) as e:
        return f"Error parsing the Mistral AI response: {str(e)}"
    
    except Exception as e:
        return f"Unexpected error: {str(e)}"
