import os
import argparse
import ai

def process_files(input_dir, output_dir):
    # Ensure that the input and output directories exist
    if not os.path.isdir(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return

    if not os.path.isdir(output_dir):
        print(f"Output directory '{output_dir}' does not exist.")
        return

    # Loop through the files in the input directory
    for filename in os.listdir(input_dir):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename)

        process_sections(input_file, output_file)
        print(f"Extraction done.\nCheck the output file: {output_file}")

    print("File processing completed.")

def process_sections(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    sections = content.split('\n\n')[2:]
    output_md = ''

    for section in sections:
        print("Using text-davinci-003 to generate release note...")
        release_note = ai.get_release_note(section)
        output_md += release_note
        output_md += '\n---\n\n'

    with open(output_file, 'w') as file:
        print("Writing release notes to output file...")
        file.write(output_md)
    return sections


def main():
    parser = argparse.ArgumentParser(description="Process input files and generate output files.")
    parser.add_argument("-i", "--input", help="Path to the input directory", required=True)
    parser.add_argument("-o", "--output", help="Path to the output directory", required=True)
    args = parser.parse_args()

    input_directory = args.input
    output_directory = args.output

    process_files(input_directory, output_directory)

if __name__ == "__main__":
    main()
