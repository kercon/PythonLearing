import re


def phonesearch(text):
    phoneregex = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
    mo = phoneregex.search(text)
    return mo
