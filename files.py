with open("DataStructure/testFile.txt") as file:
    data = file.readlines()
    x = data[0].strip()
    print(x)
#print(data[1])


print('www.example.com'.strip('cmowz.'))

x = "Lat Long"
print(x.strip('Lang'))