def is_palindrome(number):
    str_number = str(number)
    binary_number = bin(number)[2:]
    if str_number == str_number[::-1] and binary_number == binary_number[::-1]:
        return True
    else:
        return False


print(is_palindrome(8))
