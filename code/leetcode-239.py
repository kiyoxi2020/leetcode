'''
leetcode 239. 滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        out = []
        queue = collections.deque()
        for i in range(k):
            while(queue and nums[queue[-1]]<=nums[i]):
                queue.pop()
            queue.append(i)
        out.append(nums[queue[0]])
        for i in range(k, n, 1):
            while(queue and queue[0]<i-k+1):
                queue.popleft()
            while(queue and nums[queue[-1]]<=nums[i]):
                queue.pop()
            queue.append(i)
            out.append(nums[queue[0]])
        return out
