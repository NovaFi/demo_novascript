import gradio as gr
import functions.respond_functions as respond_functions
import utils

def chat_tab(params_component):
    # Define a global variable to hold parameters for the chat
    global prompt_params
    with gr.Blocks():
        # Create a row layout with unequal height columns
        with gr.Row(equal_height=False):
            # Main column for the chatbot and script generation, taking 3/4th of the width
            with gr.Column(scale=3):
                # Initialize the chatbot component
                chatbot = gr.Chatbot(
                    show_copy_button=True,
                    show_share_button=True,
                    # Default message to start the chat
                    value=[[None, "please describe your strategy, or start a conversation to build your strategy together"]]
                )

                # Textbox for user to input their message
                msg = gr.Textbox(label="", autofocus=True, placeholder="Describe your Investment Strategy...")

                # Row layout for buttons
                with gr.Row():
                    # Button to trigger script generation
                    generate_script_btn = gr.Button("Generate NovaScript")

                # Code block for displaying generated novascript
                code_novascript = gr.Code(
                    label="novascript",
                    scale=1,
                    language="javascript",
                    interactive=True,
                    value="novascript will be displayed here",
                    visible=True,
                    lines=1,
                    render=True,
                )

                # Code block for displaying Bash commands
                code_bash = gr.Code(
                    label="Bash",
                    scale=1,
                    language="shell",
                    interactive=True,
                    value="Bash commands will be displayed here",
                    visible=True,
                    lines=10,
                    render=True,
                )

            # Side column for additional parameters, taking 1/4th of the width
            with gr.Column(scale=1):
                # Render the parameters component passed to the function
                prompt_params = params_component.render()

            # Hidden text component to track the conversation phase
            conversation_phase = gr.Text(value="questioning", visible=False)

            # Hidden text component to track the number of skip attempts
            skip_tries = gr.Text(visible=False)

            # Submit action for the message textbox
            msg.submit(respond_functions.respond, inputs=[msg, chatbot, prompt_params, prompt_params, conversation_phase], outputs=[msg, chatbot, code_novascript, code_bash, prompt_params, conversation_phase, skip_tries], js=utils.autoscroll_JS)

            # Click action for the generate script button
            generate_script_btn.click(respond_functions.skip_to_script, inputs=[msg, chatbot, prompt_params, prompt_params, conversation_phase, skip_tries], outputs=[msg, chatbot, code_novascript, code_bash, prompt_params, conversation_phase, skip_tries], js=utils.autoscroll_JS)
