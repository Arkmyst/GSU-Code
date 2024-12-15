def swap_values(user_val1, user_val2, user_val3, user_val4):
    lst = [user_val2, user_val1, user_val4, user_val3]
    mystring = ' '.join(map(str,lst))
    print(mystring)


def main():
    user_val1 = int(input("First : "))
    user_val2 = int(input("Second : "))
    user_val3 = int(input("Third : "))
    user_val4 = int(input("Fourth : "))

    swap_values(user_val1, user_val2, user_val3, user_val4)
main()