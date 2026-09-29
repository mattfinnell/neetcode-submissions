from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, table = [0] * numCourses, defaultdict(list)
        for course, prereq in prerequisites:
            indegree[prereq] += 1
            table[course].append(prereq)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        finish, output = 0, []
        while queue:
            course = queue.popleft()
            output.append(course)
            finish += 1

            for prereq in table[course]:
                indegree[prereq] -= 1 
                if indegree[prereq] == 0:
                    queue.append(prereq)

        if finish != numCourses:
            return []

        return output[::-1]