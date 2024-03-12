import gradio as gr
import functions.respond_functions as respond_functions
import functions.handling_functions as handling_functions
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
                    value=[[None, "Let's start building your strategy !\n\nPlease describe to me what type of X strategy you would like to implement using A,B,C platforms."]]
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
                    lines=2,
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

# Options tab interface definition
options_tab = gr.Interface(
    fn=handling_functions.options_func,
    clear_btn=gr.Button(visible=False),
    submit_btn=gr.Button(visible=False),
    inputs=[
        # Various input components for strategy options
        gr.Markdown(utils.options_tab_HTML),
        gr.Radio(["Dollar Cost Average", "Take Profit", "Solana Staking"], label="What strategy would you like to program ?", info="This will lay the foundation for the automation logic"),
        gr.Text(label="How much would you like to invest in this strategy ?", info="Type the corresponding USD value", placeholder="$0.00"),
        gr.Dropdown(["Marginfi", "Kamino", "Orca", "Raydium", "Solend", "Mango", "Drift", "Marinade", "Sol Blaze", "Jito", "Meteora", "Parcl", "Hubble", "UXD"], label="Which platform will this strategy use ?", info="This information allows novascript to connect to the platform's API", multiselect=True, allow_custom_value=True),
        gr.Radio(["USDC", "USDH", "UXD"], label="What stablecoin would you like to use ?", info="Select a stablecoin"),
        gr.Radio(["SOL", "JitoSol", "mSOL", "BTC", "ETH"], label="What crypto asset would you like to invest with ?", info="Select a crypto asset"),
    ],
    outputs=[],
)

# Feedback tab interface definition
feedback_tab = gr.Interface(
    fn=handling_functions.feedback_func,
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

# Starting tab content definition
def starting_tab():
    with gr.Column():
        # Display the starting page HTML content
        gr.Markdown(utils.starting_page_HTML)
