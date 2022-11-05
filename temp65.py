def bfs(graph,start):
    queue = []
    visited = set()
    result = []
    queue.append(start)
    visited.add(start)
    while(len(queue) > 0):
        current = queue.pop(0)
        result.append(current)
        for i in graph[current]:
            if(i not in visited):
                queue.append(i)
                visited.add(i)
    return result
        
def dfs(graph,start):
    stack = []
    visited = set()
    result = []
    stack.append(start)
    visited.add(start)
    while(len(stack) > 0):
        current = stack.pop()
        result.append(current)
        for i in graph[current]:
            if(i not in visited):
                stack.append(i)
                visited.add(i)
    return result

graph = {
    'A': ["B", "D", "E"],
    'B': ["A", "C"],
    'C': ["B", "E"],
    'D': ["A", "E"],
    'E': ["A", "D", "F", "C"],
    'F': ["E"]     
}

print(bfs(graph,'A'))
print(dfs(graph,'A'))