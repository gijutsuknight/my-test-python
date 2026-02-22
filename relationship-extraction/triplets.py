"""Parse REBEL model output into (head, type, tail) triplets."""


def extract_triplets(text: str) -> list[dict]:
    """Parse REBEL generated text (with <triplet>, <subj>, <obj> tokens) into triplets."""
    triplets = []
    relation, subject, object_ = "", "", ""
    text = text.strip()
    current = "x"
    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").split():
        if token == "<triplet>":
            current = "t"
            if relation != "":
                triplets.append({"head": subject.strip(), "type": relation.strip(), "tail": object_.strip()})
                relation = ""
            subject = ""
        elif token == "<subj>":
            current = "s"
            if relation != "":
                triplets.append({"head": subject.strip(), "type": relation.strip(), "tail": object_.strip()})
            object_ = ""
        elif token == "<obj>":
            current = "o"
            relation = ""
        else:
            if current == "t":
                subject += " " + token
            elif current == "s":
                object_ += " " + token
            elif current == "o":
                relation += " " + token
    if subject != "" and relation != "" and object_ != "":
        triplets.append({"head": subject.strip(), "type": relation.strip(), "tail": object_.strip()})
    return triplets
