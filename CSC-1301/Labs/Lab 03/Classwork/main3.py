quarters = int(input())
dimes = int(input())
nickels = int(input())
pennies = int(input())


dollars = ((quarters*25)+(dimes*10)+(nickels*5)+(pennies)) / 100

print(f'Amount: ${dollars:.2f}')
