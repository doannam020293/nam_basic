import unidecode


def remove_accent(string):
    return unidecode.unidecode(string)