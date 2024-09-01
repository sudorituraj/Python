'''score = int(input("what's the number? "))
if score >= 90 and score <= 100:
    print("grade A")


elif score >= 80 and score < 90:
    print("grade b")

elif score >= 70 and score < 80:
    print(" grade c")

elif score >= 60 and score < 70:
    print("Grade D")

else :
    print(" Grade F")'''

#another way 

score = int(input("what's the number? "))
if 90 <= score <= 100:
    print("grade A")

elif 80 <= score < 90:
    print("grade b")

elif 70 <= score < 80:
    print(" grade c")

elif 60 <= score < 70:
    print("Grade D")

else :
    print(" Grade F")