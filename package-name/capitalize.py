def capitalize(text):
    if text == '':
        return ''
    first_char, *rest_char = text
    rest_subsrting = ''.join(rest_char)
    return f'{first_char.upper()}{rest_subsrting}'