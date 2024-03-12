import gradio as gr
import functions.respond_functions as respond_functions
import utils
from datetime import datetime
import csv
import os
import sys

# Callback function
def options_func(_, strategy_field, deposit_field, platform_field, stablecoi_field, crypto_asset_field):
    # Format the parameters received from the user into a string
    parameters = f"""Deposit amount = {deposit_field}, \nStableCoin = {stablecoi_field}, \nCrypto asset = {crypto_asset_field}, \nStrategy = {strategy_field}, \nPlatform = {platform_field}"""
    
    # Move to the next tab in the Gradio interface and return the formatted parameters
    return gr.Tabs(selected=2), parameters,


# Options tab interface definition
options_tab = gr.Interface(
    fn=options_func,
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