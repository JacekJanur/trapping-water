from typing import List

class TrappedWater:
    def trap(self, clicked_values):
        """
        Args:
            clicked_values (list of tuple): A list of tuples representing clicked positions (x, y).

        Returns:
            list: A list containing the amount of trapped water at each position.
        """
        max_x = max(x for x, _ in clicked_values) if clicked_values else 0
        height = [0] * (max_x + 1)

        for x, y in clicked_values:
            height[x] = y + 1 

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = [0] * (max_x + 1)
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res[l] = max(leftMax - height[l], 0) 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res[r] = max(rightMax - height[r], 0)
        
        return res
