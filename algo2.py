def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Якщо елемент не знайдено, повертаємо "верхню межу"
    if right >= 0:
        return iterations, arr[right]
    else:
        return iterations, None

