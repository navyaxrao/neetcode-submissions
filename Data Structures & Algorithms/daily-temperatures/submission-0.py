class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        curr_index = 0
        for temp in temperatures:
            while stack and temp > stack[-1][0]:
                t, i = stack.pop()
                results[i] = curr_index - i
            stack.append((temp, curr_index))
            curr_index +=1
        return results

                

        

        