# Finds array indices of values that add up to target value
def ind_to_target(array, target):
    indices = []
    for i in range(len(array)):
        if len(indices) > 0: break
        for j in range(len(array)):
                if array[i]+array[j] == target and i != j:
                    indices.append(i)
                    indices.append(j)
                    break
    return indices


def main():
    nums = [3, 3, 4, 23, 6, 6, 3, 2]
    target = 25
    sol = ind_to_target(nums, target)
    print(sol)


if __name__ == "__main__":
    main()