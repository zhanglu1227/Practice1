'''
给定一个整数数组nums和一个目标值target,请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标
给定nums = [2, 7, 11, 15]
target = 9
'''


def sumA(nums,target):

    a = len(nums)
    for i in range(a):
        for j in range(i, a):
            if nums[i] + nums[j] == target:
                return i, j

nums = [2, 7, 11, 15]
target = 9
b = sumA(nums, target)
print(b)