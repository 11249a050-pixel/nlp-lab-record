import nltk
from nltk import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = input('enter a sentence:')
tokens = word_tokenize(text)
tags = pos_tag(tokens)
print("\nPOS Tags using viterbi decoding concept")
print("-" * 45)
for word, tag in tags:
    print(f"{word:<15} {tag}")
    