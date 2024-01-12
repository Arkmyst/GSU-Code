def laps_to_miles(user_laps):
    convert = .25 * user_laps
    return (convert)

def main():
    user_laps = float(input("Input a Number : "))
    print(f'{laps_to_miles(user_laps):.2f}')
main()