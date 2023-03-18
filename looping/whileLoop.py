prompt = "\nAdd a new node, write quit to exit \t"

message = ""
while message !='quit':
    message = input(prompt)
    if message != 'quit': #quit word not printed
        print(message)

#FLAG
active: bool = True
while active:
    message = input(prompt)
    if message == 'quit':
        active=False
    else:
        print(message)