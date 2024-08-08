def recLength(string):
    if string == '':
        return 0
    else:
        return 1 + recLength(string[1:])
    
r = recLength("impossível")
print(r)