def exact_change(user_total):
    num_quarters = user_total // 25
    user_total = user_total % 25
    num_dimes = user_total // 10
    user_total = user_total % 10
    num_nickels = user_total // 5
    user_total = user_total % 5
    num_pennies = user_total
    return(num_quarters, num_dimes, num_nickels, num_pennies)



if __name__ == '__main__': 
    input_val = int(input())    
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

    if input_val <= 0:
        print("Add change")
        input_val = int(input())    
    print()
    if num_quarters > 1:
        print(f"{num_quarters} quarters")
    else:
        print(f"{num_quarters} quarter")

    if num_dimes > 1:
        print(f"{num_dimes} dimes")
    else:
        print(f"{num_dimes} dime")

    if num_nickels > 1:
        print(f"{num_nickels} nickels")
    else:
        print(f"{num_nickels} nickel")

    if num_pennies > 1:
        print(f"{num_pennies} pennies")
    else:
        print(f"{num_pennies} penny")