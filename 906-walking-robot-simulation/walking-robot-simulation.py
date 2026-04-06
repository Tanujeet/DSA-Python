class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx  = [0,1,0,-1]
        dy  = [1,0,-1,0]

        obstacle_set = set(map(tuple, obstacles))


        ans = 0
        x = 0 
        y = 0
        di = 0

        for num in commands:
            if num == -2:
                di = (di + 3) % 4
            
            elif num == -1:
                di = (di + 1) % 4
            

            else:
                for _ in range(num):
                    nx , ny = x + dx[di] , y + dy[di]

                    if (nx , ny) not in obstacle_set:
                        x,y = nx , ny
                        ans =  max(ans,x*x+y*y)
                    else:
                        break
        

        return ans 