def greeting(name: str) -> str:
    return

suma: int = 0
lista : list[int] = []
for value in range(1,9):
    lista.append(value)
    suma = suma + value
print(sum(lista))
print(f"suma = {suma}")

#type checking
isinstance(suma, int)
if type(suma) is int:
    print(suma)

#type checking swith case

x = 'a'
#https://stackoverflow.com/questions/66159432/how-to-use-values-stored-in-variables-as-case-patterns
match x:
    case isinstance(x, int): "integer"
    case isinstance(x,str): "string"
    case  _: print("other type")
