import csv
data=[
   
         ['Name','Age','City'],
    
        ['sundaram','19','ghosia'],
    
        ['aman','19','ghosia'],
    
        ['rahul','19','ghosia']
]
with open('file.csv','w') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
with open('file.csv','r', newline='')as file:
    csv_reader=csv.reader(file)
    for row in csv_reader:
        print(row)