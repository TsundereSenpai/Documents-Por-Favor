def Judgment(arg, person):
    if (arg == 'accept' or arg == 'a') and (person.tag == 'people'):
        return True
    if (arg == 'reject' or arg == 'r') and (person.tag != 'people'):
        return True
    if (arg == 'accept' or arg == 'a') and (person.tag != 'people'):
        return False
    if (arg == 'reject' or arg == 'r') and (person.tag == 'people'):
        return False
    else:
        return None
