class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # starting from the edges,
        # it only makes sense going deeper if i can find higher bars
        # since the width will always be smaller.

        # we care about the min of the two heights getting higher.
        # we cannot only move by one because there might be better solutions inside.
        # we must scan the entire array.

        # we move the shortest line since moving the tallest does not help.

        l=0
        r=len(heights)-1
        out = 0

        while l < r:
            width = r-l
            height = min(heights[l],heights[r])
            area = width*height
            out = max(out, area)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return out
            








