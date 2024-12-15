def main():
    word = input("Enter a Password: ")
    password = list(word)
    newpass = ''

    for i in range(0,len(password)):
        if password[i] == 'i':
            password[i] = '1'

        if password[i] == 'a':
            password[i] = '@'

        if password[i] == 'm':
            password[i] = 'M'

        if password[i] == 'B':
            password[i] = '8'

        if password[i] == 's':
            password[i] = '$'

        newpass = newpass + password[i]
    
    print(f"{newpass}!")
main()