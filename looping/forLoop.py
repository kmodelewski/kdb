'''
RANGE FUNCTION

for element in range(10):
    print(element, end=' ')  # end=' ' - oznacza oddzielenie spacją, można też wstawić separator sep=','
'''
def addListElements(lista: list) -> int:
    suma = 0
    for liczba in lista:
            suma += liczba
    return suma

print(addListElements([1,2,3,4]))


