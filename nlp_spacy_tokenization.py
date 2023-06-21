import spacy

nlp = spacy.load('C:\\Users\\SDUPPALL\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\en_core_web_sm\\en_core_web_sm-3.5.0')
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
for token in doc:
    print(token.text, token.pos)
