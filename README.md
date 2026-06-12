# Custom AI Agent

## Overview

Custom AI Agent is a command-line coding assistant powered by Google's Gemini 2.5 Flash model.

The agent can:
- Read files from disk
- Create new files
- Modify existing files
- Execute programs and scripts
- Interact through natural language prompts directly from the terminal

## Installation

### Prerequisites

- Python 3.12+
- uv

Install uv:

```bash
pip install uv
```

### Clone The Repository

```bash
git clone https://github.com/tian-suan-ji/custom-ai-agent.git
cd custom-ai-agent
```

### Install Dependencies

```bash
uv sync
```
## Configuration

This project requires a Gemini API key to function.
Create a `.env` file in the project's root directory.

GEMINI_API_KEY="Your API Key Here"

You can obtain a Gemini API key from Google AI Studio.

## Usage

Run the agent in the terminal:
```bash
uv run main.py "<your prompt>"
```

### Example

```bash
uv run main.py "Create a Python script that prints Hello World"
```

## License

This project is licensed under the MIT License.
