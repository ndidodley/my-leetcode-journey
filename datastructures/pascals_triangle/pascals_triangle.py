def generate(numRows: int) -> List[List[int]]:
    res = [[1]] if numRows == 1 else [[1], [1, 1]]
    if numRows == 1:
        return res
    elif numRows == 2:
        return res
    start = 1
    end = 1
    for i in range(numRows - 2):
        i = 0
        j = 1
        temp = [1]
        while i < (len(res[-1]) - 1) and j < len(res[-1]):
            temp.append(res[-1][i] + res[-1][j])
            i += 1
            j += 1
        temp.append(1)
        res.append(temp)
    return res
