while True:
    # Ask the user to enter a string
    input_string=input("Please enter the string.Press Q to Quit")
    #Exit if user enters "Q" or "q"
    if input_string=="q" or input_string == "Q":
        break
    else:
        def check_string(input_string):
            reverse_string = input_string[::-1].capitalize()
            if input_string.capitalize()==reverse_string:
                print("{} is a palindrome".format(input_string))
            else:
                print("{} is not a palindrome".format(input_string))
        check_string(input_string)
    print("Thank you for participating")