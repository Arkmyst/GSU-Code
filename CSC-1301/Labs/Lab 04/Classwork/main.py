#caffiene = half life of 6 hrs in humans

#given caffiene amt as (input) - calc the output in 6,12, and 24 hrs
def main():
    Caffeine = float(input())

    firstHalf = Caffeine/2
    secondHalf = firstHalf/2
    thirdHalf = secondHalf/4

    print(f'After 6 hours: {firstHalf:.2f} mg')
    print(f'After 12 hours: {secondHalf:.2f} mg')
    print(f'After 24 hours: {thirdHalf:.2f} mg')

main()