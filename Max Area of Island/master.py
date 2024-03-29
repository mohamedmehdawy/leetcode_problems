class Solution:
    def __init__(self):
        self.areas = []
    def checkPos(self, pos): # O(n)
        """
            this function check if pos found in areas
            parametrs:
                pos: the current pos
            return: boolean value of status of pos in areas and current area
        """
        for area in range(len(self.areas)):
            for ele in self.areas[area]:
                if ele == pos:
                    return True, area
        return False, -1
    def mixAreas(self, pos):
        """
            this function mix areas if element found in not current area
            parameters: 
                pos: position of current element
            
        """
        pass
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        one_pos = []
        # get the pos of all one
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    one_pos.append((row, column))
        # here should use while insted of for loop
        for i in range(len(one_pos)):
            # area
            area = []
            # check if current element found in any area access this area
            check_area, area_index = self.checkPos(one_pos[i])
            if check_area:
                area = self.areas[area_index]
            else:
                area.append(one_pos[i])
            # the counts for each position
            right_count = 1
            left_count = 1
            top_count = 1
            bottom_count = 1

            for j in range(len(one_pos)):
                # check for x-aixs position
                if one_pos[i][0] == one_pos[j][0]:
                    # check for right position
                    if one_pos[i][1] == one_pos[j][1] - right_count:
                        check_area_status, area_index = self.checkPos(one_pos[j])
                        if check_area_status and self.areas[area_index] != area:
                            for ele in self.areas[area_index]:
                                area.append(ele)
                            self.areas.remove(self.areas[area_index])
                            right_count += 1
                        if not self.checkPos(one_pos[j])[0]:
                            
                            area.append(one_pos[j])
                            right_count += 1
                    # check for right position
                    elif one_pos[i][1] == one_pos[j][1] + left_count:
                        check_area_status, area_index = self.checkPos(one_pos[j])
                        if check_area_status and self.areas[area_index] != area:
                            for ele in self.areas[area_index]:
                                area.append(ele)
                            self.areas.remove(self.areas[area_index])
                            left_count += 1
                        if not self.checkPos(one_pos[j])[0]:
                            area.append(one_pos[j])
                            left_count += 1
                # check for y-axis position
                elif one_pos[i][1] == one_pos[j][1]:
                    # check for top position
                    if one_pos[i][0] == one_pos[j][0] + top_count:
                        check_area_status, area_index = self.checkPos(one_pos[j])
                        if check_area_status and self.areas[area_index] != area:
                            for ele in self.areas[area_index]:
                                area.append(ele)
                            self.areas.remove(self.areas[area_index])
                            top_count += 1
                        if not self.checkPos(one_pos[j])[0]:
                            area.append(one_pos[j])
                            top_count += 1
                    # check for top position
                    elif one_pos[i][0] == one_pos[j][0] - bottom_count:
                        check_area_status, area_index = self.checkPos(one_pos[j])
                        if check_area_status and self.areas[area_index] != area:
                            for ele in self.areas[area_index]:
                                area.append(ele)
                            self.areas.remove(self.areas[area_index])
                            bottom_count += 1
                        if not self.checkPos(one_pos[j])[0]:
                            area.append(one_pos[j])
                            bottom_count += 1
            # if this is new area append to areas
            if not check_area:
                self.areas.append(area)
        return len(self.areas)
obj = Solution()

obj.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])