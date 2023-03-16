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