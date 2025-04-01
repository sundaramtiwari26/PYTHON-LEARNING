#multiline
name="""
hello 
its me
sundaram 
learning python
"""
print(name)
#string slicing
name2="sundaram"
print(name2[1:4])
#changing case
name3="sundaram"
print(name3.upper())
print(name3.lower())
print(name3.strip())
print(name3.replace("a","A"))
#cancatination in string
a="hello"
b="world"
c=a+" "+b
print(c)
firstname="sundaram"
secondname="tiwari"
print(firstname+" "+secondname)
#string formatting
age=19
text="hello i am sundaram tiwari and i am {} year old"#placeholder
print(text.format(age))
qty=2
itemno=345
price=56
text=" i want {} pieces of item {} for {} rupees"
print(text.format(qty,itemno,price))
text=f"i want {qty} pieces of item {itemno} for {price} rupees"
print(text)