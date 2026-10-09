class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            #sort it from either smallest to largest or largest to smallest, then you want to take that i item and comapred it to the one enxt to it again and agian. \
        while len(stones)>1:
            stones.sort()
            current=stones.pop()-stones.pop()
            if current!=0:
                stones.append(current)
        if stones:
            return stones[0]
        else:
            return 0



        