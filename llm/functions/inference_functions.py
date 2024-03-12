import requests
from openai import OpenAI
import anthropic
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# -------------------------------------------------------------
# ___________________________ Llama ___________________________
# _____________________________________________________________

def llama_prompt(prompt, systemPrompt="", history =[]):
    bodyRequest= {
        "model" : "llama2",
        # "prompt" : prompt,
        "messages" : [{"role" : "user", "content" : prompt}],
        "stream" : False
    }
    
    response = requests.post("http://localhost:11434/api/chat", json=bodyRequest)

    if response.status_code == 200:
    #     output = response.json()["response"]
        output = response.json()["message"]["content"]

    else:
        print("Failed to prompt the LLM : ", response.status_code)
        return "No Response :("

    return output

# -------------------------------------------------------------
# ___________________________ OpenAI ___________________________
# _____________________________________________________________


def openai_prompt(prompt, systemPrompt="", history =[]) :
    chatHistory = [{"role" : "system", "content" : systemPrompt}]
    # chatHistory.clear()

    input_token_count = 0
    for interaction in history : # history variable comes from gradio interface, we first add the system prompt and fetch the chat history
        user_input = interaction[0]
        if user_input is None :
            user_input = ""
        assistant_response = interaction[1]
        chatHistory.append({"role": "user", "content": user_input})
        chatHistory.append({"role": "assistant", "content": assistant_response})
        input_token_count += len(user_input.split())  # Rough token count for user input
        input_token_count += len(assistant_response.split())  # Rough token count for assistant response

    chatHistory.append({"role" : "user", "content" : prompt}) # Add the new question
    # input_token_count += len(prompt.split())

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    try:
        # Attempt to use GPT-4 model
        res = client.chat.completions.create(
            model="gpt-4-1106-preview",
            temperature=0,
            # max_tokens=120000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            messages=chatHistory,
        )
    except Exception as e:
        print(f"\n\nException during openAI request : {e}\n\n")
        # If the GPT-4 request fails, fall back to GPT-3.5
        print("GPT-4 request failed, falling back to GPT-3.5:", str(e))
        res = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            temperature=0,
            max_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            messages=chatHistory,
        )

    # Extract the response content
    output = res.choices[0].message.content.strip()
    output_token_count = len(output.split())
    
    return output


def claude_prompt(prompt, systemPrompt="", history =[]) :
    chatHistory = []

    input_token_count = 0
    for interaction in history : # history variable comes from gradio interface, we first add the system prompt and fetch the chat history
        user_input = interaction[0]
        if user_input is None or user_input == "" :
            user_input = "none"
        assistant_response = interaction[1]
        chatHistory.append({"role": "user", "content": user_input})
        chatHistory.append({"role": "assistant", "content": assistant_response})
        input_token_count += len(user_input.split())  # Rough token count for user input
        input_token_count += len(assistant_response.split())  # Rough token count for assistant response

    chatHistory.append({"role" : "user", "content" : prompt}) # Add the new question
    # input_token_count += len(prompt.split())

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=os.getenv('CLAUDE_API_KEY'),
    )

    try:
        res = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=chatHistory,
            system = systemPrompt,
        )
        # Extract the response content
        output = res.content[0].text
        output_token_count = len(output.split())
        return output

    except Exception as e:
        print(f"\n\nException during Claude request : {e}\n\n")
        print("Switching to OpenAI\n")
        return openai_prompt(prompt=prompt, systemPrompt=systemPrompt, history=history)

    