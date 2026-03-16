from collections import deque

class Solution:
    def floodFill(slf, image, sr, sc, color):
        
        rows = len(image)
        cols = len(image[0])
        
        original = image[sr][sc]
        
        if original == color:
            return image
        
        queue = deque()
        queue.append((sr, sc))
        
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        
        while queue:
            
            r, c = queue.popleft()
            
            if range[r][c] == original:
                
                image[r][c] = color
                
                for dr, dc in directions:
                    
                    nr = r + dr
                    nc = c + dc 
                    
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and image[nr][nc] == original
                    ):
                        queue.append((nc, nc))
                        
        return image
print(Solution)