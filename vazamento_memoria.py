# vazamento_memoria.py

import time

class ObjetoPesado:
    def __init__(self):
        # Aloca uma grande quantidade de memória (simula um objeto pesado) 4
        self.dados = [0] * 10**6  # ~8 MB por instância

# Lista global que nunca é liberada
objetos_vazando = []

def vazamento_de_memoria():
    contador = 0
    while True:
        obj = ObjetoPesado()
        objetos_vazando.append(obj)  # nunca removemos nada da lista
        contador += 1
        print(f"Objeto {contador} criado e armazenado. Memória total em uso aumenta.")
        time.sleep(0.5)  # reduz velocidade para monitorar no gerenciador de tarefas

if __name__ == "__main__":
    vazamento_de_memoria()
