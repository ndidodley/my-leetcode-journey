def isPossible(target):
    while target != [1]*len(target):
        max_num = target[0]
        min_num = target[0]
        index = 0
        for i in range(len(target)):
            if target[i] >= max_num:
                max_num = target[i]
                index = int(i)
            if target[i] <= min_num:
                min_num = target[i]
            if min_num < 1:
                return False
        others = sum(target) - max_num
        num = max_num - others
        target[index] = num
        if sum(target) == len(target):
            return True
    else:
        return False
