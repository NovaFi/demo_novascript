import gradio as gr
import functions.respond_functions as respond_functions
import utils

# Starting tab content definition
def starting_tab():
    with gr.Column():
        # Display the starting page HTML content
        gr.Markdown(utils.starting_page_HTML)