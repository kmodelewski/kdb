alien = {'color': 'black', 'age': 30}

print(alien['color'].title())
alien.get('age')

#looping
for key, value in alien.items():
    print(key, value)

print(alien.keys())

#ZIP TWO LISTS
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)

# LIST IN DICTIONARY

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("--------Piza toppings--------")
for topping in pizza['toppings']:
    print(f"\t {topping}")

print(*pizza['toppings']) #wypisze liste po spacji

