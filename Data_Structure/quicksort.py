#TODO: 快排


def partition(nums):
    if len(nums) == 1:
        result.append(nums[0])
        return nums[0]
    # 获取初始头和尾的位置 枢纽位置
    left = 0
    right = len(nums)-1
    pivot = nums[left]
    while left < right:
        #开始从右往左
        while left < right:
            if pivot < nums[right]:
                right -= 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                break

        # 从左往右开始
        while left < right:
            if pivot > nums[left]:
                left += 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
                break
    # 当left == right时，分割成两个区块
    if left == right:
        if len(nums) == 1:
            result.append(nums[0])
            return nums[0]
        elif left == 0:
            result.append(nums[0])
            partition(nums[1:])
        elif right == len(nums) -1:
            partition(nums[0:left])
            result.append(pivot)
        else:
            partition(nums[0:left])
            result.append(pivot)
            partition(nums[right+1:])

    return nums

#TODOP: 递归调用
def quicksort(nums):
    partition(nums)
    return 0

if __name__ == '__main__':
    # 排序数组：
    nums = [1, 2, 4, 5, 11, 22, 3, 7, 12, 33, 99, 13, 188, 1]
    # 存储最终结果
    result = []
    quicksort(nums)
    print(result)

