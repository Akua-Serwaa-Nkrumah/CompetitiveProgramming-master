class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        mx = arr[-1]

        for i in range(len(arr)-1,0,-1):
            if arr[i] < arr[i-1]:
                break
        
        mx = 0
        mx_j = i-1

        for j in range(i,len(arr)):
            if arr[j] < arr[i-1]:
                if mx != max(mx,arr[j]):
                    mx = max(mx,arr[j])
                    mx_j = j

        arr[i-1],arr[mx_j] = arr[mx_j],arr[i-1]

        return arr
