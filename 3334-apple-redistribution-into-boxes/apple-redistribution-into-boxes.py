class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total_apples = sum(apple)


        need = 0
        while total_apples > 0:
            total_apples -=capacity[need]
            need+=1


        return need    