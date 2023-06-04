def find_duplicate(nums: list):
    if not (
        isinstance(nums, list)
        and all(isinstance(num, int) for num in nums)
        and all(num >= 0 for num in nums)
        and len(nums) > 1
    ):
        return False
    sorting = sorted(nums)
    for i in range(0, len(sorting)):
        key = sorting[i]
        if i < len(sorting) - 1 and key == sorting[i + 1]:
            return key
    return False


nums = [10, 2, 8, 1, 6, 4, 9, 0, 5, 3, 8]
result = find_duplicate(nums)
print(result)
