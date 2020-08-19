class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        r = len(image)
        c = len(image[0])
        
        def dfs(image: List[List[int]], sr: int, sc: int):
            # Bounds check
            if sr < 0 or sr >= r or sc < 0 or sc >= c \
                      or image[sr][sc] == newColor \
                      or image[sr][sc] != oldColor:
                return
            image[sr][sc] = newColor
            dfs(image, sr+1, sc)
            dfs(image, sr-1, sc)
            dfs(image, sr, sc+1)
            dfs(image, sr, sc-1)
        
        dfs(image, sr, sc)
        return image