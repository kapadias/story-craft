import streamlit as st
from services.story_craft.service import generate_user_story

def run():
    st.title("StoryCraft")
    st.write(
        "Generate high-quality user stories based on user prompts and other information."
    )

    # Add an image/banner if you have one (optional)
    # st.image("path/to/your/image.png", use_column_width=True)

    with st.expander("Instructions", expanded=True):
        st.write(
            """
            1. Provide a **Persona** (the user role or type)
            2. Provide a **Scope** (the feature or functionality the user wants)
            3. Optionally, add a **Title** and **Acceptance Criteria** to further refine the user story
            4. Click the 'Generate User Story' button to generate the user story
            """
        )

    # Collect user inputs
    persona = st.text_input("Persona (Mandatory):", value="", help="Enter the user role or type.")
    scope = st.text_input("Scope (Mandatory):", value="", help="Enter the feature or functionality the user wants.")
    title = st.text_input("Title (Optional):", value="", help="Enter a title for the user story (optional).")
    acceptance_criteria = st.text_input("Acceptance Criteria (Optional):", value="", help="Enter the criteria for accepting the user story (optional).")

    # Generate the user story when the button is clicked
    if st.button("Generate User Story"):
        if not scope:
            st.warning("Please provide a scope to generate the user story.")
        else:
            story = generate_user_story(persona, scope, title, acceptance_criteria)
            st.success("User Story generated successfully!")
    else:
        st.write(
            "Provide the necessary input and click the 'Generate User Story' button."
        )

if __name__ == "__main__":
    run()
