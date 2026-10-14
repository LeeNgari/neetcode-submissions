class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap={i:[] for i in range(numCourses)}
        result = []
        for crs,pre in prerequisites:
            premap[crs].append(pre)

        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for cour in premap[course]:
                if not dfs(cour):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []
        

        return result