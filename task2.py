def remove_duplicates(string):
    # Converter a string em uma lista de caracteres
    chars = list(string)

    # Criar uma nova lista sem caracteres duplicados
    unique_chars = []
    for char in chars:
        if char not in unique_chars:
            unique_chars.append(char)

    # Juntar os caracteres únicos em uma nova string
    unique_string = ''.join(unique_chars)

    # Retornar a nova string
    return unique_string


# Caso de teste
test_case = "Hello, world"
result = remove_duplicates(test_case)
print(f"Input: {test_case}")
print(f"Output: {result}")
