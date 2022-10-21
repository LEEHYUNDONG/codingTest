import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    
    doc = nlp(sentences)
    txtLst = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            txtLst.append(ent.text)
            sentences = sentences.replace(ent.text, 'X'*len(ent.text), 1)
    

    return sentences
    


there is at least one '$' character between every two occurences of the same letter