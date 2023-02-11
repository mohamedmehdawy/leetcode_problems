class Solution:
    def __init__(self):
        self.areas = []
    def checkPos(self, pos):
        """
            this function check if pos found in areas
            parametrs:
                pos: the current pos
            return: boolean value of status of pos in areas and current area
        """
        for area in range(self.areas):
            for ele in self.areas[area]:
                if ele == pos:
                    return True, area
        return False, -1
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        one_pos = []
        # get the pos of all one
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    one_pos.append((row, column))
        print(one_pos)
        # here should use while insted of for loop
        for i in range(len(one_pos)):
            # append current one to areas
            area = []
            area.append(one_pos[i])
            left_count = 1
            for j in range(len(one_pos)):
                if one_pos[i][0] == one_pos[j][0] and one_pos[i][1] == one_pos[j][1] - left_count:
                    if not self.checkPos(one_pos[j]):
                        area.append(one_pos[j])
                        left_count += 1
            print(f"area is {area}")
            self.areas.append(area)
            print(one_pos)
        print(self.areas)
obj = Solution()

obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0]]) 