import os
import streamlit as st

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI

def main():
    st.set_page_config(page_title="Ask NFL Stats", layout="wide")

    agent = create_csv_agent(
            ChatOpenAI(temperature=0, model="gpt-4o", max_tokens=1000),
            "play_by_play_2024.csv",
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            allow_dangerous_code=True
        )

    col1, col2 = st.columns(2, vertical_alignment="top", gap="large")

    with col1:
        st.header("Play by play 📊")

        user_question = st.text_input("Ask your question:")
        if user_question is not None and user_question !="":
            response = agent.invoke(user_question)
            st.write(response['output'])

    with col2:
        st.header("Sample questions")

        st.subheader("How many rows are there in the dataset?", divider=True)
        st.subheader("How many passing yards gained by SEA in the game vs SF?", divider=True)
        st.subheader("Who is Seahawk's quarter back?", divider=True)
        st.subheader("Who in Seahawk has the most penalty by yards?", divider=True)
        st.subheader("Who in Seahawk has the most rushing yards so far in 2024?", divider=True)


if __name__ == "__main__":
    main()