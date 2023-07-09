def reverse_sentence(sentence):
    # Dividir a frase em palavras
    words = sentence.split()

    # Inverter a ordem das palavras
    reversed_words = words[::-1]

    # Reunir as palavras em uma nova frase
    reversed_sentence = ' '.join(reversed_words)

    # Retornar a nova frase
    return reversed_sentence


# Casos de teste
test_cases = [
    "hello, world! open ia is amazing",
    "this is a test",
    "programming is fun"
]

for test_case in test_cases:
    result = reverse_sentence(test_case)
    print(f"Input: {test_case}")
    print(f"Output: {result}")
    print()
