

def partition_memo(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    memo = {}

    def dp(i, current_sum):
        if current_sum == 0:
            return True
        if i == 0 or current_sum < 0:
            return False
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        include = dp(i - 1, current_sum - nums[i - 1])
        exclude = dp(i - 1, current_sum)
        memo[(i, current_sum)] = include or exclude
        return memo[(i, current_sum)]

    return dp(len(nums), target)



def partition_recursive(nums, n, target):
    # Caso base: si target llega a 0, hay una combinación que da la mitad
    if target == 0:
        return True
    if n == 0 or target < 0:
        return False
    # Incluir el elemento actual o no incluirlo
    include = partition_recursive(nums, n - 1, target - nums[n - 1])
    exclude = partition_recursive(nums, n - 1, target)
    return include or exclude



