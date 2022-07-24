def search_matrix(matrix, target):
    for i in matrix:
        start = 0
        end = len(i) - 1
        while start <= end:
            mid = (start + end) // 2
            if i[mid] == target:
                return True
            elif target < i[mid]:
                end = mid - 1
            elif target > i[mid]:
                start = mid + 1

    return False

def search_matrix2(matrix, target):
    m = len(mat)
    n = len(mat[0])

    i = m - 1
    j = 0

    while i >= 0 and j < n:
        if mat[i][j] == target:
            return True
        elif mat[i][j] < target:
            j += 1
        else:
            i -= 1

    return False