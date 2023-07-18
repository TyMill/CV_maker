# CV Generator

This is a simple Python script that generates a CV in Markdown format.

## Usage

1. Clone this repository or download the `main.py` file.
2. Open `main.py` in a text editor.
3. Replace the placeholder text in the `main` function with your actual CV details.
4. Save and close the file.
5. Run the script with the command `python main.py` in your terminal.
6. The script will create a file named `CV.md` in the same directory with your generated CV.

## Customization

You can customize this script to fit your needs. Each section of the CV is generated by a separate Python class:

- `ContactInfo` for your contact information
- `Summary` for your professional summary
- `Experience` for your work experience
- `Skills` for your skills
- `Education` for your education

You can add, remove, or modify these classes as needed. The `generate_markdown` function takes a dictionary with instances of these classes and generates the CV. If you modify the classes, you will also need to modify this function to match.

## License

This project is licensed under the terms of the MIT license.
