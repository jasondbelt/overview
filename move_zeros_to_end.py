"""
Move all zeros to the end of an array while maintaining the order of the other elements. Given an array of integers, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.
"""
def move_zeros_to_end(arr: list[int]) -> list[int]:
    # If array's length is less than 2, return arr
    if len(arr) < 2:
        return arr

    # keep track of current position to insert non-zero elements
    counter = 0

    # Iterate through each element of the array using enumerate, which provides both the index and the value
    for idx, val in enumerate(arr):
        # for nonzero values, move it to the position indicated by 'counter' and increment 'counter' by 1
        if val != 0:
            arr[counter] = val
            counter += 1

    # fill remaining positions in the array with zeros by continuing to increment 'counter' until it reaches the length of the array
    while counter < len(arr):
        arr[counter] = 0
        counter += 1

    # Return the modified array
    return arr


print(move_zeros_to_end([0,1,0,3,12])) # [1,3,12,0,0]
print(move_zeros_to_end([1,2,0,4,3,0,5,0])) # [1,2,4,3,5,0,0,0]
print(move_zeros_to_end([1])) # [1]
print(move_zeros_to_end([0,0,1])) # [1,0,0]