"""
**Practice: Remove Duplicates in String**

Remove Adjacent Duplicates in String. You are given a string `s` and an integer `k`. Write a function to remove `k` adjacent duplicates from `s` where the "adjacent" characters are equal.
"""
def identify_adjacent(s: str, k: int) -> str:
    # want to store pair of characters and their consecutive counts
    # [[char: count]
    stack = []

    # iterate through each character in string
    for char in s:
        # if string isn't empty and last element, first index is char...
        # increment char count by 1
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        # append character and a count of 1
        else:
            stack.append([char, 1])
        # if stack's last element, first index value is equal to k...
        # remove it from the stack
        if stack[-1][1] == k:
            stack.pop()

    # return string from stack by repeating each char according to its count
    return ''.join(char * count for char, count in stack)

print(identify_adjacent('daaabbbaa', 3)) # 'daa'
print(identify_adjacent('abcd', 2)) # 'abcd'
print(identify_adjacent('deeedbbcccbdaa', 3)) # 'aa
print(identify_adjacent('pbbcggttciiippooaais', 2)) # 'ps'
print(identify_adjacent('aaabbbacd', 3)) # 'acd