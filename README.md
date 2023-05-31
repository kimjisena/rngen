# rngen

rngen is a Python project that converts a Committed Backlog document, extracted from a Google Doc in markdown format using the "Docs To Markdown" extension, into Release Notes. The resulting output is a markdown document that only includes the "Feature", "Description", and "Acceptance criteria" fields from the input document. This output document can be used as input to an AI model that will produce the release notes for each feature based on a "Release notes prompt".

## Installation

To use rngen, you need to have Python and pipenv installed on your system. Follow these steps to get started:

1. Clone the rngen repository from GitHub:

   ```bash
   git clone https://github.com/kimjisena/rngen.git
   ```

2. Navigate to the rngen directory:

   ```bash
   cd rngen
   ```

3. Install the required dependencies using pipenv:

   ```bash
   pipenv install
   ```

## Usage

```
usage: main.py [-h] -i INPUT -o OUTPUT

Process input files and generate output files.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the input directory
  -o OUTPUT, --output OUTPUT
                        Path to the output directory

```

1. Ensure that you have the Committed Backlog document in markdown format, extracted from a Google Doc using the "Docs To Markdown" extension. Save the document as `input.md` in the `inputs` directory (anywhere in your filesystem).

2. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

3. Run the `main.py` script to convert the Committed Backlog document to Release Notes:

    For instance:
   ```bash
   python src/main.py -i ./inputs -o ./outputs
   ```

4. After the script finishes executing, the Release Notes will be generated and saved as `output.md` in the `outputs` directory.

5. Use the generated `output.md` file as input to your AI model to produce the release notes for each feature based on a "Release notes prompt".

Note: You can modify the input document by replacing the content of `input.md` in the `inputs` directory with your own Committed Backlog document in markdown format.

## Release Notes AI Prompt
```
command: /release_notes_generetor

act: Release Notes Generator

prompt:
I want you to act as a Release Notes Generator. I will provide you with the following information: 

- Feature: [Brief description of the feature]
- Description: [Detailed description of the feature]
- Acceptance Criteria: [A list of specific criteria that the feature must meet]

I want you to generate release notes for the feature in the following format:

[Feature in titlecase]

    - [Acceptance criteria in two words]: [Brief description of acceptance criterion starting with "User can now..." or "We've..."]

Note: The feature has already been implemented and all acceptance criteria have been checked and they pass.
```
## Feedback

If you encounter any issues or have suggestions for improvement, please feel free to open an issue on the rngen GitHub repository. We welcome your feedback and contributions to make this project even better!