import time
import random
import string

# Lista global que acumula dados desnecessariamente 8
memory_leak_simulation = []

def generate_random_string(size=10000):
    """Gera uma string aleatória grande"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def leak_memory():
    while True:
        # Gera dados que não serão mais usados, mas continuam referenciados
        data = generate_random_string()
        memory_leak_simulation.append(data)

        print(f"Objetos acumulados: {len(memory_leak_simulation)}")

        # Aguarda para tornar o crescimento mais visível com ferramentas de profiling 
        time.sleep(0.5)

if __name__ == "__main__":
    leak_memory()
