#Sum of Pairs

#Example
l5= [10, 5, 2, 3, 7, 5]
p=10

def sum_pairs(ints, s):
    for i in range(len(ints)):
        for j in range(len(ints)):
            if i != j:
                sum = ints[i] + ints[j]
                if sum == s:
                    min = j-i
                    if
                    ans = [ints[i], ints[j]]
                    return ans


print(sum_pairs(l5,p))
