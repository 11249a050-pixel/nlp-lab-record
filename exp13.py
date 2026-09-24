import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = input('enter a sentence:')
tokens = word_tokenize(sentence)
tagged_words = pos_tag(tokens)
print("\npart-of-speech tagged sentence")
print("-" * 40)
for word, tag in tagged_words:
    print(f"{word:<15} {tag}")
