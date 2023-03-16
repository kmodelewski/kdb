"""
Lists
"""
lista1 = ["element 1", 1, 2, "element 4"]
print(lista1[0])

# iterowanie listy
count = 0
for element in lista1:
    print(f" Element {count} listy: {element} \t")
    count = count + 1
# Dodanie do listy
lista1.append("element 5")  # lub lista1.insert(0, 0)
# zamiana elementu w liście
lista1[0] = "element pierwszy"
# usuwanie z indeksem
element_usuniety = lista1.pop(0)  # index,przydatne gdy usuwamy i chcemy miec usuniety element
print(f"element usuniety: {element_usuniety}")
# usuwanie ze wskazaniem wartosci
lista1.remove('element 4')  # remove usuwa tylko pierwszy element o takiej nazwie, jeśli chcemy wiecej
# to musimy uzyc petli
# sortowanie listy - elementy muszą być tego samego typu
# lista1.sort()

# print types in list
for element in lista1:
    if type(element) is str:
        print(f" {element} is String")
    elif type(element) is int:
        print("Integer")
    else:
        None

# Make list from range
numbered_list: list = list(range(1, 9999))

# List comprehension
# define function than for loop to feed this function
squares: list[int] = [value ** 2 for value in range(1, 11)]
print(squares)

# Copy a list
new_squares: list[int] = squares[:]  # copy of the list squares
new_squares = squares  # zmiana elementu w jednej liście powoduje zmianę w drugiej

# Check if element is in the list

users: list[str] = ["krzys", "jacek"]

user = 'krzys1'
if user not in users:
    print(f" user: {user} is not in the list")
else:
    print(f" user {user} is in the list")

# BOOLEAN EXPRESSIONS - sprawdzenie czy lista jest pusta
skladniki = []

if skladniki:
    print("lista nie jest pusta")

else:
    print("lista jest pusta")