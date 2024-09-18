from transformers import pipeline

def translate_file(input_file_path, output_file_path):
    # Define the maximum length for chunks of text
    max_chunk_length = 500  # Reduce chunk size if necessary

    # Load the translation model with a higher max_length setting
    translator = pipeline('translation_en_to_uk', model='Helsinki-NLP/opus-mt-en-uk', max_length=1024)

    # Initialize an empty list to store translated text
    translated_text = []

    # Read the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Split text into manageable parts if necessary
        parts = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]

        # Translate each part
        for part in parts:
            result = translator(part)
            translated_text.append(result[0]['translation_text'])

    # Write the translated text to an output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(translated_text))

# File paths
input_file = 'cc.txt'
output_file = 'translated_cc.txt'

# Call the translation function
translate_file(input_file, output_file)
print("Translation completed. Check the translated text in 'translated_cc.txt'.")

