def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return dollars_per_gallon/miles_per_gallon*miles_driven

def main():
    miles_per_gallon = float(input("Enter Miles per Gallon : "))
    dollars_per_gallon = float(input("Enter Dollars per Gallon : "))

    print(f'{driving_cost(miles_per_gallon,dollars_per_gallon,10):.2f}')
    print(f'{driving_cost(miles_per_gallon,dollars_per_gallon,50):.2f}')
    print(f'{driving_cost(miles_per_gallon,dollars_per_gallon,400):.2f}')
main()
