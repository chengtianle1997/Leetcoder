
# DFS Solution： Find a cycle in directed graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if numCourses <= 0:
            return True
        
        adj_list = []
        
        # init adjcent list
        for i in range(numCourses):
            adj_list.append([])
        # create adjcent list
        for v in prerequisites:
            course, next_course = v[1], v[0]
            adj_list[course].append(next_course)
        
        # depth-first search
        stack = []
        visited = [0] * (numCourses)
        # status: 0: unvisited, 1: visited, -1: visiting in the current loop
        
        # check each start point
        for i in range(1, numCourses):
            if visited[i] == 0:
                stack.append(i)

            while stack:
                top = stack[-1]
                # when check it, mark it with -1
                visited[top] = -1
                stack_len = len(stack)
                opt_counter = 0
                if len(adj_list[top]) > 0:
                    # push the neighbors into the stack
                    for next_course in adj_list[top]:
                        if visited[next_course] == 0:
                            stack.append(next_course)
                            opt_counter += 1
                        if visited[next_course] == -1:
                            # a cycle found
                            return False
                # if no operations for this node
                if not opt_counter > 0:
                    stack.pop()
                    visited[top] = 1
        
        return True
                
            
                