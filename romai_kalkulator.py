# -*- coding: utf-8 -*-

"""Roman number calculator

Created by Romeo Ervin Fukasz (FY78UY).
"""

import re


def arabic_to_roman(arabic_number):
    """Converts an arabic number to roman number

    Keyword arguments:
    arabic_number -- The input arabic number as integer
    """

    if not isinstance(arabic_number, int):
        raise TypeError("The input parameter of arabic_to_roman should be int")

    if not 0 < arabic_number < 4000:
        raise ValueError("Roman numbers can't be lower than 1 or higher than 3999")

    roman_values_from_arabic_values = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    result = ""

    for arabic_value, roman_value in roman_values_from_arabic_values.items():
        n = int(arabic_number / arabic_value)  # how many times can the value be subtracted from the arabic input
        result += roman_value * n  # append the roman value to the result string n times
        arabic_number -= arabic_value * n  # subtract the value that has been appended to the roman number result

    return result


def roman_to_arabic(roman_number):
    """Converts a roman number to arabic number.

    Keyword arguments:
    roman_number -- the roman number to be converted to arabic
    """

    if not isinstance(roman_number, str):
        raise TypeError("The input parameter of roman_to_arabic should be str")

    roman_number = roman_number.upper()

    arabic_values_from_roman_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }

    result = 0

    for index, roman_value in enumerate(roman_number):
        try:
            arabic_value = arabic_values_from_roman_values[roman_value]
            current_roman_value_is_not_last = index != len(roman_number) - 1

            """ If the next value in the input is smaller then the current one, it should be added to the
                result. If it is larger, then it should be subtracted, eg.: IV -> -1 + 5 """
            if current_roman_value_is_not_last and \
               arabic_values_from_roman_values[roman_number[index+1]] > arabic_value:
                result -= arabic_value
            else:
                result += arabic_value
        except KeyError:
            raise ValueError("The input is not a valid roman number")
    return result


def evaulate_roman_number_expression(expression):
    """Evaulates a mathematical expression that contains roman numbers.

    Keyword arguments:
    expression -- the roman number expression to be evaulated in a string
    """

    if not isinstance(expression, str):
        raise TypeError("The expression must be provided in a string")

    roman_number_regex = r'[IiVvXxLlCcDdMm]+'

    try:
        # find every roman number in the input string and replace it with an arabic number
        expression_with_arabic_numbers = re.sub(roman_number_regex,
                                                lambda x: str(roman_to_arabic(x.group())),
                                                expression)
        result_of_expression = int(eval(expression_with_arabic_numbers))
    except (SyntaxError, NameError):
        raise(ValueError("The provided roman number expression is not valid"))

    result_in_roman_numbers = arabic_to_roman(result_of_expression)
    return result_in_roman_numbers


if __name__ == "__main__":

    print("Roman number calculator\n\n")

    while True:  # main loop
        try:
            user_input = input("Please write an expression with roman numbers, then press ENTER. Exit with CTRL+C\n")
            result = evaulate_roman_number_expression(user_input)
            print(result)
        except KeyboardInterrupt:
            break  # exit program on CTRL+C
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            print()  # write an empty line to console before a new user input is asked
