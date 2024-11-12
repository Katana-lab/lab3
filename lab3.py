def count_letters_and_digits(s):
    letter_count = 0
    digit_count = 0

    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letter_count += 1
        elif '0' <= char <= '9':
            digit_count += 1

    return letter_count + digit_count

print(count_letters_and_digits("hel2!lo"))
print(count_letters_and_digits("wicked .. !"))
print(count_letters_and_digits("!?..A"))
