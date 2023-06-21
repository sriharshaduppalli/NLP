import spacy

nlp = spacy.load('en_core_web_sm-3.5.0')
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
for token in doc:
    print(token.text, token.pos)
