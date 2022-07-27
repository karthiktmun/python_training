s=input("Enter the string to be tested")
print(f"The string for which we will be check the middle character is '{s}'")

def get_middle(s):
    length=len(s)
    print(f"The length of the string is {length}")
    middle=length //2;
    if(middle % 2) != 0:
        print(s[middle])
    else:
        print(s[middle-1],s[middle])

get_middle(s)
