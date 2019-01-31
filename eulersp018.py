#!/usr/bin/env python3

# Problem 18:  - https://projecteuler.net/problem=18
# By Matias D. Lee


input_data = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def get_data_struct():
    raw_data = input_data.split()
    data = []
    for line in range(1,16):
        row = []
        offset = int((line * (line + 1)) / 2) - line       
        for pos in range(0,line):
            row.append({
                'cost' : int(raw_data[offset + pos]),
                'max_path_cost' : int(raw_data[offset + pos])
            })
        data.append(row)

    return data

def get_neighbors(x, y):
    """ x/row starts at 0. 

    >>> get_neighbors(1, 0)
    [(0, 0)]

    >>> get_neighbors(1, 1)
    [(0, 0)]

    >>> get_neighbors(2, 0)
    [(1, 0)]

    >>> get_neighbors(2, 1)
    [(1, 0), (1, 1)]

    >>> get_neighbors(2, 2)
    [(1, 1)]

    """
    if y == 0:
        return [(x-1, 0)]
    elif y == x:
        return [(x-1, y-1)]
    else:
        return [(x-1, y-1), (x-1, y)]


def solver(rows_to_considers=15):
    """
    >>> solver(2)
    170

    >>> solver(3)
    221

    """
    ds = get_data_struct()

    for i in range(1, rows_to_considers):
        for j in range(0,i+1):
            neighbors = get_neighbors(i, j)
            new_costs = []
            for prev_i, prev_j in neighbors:
                new_costs.append(
                    ds[i][j]['cost'] + ds[prev_i][prev_j]['max_path_cost']
                )
            ds[i][j]['max_path_cost'] = max(new_costs)
    
    last_row = ds[rows_to_considers-1]
    maxs = [r['max_path_cost'] for r in last_row]
    return max(maxs)

if __name__ == '__main__':
    print(solver())
                