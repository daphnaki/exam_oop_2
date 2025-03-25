from typing import List

def find_unique(lst: List):
    for i in range(0, len(lst) - 1, 2):
        if lst[i] != lst[i + 1]:
            return lst[i]
    return lst[-1]


if __name__ == '__main__':
    lst1 = [1,1,10,10,9,9,5,5,6,8,8]
    print(find_unique(lst1))
    lst2 = [1,3,3]
    print(find_unique(lst2))
    lst3 = [9, 9, 4]
    print(find_unique(lst3))
