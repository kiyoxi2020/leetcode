'''
leetcode 769. 最多能完成排序的块

数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-chunks-to-make-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ed = arr[0]
        n = len(arr)
        i = 0
        count = 0
        # if n==1 and ed==0: count+=1
        while(i<n):
            if arr[i]>ed: ed=arr[i]
            if i==ed or i==n-1: 
                count += 1
                ed+=1
            i+=1
        return count
