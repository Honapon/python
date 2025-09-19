# navn = ["stine", "mari", "ingrid"]

person = {"fornavn" : "Jonathan", "etternavn" : "Liu "}
print(person["fornavn"])

person["fornavn"] = "stine"

print(person["fornavn"])

person["alder"] = 27

print(person["fornavn"], person["etternavn"])

for value in person.values():
    print(value)

for keys in person.keys():
    print(keys)
    
for value, keys in person.items():
    print(value, keys)
# for i in person:
    # print(i)
    # print(person[i])