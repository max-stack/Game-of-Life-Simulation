def initialise_state(grid, ON):
    grid.fill(0)
    grid[10][0:100] = ON
    grid[11][10:70] = ON
    grid[12][20-50] = ON
    grid[13][40-45] = ON
    grid[13][41-58] = ON
