def quicksort(nums):
    if nums:
        pivot = partition(nums)
        quicksort(nums[:pivot])
        quicksort(nums[pivot + 1:])


def partition(nums):
    def swap(p, q):
        temp = nums[p]
        nums[p] = nums[q]
        nums[q] = temp

    pivot = nums[0]
    count_lower = 0
    # Move all numbers lower than the pivot to the left
    for i in range(len(nums)):
        if nums[i] < pivot:
            count_lower += 1
            swap(i, count_lower)
    # Move the pivot to the correct position
    swap(0, count_lower)
    return count_lower


if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    quicksort(nums)
    print(nums)
