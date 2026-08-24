class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zeros = 0
        mult2 = 1
        for num in nums:
            mult *= num
            if num == 0:
                zeros += 1
        if zeros == 1:
            for num in nums:
                if num != 0:
                    mult2 *= num

        answer = []
        for num in nums:
            if num == 0 and zeros == 1:
                answer.append(mult2)
            elif num == 0 and zeros != 1:
                answer.append(0)
            else:
                answer.append(mult // num)
        return answer