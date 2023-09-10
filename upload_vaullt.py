def convert_to_python_dict(filename='config.txt'):
    # Read the contents of the file
    with open(filename, 'r') as f:
        contents = f.read()

    # Replace JavaScript object syntax to Python dictionary syntax
    contents = contents.replace('{', '{\n')
    contents = contents.replace('}', '\n}')
    contents = contents.replace(':', ': ')
    contents = contents.replace(',', ',\n')

    # Remove const declaration and unnecessary characters
    lines = contents.splitlines()
    lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('const')]

    # Create the final dictionary string
    python_dict_str = '\n'.join(lines)

    # Save the Python dictionary back to the file
    with open(filename, 'w') as f:
        f.write(python_dict_str)

    print(f"Converted JS object to Python dictionary in {filename}")

# Call the function
convert_to_python_dict()
