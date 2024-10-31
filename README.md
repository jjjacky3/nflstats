# NFLStats

NFLStats is a powerful tool that allows you to query structured NFL data using natural language. Built with LangChain and powered by OpenAI's LLM, it features a user-friendly interface developed using the Streamlit library.

I’ve deployed the NFLStats app on the free to use [Streamlit Community Cloud](https://streamlit.io/cloud) with [2024 play by play data](https://github.com/nflverse/nflverse-data/releases/tag/pbp). You can try it out here: [NFLStats](https://nflstats-jacky.streamlit.app/)

## Introduction
While LLMs are impressive, I often wonder how they can answer questions without access to specific knowledge. For instance, how do they tackle NFL-related inquiries? Can they intelligently search the web for answers? What if the data isn’t publicly available or is formatted as structured text rather than natural language?

Interestingly, LLM agents can help address these challenges. This concept is based on the paper titled "ReAct: Synergizing Reasoning and Acting in Language Models." An LLM agent can reason through your prompts and suggest actions, such as querying a dataset, to tackle the problem. The agent also has memory capabilities to support sequential reasoning.

This project is a very simple chatbot using LangChain's CSV agent with OpenAI's ChatGPT LLM to answer questions about NFL games. The agent leverages the LLM to understand the questions and generates a sequence of data queries against the NFL play-by-play data in the CSV files, enabling it to provide accurate answers.

## Installation

To get started, follow these steps:

1. **Install Python**: Download and install [Python 3.12.6](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe) for optimal compatibility.
2. **Set Up Development Environment**:
   - Install Visual Studio Code and the Python extension.
   - Install Git and Git Desktop.
3. **Clone the Repository**:
   ```
   git clone <repository-url>
4. **Set Up a Virtual Environment**:
   ```
   python -m venv .venv
5. **Activate the Virtual Environment**:
   ```
   .venv\Scripts\activate
6. **Install Dependencies**: 
   ```
   pip install langchain
   pip install python-dotenv
   pip install langchain_experimental
   pip install open_ai
   pip install tabulate
   pip install langchain-openai
 7. **Run the application**:
    ```
    streamlit run main.py
