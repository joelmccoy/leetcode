# problem: https://leetcode.com/problems/3sum/


def three_sum(nums: list[int]) -> list[list[int]]:
    # O(nlogn)
    nums.sort()
    results = []

    # O(n^2)
    for idx in range(len(nums)):
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue

        l, r = idx + 1, len(nums) - 1
        while l < r:
            x_val, l_val, r_val = nums[idx], nums[l], nums[r]
            the_sum = sum((x_val, l_val, r_val))
            if the_sum == 0:
                results.append([x_val, l_val, r_val])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            elif the_sum > 0:
                r += -1
            elif the_sum < 0:
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return results
