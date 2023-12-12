class Solution(object):
    def validMountainArray(self, arr):
        max_element = max(arr)
        max_position = arr.index(max_element)
        if len(arr) < 3 or max_position == len(arr)-1 or max_position == 0:
            return False
    
        for i in range(max_position):
            if arr[i] >= arr[i+1]:
                return False
        for  j in range(max_position,len(arr)-1):
            if arr[j] <= arr[j+1]:
                return False
    
        return True