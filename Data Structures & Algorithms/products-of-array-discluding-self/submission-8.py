class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zeros = 0
        mult2 = 1
        for num in nums:
            mult *= num
            if num == 0:
                zeros += 1
            else:
                mult2 *= num

        if zeros > 1:
            return [0] * len(nums)
        answer = []
        for num in nums:
            if num == 0:
                answer.append(mult2)
            else:
                answer.append(mult // num)
        return answer