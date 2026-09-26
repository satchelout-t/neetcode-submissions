class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = {}
        count[0] = 1
        prefix = 0
        answer = 0
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            rem = prefix % k
            if rem in count:
                answer = answer + count[rem]
                count[rem] = count[rem] + 1
            else:
                count[rem] = 1
        return answer