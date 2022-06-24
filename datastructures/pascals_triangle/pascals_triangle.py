def generate(numRows: int) -> List[List[int]]:
    res = [[1]] if numRows == 1 else [[1], [1, 1]]
    if numRows == 1:
        return res
    elif numRows == 2:
        return res
    for i in range(numRows - 2):
        x = 0
        y = 1
        temp = [1]
        while x < (len(res[-1]) - 1) and y < len(res[-1]):
            temp.append(res[-1][x] + res[-1][y])
            x += 1
            y += 1
        temp.append(1)
        res.append(temp)
    return res
