import gradio as gr  # Importing Gradio for creating GUI applications
import requests  # Importing requests to make HTTP requests
import json  # Importing json for JSON parsing and serialization

def submit(code):
    # Set the URL of the deployment endpoint
    # url = "http://176.9.238.145:5007/deploy"  # Unused, alternative URL for deployment
    url = "http://localhost:5007/deploy"  # Localhost URL for the deployment service
    data = {
        "code" : str(code)  # Package the submitted code into a data dictionary
    }
    headers = {
    'Content-Type': 'application/json',  # Specify the content type as JSON
    }  

    json_data = json.dumps(data)  # Serialize the data dictionary to a JSON formatted string

    response = requests.post(url, data=json_data, headers=headers)  # Send a POST request to the URL with the serialized data and headers
    print(response)  # Print the response object for debugging
    if response.status_code == 200:  # Check if the request was successful
        json_response = response.json()  # Parse the JSON response
    else:
        print("Error:", response.text)  # Print error if request failed
        return "error", "error"  # Return error indication
    
    # Return formatted code and the deployment result URL
    return  "\n".join(json_response["code"]), json_response["deploymentResult"]["explorerUrl"]

# Create a Gradio interface for the submit function
code_submit_component = gr.Interface(
    fn = submit,
    inputs = gr.Code(  # Define the input as a code editor
        value = "Write your code here...",  # Default placeholder text
        language="javascript",  # Set the language for syntax highlighting
        interactive=True,  # Allow interactive editing
    ),

    outputs = [
        gr.Code(),  # Define the first output as a code block
        gr.Text()  # Define the second output as a text block
    ],
    title="Code Executor",  # Title of the interface
    description="Write code in the block and press submit to see the result."  # Description of what the interface does
)

# Wrap the Gradio interface in a Blocks container
with gr.Blocks() as app:
    with gr.Column() :  # Organize the interface in a column layout
        code_submit_component.render()  # Render the interface component
    

app.launch()  # Launch the Gradio app when the script is executed
