from posixpath import sep


string = '01234567890123456789012345678901234567890123456789'

def funcao(param):
    sep_str = [param[index:index + 10] for index in range(0, len(param), 10)]
    print(sep_str)
    return '.'.join(sep_str)

print(funcao(string))