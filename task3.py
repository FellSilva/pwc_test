def longest_palindrome_substring(s):
    n = len(s)
    # Tabela para armazenar se uma substring é palindrômica
    dp = [[False] * n for _ in range(n)]
    start = 0  # Índice inicial da substring palindrômica mais longa
    max_length = 1  # Comprimento da substring palindrômica mais longa

    # Todas as substrings de comprimento 1 são palindrômicas
    for i in range(n):
        dp[i][i] = True

    # Verificar substrings de comprimento 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Verificar substrings de comprimento maior que 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    # Extrair a substring palindrômica mais longa
    longest_palindrome = s[start : start + max_length]

    return longest_palindrome


# Caso de teste
input_string = "babad"
result = longest_palindrome_substring(input_string)
print(f"Input: {input_string}")
print(f"Output: {result}")
