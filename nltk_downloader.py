import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging

logging.basicConfig(level=logging.INFO)

def download_nltk_resources():
    """
    Download the required NLTK resources: wordnet, punkt, and stopwords.
    """
    resources = ['wordnet', 'punkt', 'stopwords']
    for resource in resources:
        try:
            nltk.download(resource)
            logging.info(f"NLTK resource '{resource}' downloaded successfully.")
        except Exception as e:
            logging.error(f"Error downloading NLTK resource '{resource}': {e}")

def get_synonyms(word):
    """
    Get synonyms for a given word using WordNet.

    Parameters:
    word (str): The word to find synonyms for.

    Returns:
    list: A list of synonyms.
    """
    synonyms = set()
    try:
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
    except Exception as e:
        logging.error(f"Error getting synonyms for word '{word}': {e}")
    return list(synonyms)

def tokenize_text(text):
    """
    Tokenize the input text into words.

    Parameters:
    text (str): The text to tokenize.

    Returns:
    list: A list of tokens.
    """
    try:
        return word_tokenize(text)
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
        return [token for token in tokens if token.lower() not in stop_words]
    except Exception as e:
        logging.error(f"Error removing stopwords: {e}")
        return []

def text_preprocessing(text):
    """
    Perform a full text preprocessing pipeline including tokenization and stopword removal.

    Parameters:
    text (str): The text to preprocess.

    Returns:
    list: A list of cleaned tokens.
    """
    tokens = tokenize_text(text)
    return remove_stopwords(tokens)

if __name__ == "__main__":
    # Example usage
    download_nltk_resources()
    
    example_text = "This is a simple example sentence for testing NLTK functionalities."
    cleaned_tokens = text_preprocessing(example_text)
    logging.info(f"Cleaned Tokens: {cleaned_tokens}")
    
    example_word = "simple"
    synonyms = get_synonyms(example_word)
    logging.info(f"Synonyms for '{example_word}': {synonyms}")