#reading a file
with open('FUNDAMENTALS OF PYTHON\operators.py','r') as file:
    content=file.read()
    print(content)
#writting in a file
with open('hello.txt','w') as file:
    file.write('hello this is a sample text')
#reading lines from txt
with open('hello.txt','r') as file:
    content=file.readlines()
    for line in content:
        print(line.strip())
#adding data in file without removing the existing data
with open('hello.txt','a') as file:
    file.write("\nadding new line whenever we run this program file.")
#error handling
file_path='hello.txt'
try:
    with open('file_path','r') as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print(f'file not found:{file_path}')