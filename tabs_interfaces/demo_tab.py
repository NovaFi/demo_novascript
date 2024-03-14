# Import necessary libraries
import gradio as gr
import requests
import json

def submit(code):
    # Endpoint URL for code deployment; currently set to localhost for testing
    url = "http://localhost:5007/deploy"
    
    # Prepare the data payload with the code to be deployed
    data = {
        "code": str(code)
    }
    # Set headers for the HTTP request
    headers = {
        'Content-Type': 'application/json',
    }

    # Convert the Python dictionary to a JSON string
    json_data = json.dumps(data)

    # Perform a POST request to the deployment URL
    response = requests.post(url, data=json_data, headers=headers)
    
    # Check the status code of the response
    if response.status_code == 200:
        # Convert response to JSON format if the request was successful
        json_response = response.json()
    else:
        # Print error if the request failed
        print("Error:", response.text)
        return "error", "error"
    
    # Return the formatted code and deployment result URL
    # return "\n".join(json_response["code"]), json_response["deploymentResult"]["explorerUrl"]

    return "\n".join(json_response["code"]), gr.Button("View on BlockChain explorer", link = json_response["deploymentResult"]["explorerUrl"])

link = gr.Markdown(visible = False)

# Create a Gradio interface for code submission
code_submit_component = gr.Interface(
    fn=submit,  # Function to be called when the interface is used
    inputs=gr.Code(
        label = "Code",
        value="// Try typing something like...\n// print(5 + 2)",  # Default text in the code input area
        language="javascript",  # Language for syntax highlighting
        interactive=True,  # Specifies whether the input is interactive
    ),
    outputs=[
        gr.Code(
            label = "Compiled"
        ),  # Output field for processed code
        # gr.Markdown()  # Output field for the deployment result as Markdown text

        gr.Button(
            "View on BlockChain explorer",
            link = None,
        )
    ],
    allow_flagging="never",  # Disable flagging of submissions
    title="Code Executor",  # Title of the interface
    description="Write code in the block and press submit to see the result.",  # Description of the interface's purpose
    examples=["print(5 * 10)", "print(21 / 3)"],  # Examples to demonstrate usage
)
