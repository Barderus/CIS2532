import spacy
from pathlib import Path
nlp = spacy.load("en_core_web_sm")

# Create a spaCy document to process
document = nlp("In 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C), devoted to developing web technologies")

# getting the named entities
for entity in document.ents:
    print(entity.text, entity.label_)
# Output:
# 1994 DATE
# Tim Berners-Lee PERSON
# the World Wide Web Consortium ORG

# Similiarity Detection with spaCy
# Analyze documents to determine how alike they are.

# Load the language model
document1 = nlp(Path(r"Week 7\RomeoJuliet.txt").read_text())
document2 = nlp(Path(r"Week 7\EdwardTheSecond.txt").read_text())
                
# Compare the two documents
print(document1.similarity(document2))