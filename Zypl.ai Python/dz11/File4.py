'''thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "owner": "Muazzam"
}
newdict = dict.copy(thisdict)
newdict["newkey"] = 1234
print(newdict)
print(thisdict["owner"])
print(type(thisdict))

##n = int(input("Input N: "))
###d = {1:2, 2:4, 3:9}
###d[4] = 4**2
###print(dict.keys(d))
d = {}
for x in range(n):
    key = input("Key: ")
    value = input("Value: ")
    d[key] = value
print(d)
'''
e = {a: a * 3 for a in range(5, 11)}
ed = [i ** 2 for i in range(1, 11)]
print(e)
print(ed)
