def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(mat) * len(mat[0]) != r * c:
        return mat
    flat_mat = []
    prop_mat = []
    for i in range(len(mat)):
        for j in mat[i]:
            flat_mat.append(j)
    end = c
    for i in range(0, len(flat_mat), c):
        prop_mat.append(flat_mat[i:end])
        end += c

    return prop_mat

