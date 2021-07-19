'''
leetcode 307. 区域和检索 - 数组可修改

给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。

实现 NumArray 类：

NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值更新为 val
int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + nums[left + 1], ..., nums[right]）

https://leetcode-cn.com/problems/range-sum-query-mutable/
'''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.tree = [0] * (2*n)
        for i in range(n, 2*n ,1):
            self.tree[i] = nums[i-n]
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
        self.nums = nums
        self.n = n
        return


    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        n = self.n
        self.nums[index] = val
        index += n
        self.tree[index] = val
        index = (index)//2
        while(index>0):
            self.tree[index] = self.tree[index*2]+self.tree[index*2+1]
            index = (index)//2
        return 

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum0 = 0
        n = self.n
        left += n
        right += n
        while(left<=right):
            if left%2==1:
                sum0+=self.tree[left]
                left+=1
            if right%2==0:
                sum0+=self.tree[right]
                right-=1
            left /= 2
            right /= 2
        return sum0




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)