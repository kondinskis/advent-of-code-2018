import re
import string
from collections import defaultdict

with open('input.txt', 'r') as f:
    instructions = [x.groups() for x in re.finditer(
        r'^.*([A-Z])+.*([A-Z])+.*$', f.read(), re.MULTILINE)]


graph = defaultdict(list)
restrictions = defaultdict(list)

for instruction in instructions:
    graph[instruction[0]].append(instruction[1])
    graph[instruction[0]].sort(reverse=True)
    restrictions[instruction[1]].append(instruction[0])


non_restricted = [letter for letter in string.ascii_uppercase if len(
    restrictions[letter]) == 0]


def is_step_ready(step, visited):
    for s in restrictions[step]:
        if s not in visited:
            return False
    return True


def dfs(graph, vertex):
    stack = vertex
    stack.sort(reverse=True)
    path = []

    visited = defaultdict(bool)

    while stack:
        v = stack.pop()
        if v not in visited and is_step_ready(v, visited):
            visited[v] = True
            path.append(v)
            stack.extend(graph[v])
            stack.sort(reverse=True)

    return ''.join(path)


first_part = dfs(graph, non_restricted)
print('First part: {0}'.format(first_part))
