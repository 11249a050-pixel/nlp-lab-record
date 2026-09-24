import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download("averaged_perceptron_tagger_eng")
sentence = input("enter a sentence:")
words = word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print("\nword\t\tPOS Tag")
print("-" * 30)
for word, tag in pos_tags:
    print(f"{word}\t\t{tag}")