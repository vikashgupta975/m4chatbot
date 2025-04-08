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


def generate_math_hint(problem, api_key):
    """
    Generate a helpful hint for a given math problem using Mistral AI API.
    The hint provides guidance without giving away the full solution.
    
    Args:
        problem (str): The math problem to provide a hint for
        api_key (str): Mistral API key
        
    Returns:
        str: A helpful hint for approaching the math problem
    """
    # API endpoint
    url = "https://api.mistral.ai/v1/chat/completions"
    
    # Headers with API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Create a prompt with specific instructions for generating math hints
    system_prompt = """
    You are a helpful math tutor named Khushdeep Saini (ID: 12316852). Your role is to provide 
    thoughtful hints for mathematics problems without giving away the full solution. Give students 
    just enough guidance to help them make progress on their own. Provide a conceptual hint first, 
    followed by a more specific hint that points them in the right direction. Use markdown for 
    equations when appropriate. Remember, your goal is to help students learn by guiding them 
    towards the solution, not solving it for them.
    """
    
    # Data payload
    data = {
        "model": "mistral-small-latest",  # Use the most appropriate Mistral model
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Please provide a helpful hint for this math problem: {problem}"}
        ],
        "temperature": 0.3,  # Slightly higher temperature for more creative hints
        "max_tokens": 1000  # Fewer tokens needed for hints vs full solutions
    }
    
    try:
        # Make API request
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        
        # Extract and return the hint text
        hint = result['choices'][0]['message']['content']
        return hint
        
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response:
            error_detail = e.response.text
            return f"Error generating hint: {str(e)}\nDetails: {error_detail}"
        else:
            return f"Error generating hint: {str(e)}"
    
    except (KeyError, IndexError) as e:
        return f"Error parsing the hint response: {str(e)}"
    
    except Exception as e:
        return f"Unexpected error generating hint: {str(e)}"
