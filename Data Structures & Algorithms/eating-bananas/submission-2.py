class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the maximum pile
        maxPile = float('-inf')
        for pile in piles:
            if pile > maxPile:
                maxPile = pile
        # set left and right pointers
        left = 1
        right = maxPile
        speed = float('inf')

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
            

            


    
        