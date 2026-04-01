class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots  = list(zip(positions,healths,directions,range(n)))
        robots.sort(key=lambda x: x[0])

        stack = []

        for pos,health,dir,idx in robots:
            if dir == "R":
                stack.append([pos,health,dir,idx])
            else:
                while stack and stack[-1][2] == "R":


                    if stack[-1][1] > health:
                        stack[-1][1] -=1
                        health = 0
                        break
                    

                    elif stack[-1][1] < health:
                        health -=1
                        stack.pop()
                    

                    else:
                        stack.pop()
                        health = 0
                        break
                

                if health > 0 :
                    stack.append([pos,health,dir,idx])
        

        res = [0] * n

        for _ , health,_,idx in stack:
            res[idx] = health
        

        return [x for x in res if x > 0]
