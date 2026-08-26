class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       n=len(nums)
       dic={}
       ans=[]
       for num in nums:
            if num in dic:
                dic[num]=dic[num]+1
            else:
                dic[num]=1
       sorted_dic = sorted(dic.items(), key=lambda pair: pair[1], reverse=True)
       for i in range(0,k):
            ans.append(sorted_dic[i][0])

       return ans