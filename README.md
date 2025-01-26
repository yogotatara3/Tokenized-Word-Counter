# Tokenized-Word-Counter

## Overview
This script processes a folder of `.txt` files to count and analyze word occurrences, with optional tokenization using a T5 model (`google/t5-v1_1-small`). It saves the sorted word counts into a file named `tokenizer_word_counts.txt` for further use, such as training or analysis.

---

## Features
- **Folder Processing**: Scans all `.txt` files in a specified folder.
- **Word Count**: Counts words with at least 3 characters.
- **Sorting**: Outputs words sorted by frequency in descending order.
- **Tokenization Integration**: Includes optional debugging to tokenize words using a T5 model.
- **Dynamic Input**: Allows specifying the folder path via a command-line argument.
- **Output**: Saves results to a text file (`tokenizer_word_counts.txt`).

---

## Requirements
1. Python 3.7 or newer.
2. Required packages:
   - `transformers`
   - `re`
3. **Hugging Face Token**:
   - Ensure that you have a valid Hugging Face token set up.
   - Login to Hugging Face CLI:
     ```bash
     huggingface-cli login
     ```
4. **Download the T5 Model**:
   - The script automatically downloads the `google/t5-v1_1-small` model if not already available.

Install missing dependencies using:
```bash
pip install transformers
```

---

## Usage
1. **Run the script**:
   ```bash
   python script_name.py -p "path/to/your/folder"
   ```
   Replace `path/to/your/folder` with the absolute path to the folder containing `.txt` files.

3. **Output**:
   - A file named `tokenizer_word_counts.txt` containing words and their frequencies, sorted by count.

---

## Script Details
- **Input**:
  - Folder containing `.txt` files.
- **Processing**:
  - Reads text files, converts content to lowercase, and extracts words with at least 3 characters.
  - (Optional) Tokenizes words using the `google/t5-v1_1-small` model for debugging purposes.
- **Output**:
  - A sorted list of words and their counts in `tokenizer_word_counts.txt`.

---

## Example Output
Content of `tokenizer_word_counts.txt`:
```
word1 123
word2 98
word3 45
...
```

---

## Notes
- Ensure that the folder path provided contains `.txt` files.
- Use the `-p` flag to specify a custom folder path.
- Debugging outputs can be removed or commented out for production use.

---

## Troubleshooting
1. **Missing Dependencies**:
   - Ensure `transformers` is installed (`pip install transformers`).
2. **File Encoding Issues**:
   - The script assumes UTF-8 encoding for `.txt` files.
3. **Hugging Face Token**:
   - Login with `huggingface-cli login` before running the script.
4. **Model Download Issues**:
   - Ensure the environment can download the `google/t5-v1_1-small` model from Hugging Face.
5. **Tokenizer Errors**:
   - Errors during tokenization are logged for debugging and do not interrupt execution.

