class Solution:
    def nextGreatestLetter(self, letters: [str], target: str) -> str:
        left, right = 0, len(letters)-1
        greater = letters[0]

        while left <= right:
            mid = (left + right)//2

            if letters[mid] > target:
                right = mid -1
                greater = letters[mid]
            else:
                left = mid +1
  
        return greater
        

        
        