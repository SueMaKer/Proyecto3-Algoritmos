import random
from genetic.mutation import mutate

# Semilla para reproducibilidad
random.seed(42)

# === BITFLIP TEST ===
bit_individual = [1, 0, 0, 1, 1, 0, 1, 0]
bit_params = {
    'mutation_type': 'bitflip',
    'mutation_rate': 0.2  # 20% de probabilidad de mutar cada gen
}

print("=== BITFLIP MUTATION ===")
print("Original:", bit_individual)
mutated_bit = mutate(bit_individual, bit_params)
print("Mutado  :", mutated_bit)

# === SWAP TEST ===
perm_individual = [1, 2, 3, 4, 5, 6, 7, 8]
swap_params = {
    'mutation_type': 'swap',
    'mutation_rate': 0.3  # 30% del tamaño = 2 swaps aprox (si hay 8 genes)
}

print("\n=== SWAP MUTATION ===")
print("Original:", perm_individual)
mutated_perm = mutate(perm_individual, swap_params)
print("Mutado  :", mutated_perm)
