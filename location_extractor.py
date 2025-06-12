import spacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_trf")

def extract_locations(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ("GPE", "LOC")]
    return locations


