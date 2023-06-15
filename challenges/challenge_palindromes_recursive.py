def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
# Verifica se a entrada for vazia
    if low_index >= high_index:
        return True
# Verifica se a palavra tem apenas um caractere ou nenhum
    if word[low_index] != word[high_index]:
        return False
# Verifica se os caracteres nos extremos são iguais
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
# Chamada recursiva para verificar os caracteres internos da palavra
