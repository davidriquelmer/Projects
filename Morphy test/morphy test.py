#Language detection
from morphy import Language
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
lang = Language(text=text)
print(lang)

#Sentence segmentation
from morphy import MultiLang
text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
english_proc = MultiLang(lang='en')
doc = english_proc(text)
for sent in doc.sentences:
    print('%s\n%s' % (sent, '\n'.join(str(sent.tokens))))

# #Lemmatization
from morphy import MultiLang
# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry'
# english_proc = MultiLang(lang='en')
# doc = english_proc(text)
# for token in doc.tokens:
#     print('%s --> %s' % (token.text, token.lemma))
