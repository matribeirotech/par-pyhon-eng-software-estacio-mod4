def buscar_maior_inteiro_com_recursividade(lista):
    """
    Função que busca o maior inteiro em uma lista utilizando recursividade.

    Args:
        lista (list): Lista de inteiros.

    Returns:
        int: O maior inteiro encontrado na lista.
    """
    if len(lista) == 1:
        return lista[0]
    else:
        max_restante = buscar_maior_inteiro_com_recursividade(lista[1:])
        return lista[0] if lista[0] > max_restante else max_restante # Return com comparação direta do primeiro elemento com o máximo do restante da lista
buscar_maior_inteiro_com_recursividade([3, 5, 2, 8, 1])
print(buscar_maior_inteiro_com_recursividade([3, 5, 2, 8, 1]))  # Saída: 8
    
