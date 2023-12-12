class Solution(object):
   def replaceElements(self,arr):
        n = len(arr)
        max_element = -1
        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = max_element
            if temp > max_element:
                max_element = temp
        return arr