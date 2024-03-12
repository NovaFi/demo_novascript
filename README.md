# NovaScript Demo

This repository contains a demo for NovaScript compilation and deployment onchain using Gradio.

![Error](/screenshots/options1)
![Error](/screenshots/chat1)
![Error](/screenshots/chat2)
![Error](/screenshots/chat3)
![Error](/screenshots/chat4)
![Error](/screenshots/demo1)
<!-- ![Error](/screenshots/options1)
![Error](/screenshots/options1) -->

## Prerequisites

Before running the project, ensure you have the following:

- Node.js installed
- Python installed
- OpenAI API key
- Claude API key

## Getting Started

Follow these steps to set up and run the project:

1. Clone the Nano Rust repository:
   ```
   git clone https://github.com/NovaFi/nano-rust.git
   ```

2. Navigate to the cloned repository directory:
   ```
   cd nano-rust
   ```

3. Install the required dependencies:
   ```
   npm install
   ```

4. Start the server:
   ```
   node app.js
   ```
   This will start the server on port 5007, enabling the demo for NovaScript compilation and deployment on-chain.

5. Open a new terminal window and navigate to the directory of the current repository (the one containing this README file).

6. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

7. Run the Python application:
   ```
   python app.py
   ```
   This application uses Gradio for the user interface.

8. Copy the `.env.example` file to `.env`:
   ```
   cp .env.example .env
   ```

9. Open the `.env` file and fill in the OpenAI and Claude API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   CLAUDE_API_KEY=your_claude_api_key
   ```
If the two api keys are provided, the default model to use is Claude Opus. If only one is provided, it will be used as the default model.


10. Access the application through the provided URL in the terminal output.

## Usage

- Use the Gradio interface to interact with the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
