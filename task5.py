def is_anagram_of_palindrome(string):
    char_count = {}
    odd_count = 0

    # Contar a ocorrência de cada caractere na string
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Verificar quantos caracteres têm contagem ímpar
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Se houver no máximo uma contagem ímpar, é um anagrama de um palíndromo
    return odd_count <= 1


# Caso de teste
input_string = "racecar"
result = is_anagram_of_palindrome(input_string)
print(f"Input: {input_string}")
print(f"Output: {result}")
