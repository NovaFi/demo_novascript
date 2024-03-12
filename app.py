# Import necessary libraries
import gradio as gr
import random
import time
from datetime import datetime
import csv
import os
import re
import utils
import functions.inference_functions as inference_functions
import tabs_interfaces.demo_tab
import functions.extract_functions as extract_functions
import functions.respond_functions as respond_functions
import tabs_interfaces.chat_tab
import tabs_interfaces.feedback_tab
import tabs_interfaces.options_tab
import tabs_interfaces.starting_tab

# Define the path to the feedback CSV file
filename = 'data/feedback.csv'

# Define a Gradio text component for entering automation logic
prompt_params = gr.Text(
            label="Automation Logic",  # Label for the input field
            every=1,  # Update frequency, not commonly used for gr.Text
            interactive=False,  # Specifies whether the component is interactive
            visible=True  # Make the component visible
        )


# Create a Gradio app with a monochrome theme
with gr.Blocks(theme=gr.themes.Monochrome()) as app:
    # Define a tabbed interface
    with gr.Tabs() as tabs:
        # Define the first tab as the starting point
        with gr.TabItem("Start here", id=0):
            tabs_interfaces.starting_tab.starting_tab()  # Render the starting tab's interface

        # Define the second tab for the first step
        with gr.TabItem("Step 1", id=1):
            # Render options tab within a column layout
            with gr.Column():
                tabs_interfaces.options_tab.options_tab.render()
                
                # Define a submit button
                submit_btn = gr.Button("Submit", visible=True)
                # Specify the action for the button click, linking to options_func function
                submit_btn.click(
                    fn=tabs_interfaces.options_tab.options_func,
                    inputs=tabs_interfaces.options_tab.options_tab.input_components,
                    outputs=[tabs, prompt_params]
                )
            
        # Define the third tab for the second step
        with gr.Tab("Step 2", id=2):
            tabs_interfaces.chat_tab.chat_tab(params_component=prompt_params)  # Render chat tab with prompt_params component

        # Define the fourth tab for the third step
        with gr.Tab("Step 3", id=3):
            tabs_interfaces.demo_tab.code_submit_component.render()  # Render the code submission component
        
        # Define the fifth tab for collecting feedback
        with gr.Tab("Feedback", id=4):
            with gr.Column():
                # Display feedback form instructions or text
                gr.Markdown(utils.feedback_tab_HTML)

                tabs_interfaces.feedback_tab.feedback_tab.render()  # Render the feedback form

# Launch the app with specified height and sharing options
app.launch(share=True)


