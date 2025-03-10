# Medium
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for _ in range(n)] #Initializes empty 2D matrix
        top, left= 0,0
        bottom, right= n - 1, n - 1
        num = 1

        while num<=n*n:
            # Iterates left to right
            for i in range(left, right + 1):
                matrix[top][i]=num
                num += 1
            top += 1

            # Iterates top to bottom
            for i in range(top,bottom + 1):
                matrix[i][right]=num
                num += 1
            right -= 1

            # Iterates right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i]=num
                num += 1
            bottom -= 1

            #Iterates bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left]=num
                num += 1
            left += 1
        return matrix

