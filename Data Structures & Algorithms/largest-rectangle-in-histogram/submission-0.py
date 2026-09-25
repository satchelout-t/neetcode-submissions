class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # stores indices
        max_area = 0

        for i in range(len(heights) + 1):

            # Treat the extra position as height 0
            curr_height = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > curr_height:
                h = heights[stack.pop()]

                # After popping, stack[-1] is the first smaller
                # element on the left
                left = stack[-1] if stack else -1

                width = i - left - 1

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area