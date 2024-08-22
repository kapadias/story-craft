import streamlit as st
import openai

# Ensure the OpenAI API key is securely accessed from environment variables
openai.api_key = st.secrets["OPENAI_API_KEY"]


def generate_user_story(
    persona: str, scope: str, title: str, acceptance_criteria: str
) -> None:
    """
    Generates a user story using the GPT-4 model based on the provided persona, scope, title, and acceptance criteria.
    The generated user story is displayed in a chat-based format using Streamlit.

    Args:
        persona (str): The user persona.
        scope (str): The scope of the user story.
        title (str): The title of the user story.
        acceptance_criteria (str): The acceptance criteria of the user story.

    Returns:
        None
    """

    # Define the chat-based input prompt for the OpenAI API
    messages = [
        {
            "role": "system",
            "content": "You are an experienced product owner with experience that generates clear and relevant user stories based on the provided information for machine learning domain.",
        },
        {
            "role": "user",
            "content": (
                f"Generate a detailed user story including Title, Description, "
                f"and Acceptance Criteria using the following information:\n"
                f"Persona: {persona}\n"
                f"Scope: {scope}\n"
                f"Title: {title}\n"
                f"Acceptance Criteria: {acceptance_criteria}"
            ),
        },
    ]

    st.markdown("----")
    res_box = st.empty()
    report = []

    # Call the OpenAI API to generate the user story using the GPT-4 model
    for response in openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        stream=True,
        temperature=0.5,  # Slightly increased to allow more creative output
        presence_penalty=0.0,  # Neutral presence_penalty to avoid redundancy
    ):
        # Check if the content is in the response and update the output
        if "content" in response.choices[0].delta:
            report.append(response.choices[0].delta.content)
            result = "".join(report).strip()
            res_box.markdown(f"*{result}*")
