#!/usr/bin/python3
def island_perimeter(grid):
    """Say the perimeter"""
    per = 0
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] is 1:
                per += 4
                if grid[j][i - 1] is 1 and i >= 1:
                    # Left
                    per -= 1
                if grid[j - 1][i] is 1 and j >= 1:
                    # Up
                    per -= 1
                if i + 1 < len(grid[j]) and grid[j][i + 1] is 1:
                    # Right
                    per -= 1
                if j + 1 < len(grid) and grid[j + 1][i] is 1:
                    # Down
                    per -= 1
    return per
