def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    numeros_vistos = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in numeros_vistos:
            return num
        numeros_vistos.add(num)

    return False
