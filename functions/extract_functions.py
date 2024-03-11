import re  # Import the regular expressions library

def extract_code_blocks(text):
    # Define the regex pattern to find JavaScript code blocks
    js_pattern = r"```javascript\n(.*?)\n```"
    # Define the regex pattern to find bash (shell script) code blocks
    sh_pattern = r"```bash\n(.*?)\n```"
    
    # Use re.DOTALL flag to make '.' match newline characters as well
    js_matches = re.findall(js_pattern, text, re.DOTALL)
    sh_matches = re.findall(sh_pattern, text, re.DOTALL)
    
    # Initialize a dictionary to store the extracted code blocks
    all_matches = {
        "novascript": "novascript will be displayed here",  # Placeholder text for JavaScript
        "bash": "Bash commands will be displayed here",  # Placeholder text for Bash commands
    }
    
    # Update the dictionary with the first JavaScript match, if any
    if len(js_matches) > 0:
        all_matches["novascript"] = js_matches[0]
    
    # Update the dictionary with all Bash matches joined by newlines, if any
    if len(sh_matches) > 0:
        all_matches["bash"] = "\n".join(sh_matches)

    # Return the dictionary containing the extracted code blocks
    return all_matches


def extract_logic(input_text):
    # Find the index of the first occurrence of triple backticks
    start_index = input_text.find("```")
    # Find the index of the next occurrence of triple backticks after the start_index
    end_index = input_text.find("```", start_index + 3)
    
    # Extract the string enclosed by triple backticks, if found
    if start_index != -1 and end_index != -1:
        # Return the extracted string, removing the backticks and leading/trailing spaces
        return input_text[start_index + 3:end_index].strip()
    else:
        # Return None if the pattern is not found
        return None
