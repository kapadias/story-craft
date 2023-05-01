import streamlit as st
from services.story_craft.service import generate_user_story

def run():
    st.title("StoryCraft")

    st.write(
        "Generate high-quality user stories based on user prompts and other information."
    )

    # Collect user inputs
    persona = st.text_input("Persona (Mandatory):", "")
    scope = st.text_input("Scope (Mandatory):", "")
    title = st.text_input("Title (Optional):", "")
    acceptance_criteria = st.text_input("Acceptance Criteria (Optional):", "")

    # Generate the user story when the button is clicked
    if st.button("Generate User Story"):
        if not scope:
            st.warning("Please provide a scope to generate the user story.")
        else:
            generate_user_story(persona, scope, title, acceptance_criteria)
    else:
        st.write(
            "Provide the necessary input and click the 'Generate User Story' button."
        )


if __name__ == "__main__":
    run()
