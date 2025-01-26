import os
import re
from collections import Counter
from transformers import T5Tokenizer
import argparse

# Initialize T5 tokenizer
tokenizer = T5Tokenizer.from_pretrained("google/t5-v1_1-small")

# Step 1: Crawling folder and calculating word counts
def calculate_word_counts(folder_path):
    word_counter = Counter()

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Process only .txt files
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Convert text to lowercase
                    words = [word for word in re.findall(r'\b\w+\b', text) if len(word) >= 3]  # Extract words with at least 3 characters

                    # Debugging: Print words before filtering
                    print(f"Words before filtering in {filename}: {words}")

                    # Disable tokenizer filtering temporarily
                    # words = [word for word in words if len(tokenizer(word, return_tensors=\"pt\").input_ids[0]) == 1]

                    # Debugging: Print tokenizer output (optional)
                    for word in words:
                        try:
                            tokenized = tokenizer(word, return_tensors="pt").input_ids
                            print(f"Word: {word}, Tokenized: {tokenized}")
                        except Exception as e:
                            print(f"Tokenizer error for word '{word}': {e}")

                    word_counter.update(words)  # Update the counter with words
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # Sort words by count (highest to lowest)
    sorted_word_counts = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)

    # Save sorted word counts to a file
    with open("tokenizer_word_counts.txt", "w", encoding="utf-8") as output_file:
        for word, count in sorted_word_counts:
            output_file.write(f"{word} {count}\n")

    return dict(sorted_word_counts)  # Return sorted dictionary

# Example Usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process folder path')
    parser.add_argument('-p', '--path', type=str, required=True, 
                        help='Path to the folder')
    args = parser.parse_args()

    folder_path = args.path
    
    # Step 1: Calculate word counts
    word_counts = calculate_word_counts(folder_path)
    print("Word Counts saved to 'tokenizer_word_counts.txt'")
