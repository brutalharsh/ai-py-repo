import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging

def download_nltk_resources():
    """
    Download the required NLTK resources: wordnet, punkt, and stopwords.
    """
    try:
        nltk.download('wordnet')
        nltk.download('punkt')
        nltk.download('stopwords')
        print("All NLTK resources downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading NLTK resources: {e}")

def get_synonyms(word):
    """
    Get synonyms for a given word using WordNet.

    Parameters:
    word (str): The word to find synonyms for.

    Returns:
    list: A list of synonyms.
    """
    try:
        synonyms = []
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        return list(set(synonyms))
    except Exception as e:
        logging.error(f"Error getting synonyms for word '{word}': {e}")
        return []

def tokenize_text(text):
    """
    Tokenize the input text into words.

    Parameters:
    text (str): The text to tokenize.

    Returns:
    list: A list of tokens.
    """
    try:
        tokens = word_tokenize(text)
        return tokens
    except Exception as e:
        logging.error(f"Error tokenizing text: {e}")
        return []

def remove_stopwords(tokens):
    """
    Remove stopwords from a list of tokens.

    Parameters:
    tokens (list): A list of tokens.

    Returns:
    list: A list of tokens with stopwords removed.
    """
    try:
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        return filtered_tokens
    except Exception as e:
        logging.error(f"Error removing stopwords: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    download_nltk_resources()
    
    example_text = "This is a simple example sentence for testing NLTK functionalities."
    tokens = tokenize_text(example_text)
    print("Tokens:", tokens)
    
    filtered_tokens = remove_stopwords(tokens)
    print("Filtered Tokens:", filtered_tokens)
    
    example_word = "simple"
    synonyms = get_synonyms(example_word)
    print(f"Synonyms for '{example_word}':", synonyms)