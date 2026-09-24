import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input sentence
text = input("Enter a sentence: ")

# Tokenize words
words = word_tokenize(text)

# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Display heading
print("\nMorphological Analysis")
print("-" * 60)
print("{:<15} {:<15} {:<15}".format("Original", "Stemmed", "Lemmatized"))
print("-" * 60)

# Process each word
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print("{:<15} {:<15} {:<15}".format(word, stem, lemma))
