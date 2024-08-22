import streamlit as st
from services.story_craft.service import generate_user_story


class StoryCraftApp:
    def __init__(self):
        """
        Initialize the StoryCraftApp with default values for user inputs.
        """
        self.persona = ""
        self.scope = ""
        self.title = ""
        self.acceptance_criteria = ""

    def display_title(self):
        """
        Display the app's title and description.
        """
        st.title("📝 StoryCraft: User Story Generator")
        st.write(
            "Generate high-quality **user stories** based on user prompts and other information."
        )

    def display_instructions(self):
        """
        Display the instructions for using the app within an expandable section.
        """
        with st.expander("📋 Instructions", expanded=True):
            st.markdown(
                """
                **Follow these steps to generate a user story:**
                1. Provide a **Persona** (the user role or type).
                2. Provide a **Scope** (the feature or functionality the user wants).
                3. Optionally, add a **Title** and **Acceptance Criteria** to refine the user story.
                4. Click the **'Generate User Story'** button to generate the user story.
                """
            )

    def collect_user_inputs(self):
        """
        Collect user inputs for persona, scope, title, and acceptance criteria.
        """
        self.persona = st.text_input(
            "👤 Persona (Mandatory):", value="", help="Enter the user role or type."
        )
        self.scope = st.text_input(
            "📋 Scope (Mandatory):",
            value="",
            help="Enter the feature or functionality the user wants.",
        )
        self.title = st.text_input(
            "🏷️ Title (Optional):",
            value="",
            help="Enter a title for the user story (optional).",
        )
        self.acceptance_criteria = st.text_input(
            "✅ Acceptance Criteria (Optional):",
            value="",
            help="Enter the criteria for accepting the user story (optional).",
        )

    def generate_story(self):
        """
        Generate and display the user story based on the provided inputs.
        """
        if not self.scope:
            st.warning("⚠️ Please provide a scope to generate the user story.")
        else:
            story = generate_user_story(
                self.persona, self.scope, self.title, self.acceptance_criteria
            )
            st.success("🎉 User Story generated successfully!")
            st.write(story)

    def run(self):
        """
        Run the Streamlit app by displaying the title, instructions, input fields, and handling story generation.
        """
        self.display_title()
        self.display_instructions()
        self.collect_user_inputs()

        # Generate the user story when the button is clicked
        if st.button("🚀 Generate User Story"):
            self.generate_story()
        else:
            st.info(
                "ℹ️ Provide the necessary input and click the **'Generate User Story'** button."
            )


if __name__ == "__main__":
    # Create an instance of the StoryCraftApp and run the app
    app = StoryCraftApp()
    app.run()
