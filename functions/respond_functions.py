import gradio as gr
import re
import time
from datetime import datetime
import utils
import functions.inference_functions as inference_functions
import functions.extract_functions as extract_functions
import os

def skip_to_script(message, history, parameters, logic, conversation_phase, skip_tries):
    print(f"Skip tries : {skip_tries}")
    # Check if the user has already tried to skip or if all questions have been asked
    if skip_tries != "Already tried" and skip_tries != "All done":
        # Warn that there are still questions to be asked
        gr.Warning("We still have questions to ask")
        time.sleep(2)  # Wait for 2 seconds
        gr.Info("Click on 'Generate NovaScript' again to proceed anyway")
        
        skip_tries = "Already tried"  # Update the skip tries status
        # Return without making any changes, but update the skip_tries status
        return None, history, "novascript will be displayed here", "Bash commands will be displayed here", logic, conversation_phase, skip_tries
        
    # If the user clicks again or all questions have been asked, proceed to script generation
    message = "Fill the parameters and automation logic and jump to the last phase of generating automation logic then nanoscript. Do not ask me a single question by force. Proceed with generating the last phase without asking me a single question, fill in the blanks yourself"
    # Call the respond function with updated parameters for generating the script
    return respond(message, history, parameters, logic, conversation_phase, skipping=True, skip_tries=skip_tries)

def respond(message, history, parameters, logic, conversation_phase, skipping=False, skip_tries=None):
    if skipping:
        conversation_phase = "generating"  # Update the phase to generating if skipping is True

    # Determine the system prompt based on the current phase
    if conversation_phase == "questioning":
        print("\nQuestioning phase\n")
        systemPrompt = f"Context : {utils.systemPrompt_questions} \n Parameters : {parameters}"
    else:
        print("\nGeneration phase\n")
        systemPrompt = f"Context : {utils.systemPrompt_expert} \n Parameters : {parameters}"
    
    
    # Call the inference function with the provided message and system prompt
    if (os.getenv('CLAUDE_API_KEY') != "" and not os.getenv('CLAUDE_API_KEY') is None):
        response = inference_functions.claude_prompt(prompt=message, systemPrompt=systemPrompt, history=history)
        
    elif (os.getenv("OPENAI_API_KEY") != "" and not os.getenv('OPENAI_API_KEY') is None) :
        response = inference_functions.openai_prompt(prompt=message, systemPrompt=systemPrompt, history=history)

    else : # In case no API KEY is provided
        history.append((message, "No API key provided, check .env please"))
        return "", history, None, None, logic, conversation_phase, skip_tries
        
    if "READY" in response and not "READY?" in response:
        print("\n\nTerminating ...\n\n")
        skip_tries = "All done"  # Update skip_tries to allow generating novascript
        logic_extracted = extract_functions.extract_logic(response)
        if logic_extracted is not None:
            logic = logic_extracted  # Update the logic only if new logic is extracted
        
        message = None  # Reset the message for the next interaction

    if skipping:
        message = ""  # Clear the message if skipping to the next phase

    # Append the user message and system response to the history
    history.append((message, response))

    # Extract code blocks from the response
    code_blocks = extract_functions.extract_code_blocks(response)  # Returns a dictionary with novascript and bash
    
    # Return updated values, including any extracted code blocks and updated conversation state
    return "", history, code_blocks["novascript"], code_blocks["bash"], logic, conversation_phase, skip_tries
