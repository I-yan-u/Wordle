""" module that checks eligibility of words """
# wlen = word lenght
# inst = instance i.e is string
# real = real word i.e in dictionary
# wstring = input string by user



def wlen(wstring):
    """ Checks for lenght of string"""
    if len(wstring) != 5:
        return False
    else:
        return True


def inst(wstring):
    """ Check for arg instance """
    if type(wstring) == 'str':
        return True
    else:
        return False


def real(wstring):
    """ Check if word is a real word """
    with open("sgb-words.txt", "r") as lib:
        for wds in lib:
            if wstring == wds.strip():
                return True
        return False
