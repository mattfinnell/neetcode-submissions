class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for a, b in prerequisites:
            courses[b].append(a)

        def dfs(graph, current, visited) -> bool:
            if current in visited:
                return False

            visited.add(current)

            if not all([dfs(graph, next_course, visited) for next_course in graph.get(current, [])]):
                return False

            visited.remove(current)

            return True

        for course in courses:
            visited = set()

            if not dfs(courses, course, visited):
                return False

        return True