
def compute(nums):
    n = len(nums)
    st = 0
    count = 0
    while(st<n-1):
        t = nums[st]
        max0 = 0
        select = st+1
        for i in range(t):
            ind = st+i+1
            if ind >= n-1:
                select = ind
                break
            if nums[ind]+ind>max0:
                max0 = nums[ind]+ind
                select = ind
        st = select
        count += 1
    print(count)
    return

while(1):
    data = [int(i) for i in input().split()]
    compute(data)