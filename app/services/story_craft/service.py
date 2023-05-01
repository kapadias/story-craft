import streamlit as st
import openai
import os

# Replace with your OpenAI API key, or set it as an environment variable in your deployment settings
openai.api_key = st.secrets["OPENAI_API_KEY"]


def generate_user_story(
    persona: str, scope: str, title: str, acceptance_criteria: str
) -> None:
    """
    The function constructs a chat-based input prompt for the OpenAI API with the given persona, scope, title, and
    acceptance criteria. It then calls the OpenAI API to generate the user story using GPT-3's Davinci engine.
    The generated user story is displayed in a chat-based format using Streamlit.

    Args:
        persona (str): A string representing the user persona.
        scope (str): A string representing the scope of the user story.
        title (str): A string representing the title of the user story.
        acceptance_criteria (str): A string representing the acceptance criteria of the user story.

    Returns:
        None
    """

    # Construct the chat messages for the API prompt
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that generates user stories based on the given information",
        },
        {
            "role": "user",
            "content": f"Generate the user story with the Title, Description and Acceptance Criteria using the following information \n "
            f"scope: As a {persona}, I want to {scope}, sample title:{title}, sample acceptance criteria: {acceptance_criteria}. ",
        },
    ]

    st.markdown("----")
    res_box = st.empty()
    report = []

    # Call the OpenAI API to generate the user story in a chat-based format
    for resp in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using GPT-3's Davinci engine
        messages=messages,
        stream=True,
        temperature=0.2,
        presence_penalty=-1.5,
    ):
        # join method to concatenate the elements of the list
        # into a single string,
        # then strip out any empty strings
        if "content" in resp.choices[0].delta:
            report.append(resp.choices[0].delta.content)
            result = "".join(report).strip()
            # result = result.replace("\n", "")
            res_box.markdown(f"*{result}*")
