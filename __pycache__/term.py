

def numbers():
    nums=[1,2,3,4,5]
    sum=nums[0]+nums[-1]
    nums[0]=sum-nums[0]
    nums[-1]=sum-nums[-1]
    print(nums)
    
    numbers()
    




