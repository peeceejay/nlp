## This program uses the spaCy library to parse 5 user-defined sentences, and perform tokenisation and entity recognition.

import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["The sour drink from the Atlantic Ocean", "Elon Musk painted the wall with cracks", "Rosamund Kwan told the story cried", 
    "Mother Theresa convinced Queen Bee children are noisy", "The Winne the Pooh dog that I had really loved bones"]

for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print()
    print([(token, token.orth_, token.orth) for token in nlp(sentence)])
    print()
    print([(i, i.label_, i.label) for i in nlp_sentence.ents])


## Comment about 2 unsual entities:
# 1. 'Mother Theresa' is recognised as an organisation rather than a person.
# 2. 'Winnie the Pooh' was not recognised as a single entity phrase and 'Winnie' was recognised as a person rather than a famous cartoon character.