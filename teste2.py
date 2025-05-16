leak = []

while True:
    leak.append("x" * 10**6)  # Adiciona 1 MB de dados a cada loop 4
    print(f"Tamanho da lista: {len(leak)}")
