from bs4 import BeautifulSoup
import os
import argparse


def convert_to_bullet_list(element):
    markdown_string = str(element)
    # Remove leading/trailing whitespace and HTML tags
    markdown_string = markdown_string.strip()
    markdown_string = markdown_string.replace('<td>', '')
    markdown_string = markdown_string.replace('</td>', '')
    markdown_string = markdown_string.replace('<ul>', '')
    markdown_string = markdown_string.replace('</ul>', '')
    markdown_string = markdown_string.replace('<li>', '')
    markdown_string = markdown_string.replace('</li>', '')
    # Split the string into individual list items
    list_items = markdown_string.split('\n')

    # Generate the bullet list
    bullet_list = ''
    for item in list_items:
        # Remove any leading/trailing whitespace
        item = item.strip()

        # Skip empty items
        if not item:
            continue

        # Add a bullet point and indentation to each item
        bullet_list += f'- {item}\n'

    return bullet_list

def extract_tables(markdown_file, output_file):
    print("STEP 1: Opening input file...")
    with open(markdown_file, 'r') as file:
        markdown_data = file.read()

    # Parse the markdown file
    print("STEP 2: Parsing input file...")
    soup = BeautifulSoup(markdown_data, 'html.parser')

    # Find all tables in the markdown file
    tables = soup.find_all('table')

    extracted_data = []
    print("STEP 3: Extracting tables..")
    for table in tables:
        # Find all table rows
        rows = table.find_all('tr')

        # Initialize variables
        feature = ''
        description = ''
        acceptance_criteria = ''

        # Extract the data based on row content
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                key = cells[0].text.strip()
                value = cells[1]

                if key == 'Feature':
                    feature = value.text.strip()
                    print(f"\tFeature: {value.text.strip()}")
                elif key == 'Description':
                    description = value.text.strip()
                elif key == 'Acceptance criteria (assertions)':
                    acceptance_criteria = convert_to_bullet_list(value)

        # Append extracted data to the list
        extracted_data.append((feature, description, acceptance_criteria))

    # Generate the new markdown file with extracted data
    output_md = ''
    print("STEP 4: Writing to output file...")
    for data in extracted_data:
        feature, description, acceptance_criteria = data
        output_md += f'**Feature**: {feature}\n\n'
        output_md += f'**Description**: {description}\n\n'
        output_md += '**Acceptance criteria**:\n\n'
        output_md += acceptance_criteria
        output_md += '\n\n---\n\n'

    # Save the extracted data to the output markdown file
    with open(output_file, 'w') as file:
        file.write(output_md)

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

        # Call the second function to process the file
        extract_tables(input_file, output_file)
        print(f"Extraction done.\nCheck the output file: {output_file}")

    print("File processing completed.")

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
