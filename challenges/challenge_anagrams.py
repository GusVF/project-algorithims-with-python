def sorting(chars: str):
    chars_list = list(chars.lower())
    for i in range(1, len(chars_list)):
        key = chars_list[i]
        j = i - 1
        while j >= 0 and chars_list[j] > key:
            chars_list[j + 1] = chars_list[j]
            j -= 1
        chars_list[j + 1] = key
    return ''.join(chars_list)


def is_anagram(first_string: str, second_string: str):
    if not first_string:
        return ("", sorting(first_string + second_string), False)
    if not second_string:
        return (sorting(first_string + second_string), "", False)

    first_chars = sorting(first_string.lower())
    second_chars = sorting(second_string.lower())

    is_anagram = first_chars == second_chars

    return (first_chars, second_chars, is_anagram)


result = is_anagram('Pato', 'tapo')
print(result)
