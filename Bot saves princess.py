
def displayPathtoPrincess(n, grid):
    # print all the moves here
    n_grid = []
    c = 0
    for i in grid:
        l = list(i)
        if 'm' in l:
            b_i = c
        if 'p' in l:
            p_i = c
        n_grid.append(l)
        c += 1
    b_j, p_j = n_grid[b_i].index('m'), n_grid[p_i].index('p')
    while b_i != p_i:
        if b_i > p_i:
            print("UP")
            b_i -= 1
        else:
            print("DOWN")
            b_i += 1
    while b_j != p_j:
        if b_j > p_j:
            print("LEFT")
            b_j -= 1
        else:
            print("RIGHT")
            b_j += 1

    # print(n_grid)


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
