age=int(input("Enter your age...."))
#input function always take string as input casted into int
if age>18:
    print("you are eligible to vote")
else:
    print("you are not eligible")

#elif 
score=int(input("Enter your score......"))
if score>=60:
    print("A")
elif 60 < score>= 40:
    print("B")
elif 40<score>=30:
    print("C")
else:
    print("D")