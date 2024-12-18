from nltk.corpus import wordnet as wn

# Example: Lemmatize a word using Morphy
word = "running"
lemma = wn.morphy(word)

if lemma:
    print(f"The lemma for '{word}' is '{lemma}'.")
else:
    print(f"No lemma found for '{word}'.")