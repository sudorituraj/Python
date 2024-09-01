'''x = int(input("Enter the value of x"))

if x % == 0 :
    print("Even")

else :
    print ("odd")'''


#by using finction


def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")


def is_even(n) :
    if n % 2 == 0 :
        return True
    else:
        return False
    

main()
