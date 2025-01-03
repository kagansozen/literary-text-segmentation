import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('punkt')

def clean_text(text):
    
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.UNICODE)
    text = text.lower()
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def clean_and_save(input_filename, output_filename):
    
    with open(input_filename, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = clean_text(text)

    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"Cleaned text saved to {output_filename}")

if __name__ == "__main__":
    input_file = 'input_text.txt'
    output_file = 'cleaned_text.txt'
    clean_and_save(input_file, output_file)
