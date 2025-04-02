tuple=('apple','mango')
print(tuple)
#tuple methods
print(tuple.count('mango'))
print(tuple.index('apple'))
#sets data type
thiset={'apple',2,'mango',2,4}
print(thiset)
#set methods
thiset.add('papaya')
print(thiset)
thiset.discard("apple")
#dictionary data type
people={'name':'sundaram','age':19,'add':'india'}
print(people)
print(people.keys())
print(people.values())
print(people['name'])
print(people['age'])
#methods for dic
# print(people.clear())
for x in people:
    print(people[x])
    #print(x) this will only give key values
