class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top,bottom,left,right = 0,len(matrix),0,len(matrix[0])

        while left < right and top < bottom:
            for j in range(left,right):
                result.append(matrix[top][j])
            top += 1
            for i in range(top,bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for j in range(right - 1, left - 1,-1):
                result.append(matrix[bottom - 1][j])
            bottom -= 1
            for i in range(bottom-1,top-1,-1):
                print(i,left)
                result.append(matrix[i][left])
            left += 1
        
        return result


        