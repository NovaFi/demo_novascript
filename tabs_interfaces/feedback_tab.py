import gradio as gr
import functions.respond_functions as respond_functions
from datetime import datetime
import csv
import os
import sys

# Callback function
def feedback_func(navigation, guidance, accuracy, interface, confusion_cause, favorite, more):
    if os.path.exists("data"):
        filename = "data/feedback.csv"
    else :
        filename = "feedback.csv"
        
    # Check if the feedback file already exists to determine if headers are needed
    file_exists = os.path.isfile(filename)
    
    # Get the current time for the feedback entry
    time = datetime.now().strftime("%H:%M:%S")
    
    # Open the feedback file in append mode, creating it if it does not exist
    with open(filename, mode='a', newline='') as file:
        # Initialize a CSV writer to write data into the file
        writer = csv.writer(file)
        
        # Write the header row if the file is new (does not exist yet)
        if not file_exists:
            writer.writerow(["Time", 'Navigation', 'Guidance', 'Accuracy', 'Interface', 'Confusion Cause', 'Favorite Part', 'More'])
        
        # Write the feedback data to the file
        writer.writerow([time, navigation, guidance, accuracy, interface, confusion_cause, favorite, more])
        
    # Display a message to the user confirming receipt of feedback
    gr.Info("We appreciate your valuable feedback!")


# Feedback tab interface definition
feedback_tab = gr.Interface(
    fn=feedback_func,
    inputs=[
        # Various input components for collecting feedback
        gr.Radio(label="How satisfied are you with the ease of navigating through the interface?", choices=["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]),
        gr.Radio(label="How satisfied are you with the guidance provided by the AI?", choices=["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]),
        gr.Radio(label="Based on your initial goal, how satisfied are you with the accuracy of the strategy generated?", choices=["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]),
        gr.Radio(label="Overall, how satisfied are you with your experience using this interface?", choices=["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]),
        gr.Textbox(label="What caused you the most confusion or frustration in this process ?", placeholder="Type here"),
        gr.Textbox(label="What did you like the most about the process?", placeholder="Type here"),
        gr.Textbox(label="Do you have any more feedback?", placeholder="Type here", lines=5),
    ],
    outputs=None,
)