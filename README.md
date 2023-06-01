# rngen

rngen is a Python project that converts a Committed Backlog document, extracted from a Google Doc in markdown format using the "Docs To Markdown" extension, into Release Notes.

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

4. Copy `.env.example` to `.env` and add your OpenAI API key

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

1. Ensure that you have the Committed Backlog document in markdown format, extracted from a Google Doc using the "Docs To Markdown" extension. Save the document(s) anywhere in your filesystem.

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

Note: You can modify the input document by replacing the content of `input.md` in the `inputs` directory with your own Committed Backlog document in markdown format.

## Feedback

If you encounter any issues or have suggestions for improvement, please feel free to open an issue on the rngen GitHub repository. We welcome your feedback and contributions to make this project even better!

## TODO
- Add support for other input/output formats such as `docx` and `pdf`