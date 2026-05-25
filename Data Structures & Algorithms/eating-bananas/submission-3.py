class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # set left and right pointers
        left = 1
        right = max(piles)
        speed = right

        while left <= right:
            time = 0
            mid = (left + right) // 2
            for pile in piles:
                time += math.ceil(pile / mid)

            if time > h:
                left = mid + 1
            
            if time <= h:
                speed = min(mid, speed)
                right = mid - 1
        
        return speed
            

            


    
        