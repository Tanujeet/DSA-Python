class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx,cy = center
        bestCord = [-1,-1]
        bestQuality = -1

        for x,y,q in towers:
            dist = abs(x - cx) + abs(y-cy)
            if dist <= radius:
                if q > bestQuality:
                    bestQuality = q
                    bestCord =  [x,y]

                elif q == bestQuality:
                    if [x,y] < bestCord:
                        bestCord = [x,y]  
        
        return bestCord

            