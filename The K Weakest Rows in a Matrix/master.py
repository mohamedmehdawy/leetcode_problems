class Solution:
    @staticmethod
    def sort_soliders(soliders: list[int]) -> list[int]:
        

        for i in range(len(soliders)):
            weak = i
            for j in range(i+1, len(soliders)):
                if(soliders[j]["counter"] < soliders[weak]["counter"] or (soliders[j]["counter"] == soliders[weak]["counter"] and soliders[j]["index"] < soliders[weak]["index"])): weak = j
            
            if(weak != i):
                temp_vlaue = soliders[i]
                soliders[i] = soliders[weak]
                soliders[weak] = temp_vlaue

        return soliders
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        soldiers_data = []

        for row in range(len(mat)):
            soldiers_data.append({
                "index": row,
                "counter": 0
            })
            for col in mat[row]:
                if(col == 1): soldiers_data[row]["counter"] += 1
                else: break
        sorted_soliders = self.sort_soliders(soldiers_data)
        return [sorted_soliders[index]["index"] for index in range(k)]


test = Solution()

print(test.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))