'''
Coding Patterns List created by Daniel Lam
'''
# Sliding Window
# Use Case:
# Linear data structures (arrays, lists, strings)
# Must scan through a subarray or substring
# When the subarray must satisfy some condition (shortest/longest/min/max)
# Improve time complexity from O(N^2) to O(N)

# Dyanmic Sliding Window

# Generic Template for Dynamic Sliding Window Finding 
# Minimum Window Length
def shortest_window(nums, condition):
    left = 0
    min_length = float('inf')
    result = None
    for right, element in enumerate(nums):
        # Expand the window
        # Adds nums[right] to the current window logic

        # Shrink window as long as the condition is met
        while condition():
            # Update the result if the current window is smaller
            if right - left + 1 < min_length:
                min_length = right - left + 1
                # Add business logic to update the result
            
            # Shrink the window from the left 
            # Remove nums[left] from the current window logic
            left += 1
    return result

# Maximum Window Length
def longest_window(nums, condition):
    left = 0
    max_length = 0
    result = None

    for right, element in enumerate(nums):
        # Expand the window
        # Add nums[right] to the current window logic

        # Shrink the window if the condition is violated
        while not condition():
            # Shrink the window if the condition is violated
            # Remove nums[left] from the current window logic
            left += 1

            # Update the result if the current window is larger
            if right - left + 1 > max_length:
                max_length = right - left + 1
                # Add business logic to update result
    return result

# Fixed Window Sliding Window
def longest_window(nums, k):
    left = 0
    max_length = 0
    result = None

    for right in enumerate(nums):
        # Expand the window
        # Add nums[right] to the current window logic

        # Ensure window has size of K
        if (right - left + 1) < k:
            continue
        # Update Result
        # Remove nums[left] from window
        # increment left to maintain fixed window size of length K
        left += 1
    return result

# LeetCode Questions to Practice
# 3. Longest Substring Without Repeating Characters
# 424. Longest Repeating Character Replacement
# 1876. Substrings of Size Three with Distinct Characters
# 76. Minimum Window Substring



