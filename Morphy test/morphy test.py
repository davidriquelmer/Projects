#Language detection
from morphy import Language
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
lang = Language(text=text)
print(lang)

#Sentence segmentation
from morphy import MultiLang
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
english_proc = MultiLang(lang='en')
doc = english_proc.parse_doc(text)
for sent in english_proc.extract_sentences(text):
    print(f"Sentence: {sent.text}")
    print("Tokens:")
    for token in sent.tokens:
        print(f" - {token.text} (Lemma: {token.lemma})")

#Lemmatization
from morphy import MultiLang
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
english_proc = MultiLang(lang='en')
doc = english_proc.parse_doc(text)
for token in doc:
    print(f"{token.text} --> {token.lemma_}")


#Lemmatization test 2
from morphy import MultiLang
text = "This is an example sentence. Here is another one."

# Initialize the MultiLang processor for English
multi_lang_processor = MultiLang(lang='en')

# Extract sentences
sentences = multi_lang_processor.extract_sentences(text)
print("Extracted Sentences:")
for sentence in sentences:
    print(f" - {sentence.text}")

# Extract tokens
tokens = multi_lang_processor.extract_tokens(text=text)
print("\nExtracted Tokens:")
for token in tokens:
    print(f" - {token.text} (Lemma: {token.lemma})")

# Extract noun phrases
noun_phrases = multi_lang_processor.extract_noun_phrases(text=text)
print("\nExtracted Noun Phrases:")
for phrase in noun_phrases:
    print(f" - {phrase.text}")

# Extract named entities
named_entities = multi_lang_processor.extract_named_entities(text=text)
print("\nExtracted Named Entities:")
for entity in named_entities:
    print(f" - {entity.text} (Type: {entity.tag})")