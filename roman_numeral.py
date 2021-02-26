def is_okay(roman):
    flag = True
    count_char = {}

    for letter in roman.upper():
        count_char.setdefault(letter, 0)
        count_char[letter] += 1

        if count_char.get(letter) >= 4:
            print("'{}' cannot be repeated 4 times or more! See the rules for more information.".format(letter))
            flag = False
            return flag
        elif letter not in 'IVXLCDM':
            print(letter + " is not a valid Roman Numeral.")
            flag = False
            return flag
        else:
            flag = True

    return flag


def try_again(reply):
    if reply.lower() == 'y':
        decision_bool = True
    elif reply.lower() == 'n':
        decision_bool = False
    else:
        print("Invalid token!")
        decision_bool = False
    return decision_bool


def roman2int(roman):
    roman_dict = {
        'i': 1,
        'I': 1,
        'v': 5,
        'V': 5,
        'x': 10,
        'X': 10,
        'l': 50,
        'L': 50,
        'c': 100,
        'C': 100,
        'd': 500,
        'D': 500,
        'm': 1000,
        'M': 1000
    }

    flag = is_okay(roman)

    result = 0

    if flag is True:
        i = 0

        for number in roman:
            current_iter = roman[roman.index(number)]
            current_number = roman.index(number)
            try:
                next_iter = roman[roman.index(number) + 1]
                next_number = roman.index(number) + 1
            except IndexError:
                print("")

            if roman[next_number] is not None and roman_dict.get(next_iter) > roman_dict.get(current_iter):
                result -= roman_dict.get(number)
            else:
                result += roman_dict.get(number)

                i += 1

        print(result)

        return result

    else:
        print("Try again later!")
        quit()


decision = True

while decision:

    print("\nRoman Number Converter")
    print("")
    print("1 - Convert roman number.")
    print("2 - See the rules.")
    print("3 - Exit the program.")
    print()
    answer_number = (input("What do you want?"))

    if answer_number == '1':
        roman2int((input("\nType a roman number: ")))

        answer = (input("\nDo you want to try again? y = yes / n = no"))
        decision = try_again(answer)
    elif answer_number == '2':
        print("""\n\t\t\t\t\t# +------+-----+-----+-----+-----+-----+-----+-----+
            \t\t# | Char |  I  |  V  |  X  |  L  |  C  |  D  |  M  |
            \t\t# | Value|  1  |  5  | 10  | 50  | 100 | 500 | 1000|
            \t\t# +------+-----+-----+-----+-----+-----+-----+-----+""")
        print("\n1st Rule - The letters I, X, C, M can only be repeated for three consecutive times.")
        print("2nd Rule - The letters I, X, C can be written in front of the others, with their values added to the "
              "\nletter of greatest value.")
        print("3rd Rule - The letters I, X, C can be written before the other, having their values subtracted from the "
              "\nletter of greatest value.")
        print("4rd Rule - Since MMMM cannot be written in Roman numerals, the highest value available in the program "
              "is 3999, which would be 'MMMCMXCIX'")

        answer = (input("\nDo you want to return to the beginning of the program? y = yes / n = no"))
        decision = try_again(answer)
    elif answer_number == '3':
        print("Try again anytime!")
        quit()
    else:
        answer_number = None
        print("Invalid token!")

        answer = (input("\nDo you want to try again? y = yes / n = no"))
        decision = try_again(answer)
quit()
