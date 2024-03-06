def count_occurrences(text):
  counts = {
      "words": 0,
      "sentences": 0,
      "uppercase": 0,
      "lowercase": 0,
      "special": 0,
  }

  # Split text into words (considering punctuation as word separators)
  words = text.split()

  # Count words and sentences
  counts["words"] = len(words)
  counts["sentences"] = sum(1 for char in text if char in ".?!")

  # Count letters and special symbols
  for char in text:
    if char.isalpha():
      counts["uppercase" if char.isupper() else "lowercase"] += 1
    else:
      counts["special"] += 1

  return counts

def read_and_count(file_path):

  try:
    with open(file_path, "r") as f:
      text = f.read()

    counts = count_occurrences(text)

    print("** Text Analysis Results **")
    for category, count in counts.items():
      print(f"- {category.capitalize()}: {count}")

  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# Get the file path from the user
file_path = input("Enter the path to the text file: ")

# Read the file and count occurrences
read_and_count(file_path)
