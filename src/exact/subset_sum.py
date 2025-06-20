def fitness_subset_sum(chromosome, items, target):
    total = sum(gene * item for gene, item in zip(chromosome, items))
    if total > target:
        return 0  # penalización por pasarse
    else:
        return total  # cuanto más cerca al target, mejor

# cambiar n a cantidad de elementos
def recursive_subset_sum(nums, n, target):
    # Caso base: si el target es 0, lo logramos
    if target == 0:
        return True

    # Si no hay elementos y el target no es 0, no es posible
    if n == 0:
        return False

    # Si el elemento actual es mayor que el target, lo ignoramos
    if nums[n - 1] > target:
        return recursive_subset_sum(nums, n - 1, target)

    # Consideramos dos posibilidades: incluirlo o no
    return (recursive_subset_sum(nums, n - 1, target) or
            recursive_subset_sum(nums, n - 1, target - nums[n - 1]))

""" # Ejemplo de uso
conjunto = [3, 34, 4, 12, 5, 2]
objetivo = 9

if recursive_subset_sum(conjunto, len(conjunto), objetivo):
    print(f"Existe un subconjunto con suma {objetivo}")
else:
    print(f"No existe un subconjunto con suma {objetivo}") """



# Definimos la función con memoización (top-down)
def subset_sum_top_down(nums, n, target, memo=None):
    # Si es la primera llamada, inicializamos el diccionario de memoización
    if memo is None:
        memo = {}

    # Caso base: si el objetivo es 0, existe un subconjunto válido (el subconjunto vacío)
    if target == 0:
        return True

    # Caso base: si ya no hay elementos pero el objetivo no es 0, no se puede lograr
    if n == 0:
        return False

    # Creamos una clave única para este subproblema: (cantidad de elementos, objetivo actual)
    key = (n, target)

    # Si ya resolvimos este subproblema antes, devolvemos la respuesta guardada
    if key in memo:
        return memo[key]

    # Si el último número es mayor que el objetivo, no podemos usarlo (lo excluimos)
    if nums[n - 1] > target:
        result = subset_sum_top_down(nums, n - 1, target, memo)

    else:
        # Intentamos dos opciones:
        # 1. No usar el número actual
        # 2. Usar el número actual y reducir el objetivo en su valor
        result = (subset_sum_top_down(nums, n - 1, target, memo) or
                  subset_sum_top_down(nums, n - 1, target - nums[n - 1], memo))

    # Guardamos la solución en el diccionario memo para evitar recalcularla en el futuro
    memo[key] = result

    # Devolvemos el resultado
    return result



