# NovaScript Demo

This repository contains a demo for NovaScript compilation and deployment onchain using Gradio.

## Prerequisites

- Node.js
- Python

## Steps to Run the Project

1. Clone the `nano-rust` repository:
   ```
   git clone https://github.com/NovaFi/nano-rust.git
   ```

2. Navigate to the cloned repository and start the server:
   ```
   cd nano-rust
   node app.js
   ```
   This will start a server on port 5007, which is required for step 3.

3. In the current repository, run the Python script:
   ```
   python app.py
   ```
   
4. Access the Gradio interface in your web browser to interact with the demo.

## Additional Information

- The `nano-rust` repository is used to provide the necessary server functionality for the demo.
- The `app.py` script in the current repository utilizes Gradio to create an interactive demo for NovaScript creation, compilation and deployment.
