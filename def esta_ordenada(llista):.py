def esta_ordenada(llista):
    """Comprova si la llista està ordenada en ordre ascendent, descendent o no està ordenada."""
    if all(llista[i] <= llista[i + 1] for i in range(len(llista) - 1)):
        return "Està ordenada de forma ascendent."
    elif all(llista[i] >= llista[i + 1] for i in range(len(llista) - 1)):
        return "Està ordenada de forma descendent."
    else:
        return "No està ordenada."

# Proves de la funció
print(esta_ordenada([3, 2, 1]))  # Retorna "Està ordenada de forma descendent."
print(esta_ordenada([4, 5, 6]))  # Retorna "Està ordenada de forma ascendent."
print(esta_ordenada([1, 2, 3, 2]))  # Retorna "No està ordenada."
print(esta_ordenada([5, 5, 5]))  # Retorna "Està ordenada de forma ascendent." (o descendent, depenent de la implementació)
print(esta_ordenada([]))  # Retorna "Està ordenada de forma ascendent." (una llista buida es considera ordenada)
