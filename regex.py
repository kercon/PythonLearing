import re


def phonesearch(text):
    phoneregex = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
    mo = phoneregex.search(text)
    return mo


def regexrsearch(searchtext, regexr, mod='first'):
    compiled = re.compile(regexr)
    if mod in ['first', 'all']:
        if mod == 'first':
            foundchunks = compiled.search(searchtext)
            return foundchunks
        if mod == 'all':
            foundchunks = compiled.findall(searchtext)
            return foundchunks
    else:
        print('incorrect mod')
        return foundchunks
    return foundchunks
