import ast

def findLHS(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_len = 0
    for x in freq:
        if x + 1 in freq: 
            length = freq[x] + freq[x+1]
            if length > max_len:
                max_len = length 
    return max_len

nums = ast.literal_eval(input())
print(findLHS(nums))
