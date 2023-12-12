class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, color: int) -> [[int]]:
        visited = set()
        orig = image[sr][sc]

        def dfs(sr,sc):
            if not(-1<sr<len(image)) or not(-1<sc<len(image[0])):
                return
            
            if (sr,sc) in visited:
                return
            
            if image[sr][sc] != orig:
                return

            image[sr][sc] = color
            visited.add((sr,sc))

            dfs(sr-1,sc)
            dfs(sr+1,sc)
            dfs(sr,sc-1)
            dfs(sr,sc+1)
        
        dfs(sr,sc)

        return image

        
        