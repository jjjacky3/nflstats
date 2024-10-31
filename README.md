# NFLStats

NFLStats is a powerful tool that allows you to query structured NFL data using natural language. Built with LangChain and powered by OpenAI's LLM, it features a user-friendly interface developed using the Streamlit library.

I’ve deployed the NFLStats app on the free to use [Streamlit Community Cloud](https://streamlit.io/cloud) with [2024 play by play data](https://github.com/nflverse/nflverse-data/releases/tag/pbp). You can try it out here: [NFLStats](https://nflstats-jacky.streamlit.app/)

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
