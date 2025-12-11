# Text Processing Assignment - Starter Code
# Choose one or more tasks to complete

# Task 1: Text Analysis Tool
# ============================
def analyze_text(filename):
    """
    Analyze text from a file and display statistics.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # TODO: Implement text analysis
        # - Count words, sentences, unique words
        # - Calculate average word length
        # - Find top 10 most frequent words
        # - Display results

        pass
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Task 2: Text Transformation Tool
# ==================================
def transform_text(input_file, output_file):
    """
    Read text from input file and apply transformations.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # TODO: Implement text transformation
        # - Display menu of transformation options
        # - Apply selected transformation
        # - Save to output file
        # - Display confirmation

        pass
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


# Task 3: Text Search and Replace
# =================================
def search_and_replace(input_file, output_file):
    """
    Search for text patterns and replace them.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # TODO: Implement search and replace
        # - Prompt user for search term and replacement
        # - Replace all occurrences
        # - Save to output file
        # - Display replacement count

        pass
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


# Main Menu
# =========
if __name__ == "__main__":
    print("📝 Python Text Processing Tool")
    print("=" * 40)
    print("1. Text Analysis")
    print("2. Text Transformation")
    print("3. Search and Replace")
    print("=" * 40)

    # TODO: Implement menu selection and call appropriate functions
