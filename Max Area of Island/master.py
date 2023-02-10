class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        one_pos = []
        areas = []
        # get the pos of all one
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    one_pos.append((row, column))
        print(one_pos)
        # here should use while insted of for loop
        for i in range(len(one_pos)):
            # append current one to areas
            areas.append([one_pos[0]])
            for j in range(1, len(one_pos)):
                if one_pos[0][0] == one_pos[j][0] and one_pos[0][1] == one_pos[j][1] - 1:
                    areas[i].append(one_pos[j])

            for j in range(len(areas[i])):
                one_pos.remove(areas[i][j])
            print(one_pos)
        print(areas)
obj = Solution()

obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0]])