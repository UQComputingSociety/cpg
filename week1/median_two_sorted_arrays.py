# For more details, refer to: https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution:
    """
    Basic idea:
    
    Split each array into two, note points of splitting each array.
    Merge the left sides of both arrays together,
    and merge the right sides of both arrays together.
    
    The median can alternatively be defined as when
    every element of the combined left side is less than or equal to
    every element of the combined right side.
    
    An equivalent condition is when
    maxLeftX <= minRightY and maxLeftY <= minRightX
    (since the arrays are sorted).
    
    We move the point of splitting between left and right
    until we have reached the point where the above equivalent condition holds.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        
        # Without loss of generality, assume x < y
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low = 0
        high = x
        
        while low <= high:
            # Point to split each array
            partitionX = (low + high)//2
            partitionY = (x + y + 1)//2 - partitionX
            print(partitionX, partitionY)
            
            # We only care about four elements
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Conditions for a median
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Even median: take two middle elements and find average
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                # Odd median: take middle element
                else:
                    return max(maxLeftX, maxLeftY)
            # Move towards left in X
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # Move towards right in X
            else:
                low = partitionX + 1