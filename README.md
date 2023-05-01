# StoryCraft - Professional User Story Generator

StoryCraft is a sophisticated web application designed to generate high-quality user stories based on user prompts and 
additional input. Utilizing OpenAI's GPT-3.5 language model, StoryCraft presents user stories in an 
interactive chat-based format.

Endpoint: [StoryCraft App](https://cr-personal-streamlit-na-story-craft-5n6fqn7d2a-ue.a.run.app)

## Getting Started

To begin using the StoryCraft application, follow the steps outlined below:

1. Clone the repository to your local machine.
2. Install [Poetry](https://python-poetry.org/docs/#installation) on your local machine if not already present.
3. Navigate to the root directory of the project and execute `poetry install` to install the required dependencies.
4. Set your OpenAI API key as a streamlit secret with the name `OPENAI_API_KEY`.
5. Run `poetry run streamlit run ./app/main.py` to initiate the application.
6. Access the application by opening the URL displayed in the console.

## Usage

StoryCraft features an intuitive user interface for the seamless generation of user stories. Follow these steps to utilize the application:

1. Input the persona, representing the user or customer for the user story (mandatory field).
2. Input the scope, describing the goal or objective of the user story (mandatory field).
3. (Optional) Input the title of the user story.
4. (Optional) Input the acceptance criteria, outlining the conditions required for the user story to be considered complete.
5. Click the "Generate User Story" button to produce the user story. The generated user story will appear in a chat-based format.

## Dependencies

StoryCraft employs [Poetry](https://python-poetry.org/) for dependency management. 
The following packages are necessary to run the application:

- python = "3.9.16"
- streamlit = "^1.22.0"
- openai = "^0.27.5"

Access to OpenAI's language model requires an API key.

## Credits and Licensing

Developed by Shashank Kapadia, StoryCraft is released under the [MIT License](https://opensource.org/licenses/MIT). 
The application utilizes OpenAI's language model, subject to OpenAI's terms of service.

## Code Attribution

If you plan to use any portion of the StoryCraft source code in your own projects, please provide proper attribution by including the following in your documentation or source code:
````json
{
  "Project": "StoryCraft - Professional User Story Generator",
  "Developer": "Shashank Kapadia",
  "Source": "https://github.com/kapadias/story-craft",
  "License": "MIT License"
}
````
