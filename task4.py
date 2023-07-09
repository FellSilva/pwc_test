def capitalize_sentences(string):
    # Dividir a string em frases usando o ponto como delimitador
    sentences = string.split('. ')

    # Capitalizar a primeira letra de cada frase
    capitalized_sentences = []
    for sentence in sentences:
        capitalized_sentence = sentence[0].capitalize() + sentence[1:]
        capitalized_sentences.append(capitalized_sentence)

    # Juntar as frases em uma nova string
    capitalized_string = '. '.join(capitalized_sentences)

    return capitalized_string


# Caso de teste
input_string = "hello. how are you? i'm fine, thank you."
result = capitalize_sentences(input_string)
print(f"Input: {input_string}")
print(f"Output: {result}")
