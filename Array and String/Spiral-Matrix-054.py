# Medium
# Given an m x n matrix, return all elements of the matrix in spiral order.

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])

        result=[]
        top, bottom, right, left = 0, m-1, n-1, 0

        while len(result) <m*n:
            # Iterates left to right
            for i in range(left, right+1):              
                result.append(matrix[top][i])
            top += 1
            
            #Iterates top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            # Iterates right to left if bottom index is lower or equal to top index
            if top <= bottom:
                for i in range(right, left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Iterates bottom to top if right index is righter or equal to left index
            if left <= right:
                for i in range(bottom, top-1,-1):
                    result.append(matrix[i][left])
                left += 1
        return result