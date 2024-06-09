nums=[3,3]
target=6
def sum_(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []
a=sum_(nums,target)
print(a)
