import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0


def play_rules(frameNum, grid, img, N):
    new_grid = grid.copy()
    for y in range(N):
        for x in range(N):
            num_neighbours = int((grid[(y+1) % N, x] + grid[(y-1) % N, x] + grid[y, (x+1) % N] +
                                  grid[y, (x - 1) % N] + grid[(y+1) % N, (x+1) % N] + grid[(y+1) % N, (x-1) % N] +
                                  grid[(y-1) % N, (x+1) % N] + grid[(y-1) % N, (x-1) % N])/255)

            if grid[y][x] == ON:
                if (num_neighbours < 2) or (num_neighbours > 3):
                    new_grid[y][x] = OFF
            else:
                if num_neighbours == 3:
                    new_grid[y][x] = ON

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img


def main():
    N = 100
    updateInterval = 50

    grid = np.zeros((N, N))
    grid.fill(0)
    grid[10][0:100] = ON
    grid[11][10:70] = ON
    grid[12][20-50] = ON
    grid[13][40-45] = ON
    grid[13][41-58] = ON

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, play_rules, fargs=(
        grid, img, N, ), interval=updateInterval, save_count=50)
    plt.show()


if __name__ == '__main__':
    main()
