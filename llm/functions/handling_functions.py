import gradio as gr
from datetime import datetime
import csv
import os
import sys

def feedback_func(navigation, guidance, accuracy, interface, confusion_cause, favorite, more):

    filename = "data/feedback.csv"
    
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

def options_func(_, strategy_field, deposit_field, platform_field, stablecoi_field, crypto_asset_field):
    # Format the parameters received from the user into a string
    parameters = f"""Deposit amount = {deposit_field}, \nStableCoin = {stablecoi_field}, \nCrypto asset = {crypto_asset_field}, \nStrategy = {strategy_field}, \nPlatform = {platform_field}"""
    
    # Move to the next tab in the Gradio interface and return the formatted parameters
    return gr.Tabs(selected=2), parameters,
