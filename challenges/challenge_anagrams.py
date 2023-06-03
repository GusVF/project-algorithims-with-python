def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return ''.join(result)


def sorting(chars: str):
    if len(chars) <= 1:
        return chars

    mid = len(chars) // 2
    left = sorting(chars[:mid])
    right = sorting(chars[mid:])
    return merge(left, right)


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
