class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        if m == 1 and n == 1:
            return ["."]

        grid = []

        for i in range(m):
            grid.append("#" * n)

        not_complete = True
        starting_x = 0
        starting_y = 0
        while not_complete:
            grid[starting_y] = grid[starting_y][:starting_x] + "." + grid[starting_y][starting_x + 1 :]
            if (n - starting_x) >= (m - starting_y):
                starting_x += 1
            elif (n - starting_x) < (m - starting_y):
                starting_y += 1

            grid[starting_y] = grid[starting_y][:starting_x] + "." + grid[starting_y][starting_x + 1 :]

            if  grid[m - 1][n - 1] == ".":
                not_complete = False
        
        return grid




        