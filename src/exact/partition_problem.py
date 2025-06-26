

def dp_topdown_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    memo = {}

    def helper(i, current_sum):
        if current_sum == target:
            return True
        if i == len(nums) or current_sum > target:
            return False
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        # Incluye o excluye el elemento actual
        include = helper(i + 1, current_sum + nums[i])
        exclude = helper(i + 1, current_sum)
        memo[(i, current_sum)] = include or exclude
        return memo[(i, current_sum)]

    return helper(0, 0)



def recursive_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False  # No se puede dividir en dos subconjuntos iguales

    target = total_sum // 2

    def helper(i, current_sum):
        if current_sum == target:
            return True
        if i == len(nums) or current_sum > target:
            return False
        return helper(i + 1, current_sum + nums[i]) or helper(i + 1, current_sum)

    return helper(0, 0)



