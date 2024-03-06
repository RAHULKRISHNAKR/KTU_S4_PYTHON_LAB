def remove_special_chars(text):
  allowed_chars = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
  return "".join(char for char in text if char in allowed_chars)

def read_write_string(input_file, output_file):
  try:
    # Read the string from the input file
    with open(input_file, "r") as f:
      text = f.read()

    # Remove special characters
    clean_text = remove_special_chars(text)

    # Write the cleaned string to the output file
    with open(output_file, "w") as f:
      f.write(clean_text)

    print(f"String read from '{input_file}', special characters removed, and written to '{output_file}'.")
  except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")

# Get input and output file names from the user
input_file = input("Enter the path to the input file: ")
output_file = input("Enter the path to the output file: ")

# Read and write the string
read_write_string(input_file, output_file)
