import re
from string import punctuation


def preprocess(text: str) -> str:
    prep_text = re.sub(r"\(#[+-]?[0-9]*[.]?[0-9]*\)", '', text)
    for punc in punctuation:
        prep_text = prep_text.replace(punc, '')

    return prep_text.strip().lower()

