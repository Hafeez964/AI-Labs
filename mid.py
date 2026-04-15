import heapq

graph = {
    'S': [('A', 3), ('B', 6)],
    'A': [('W', 4), ('C', 8)],
    'B': [('W', 3), ('G', 9)],
    'W': [('C', 2), ('G', 10)],
    'C': [('G', 5)],
    'G': []
}


MAX_ARMOR = 20
TIME_LIMIT = 11   

def heuristic(node, visited_w):
    if not visited_w:
        return 10
    return 5

def a_star():
    pq = []
    heapq.heappush(pq, (0, 'S', MAX_ARMOR, 0, False, False, ['S']))

    visited = set()
    nodes_expanded = 0

    while pq:
        f, node, armor, time, visited_w, repaired_b, path = heapq.heappop(pq)
        nodes_expanded += 1

        if armor <= 0:
            continue

        if node == 'G' and visited_w:
            print("Final Path:", " -> ".join(path))
            print("Total Time:", time)
            print("Remaining Armor:", armor)
            print("Nodes Expanded:", nodes_expanded)
            return

        state = (node, visited_w, repaired_b)
        if state in visited:
            continue
        visited.add(state)

        for neighbor, cost in graph[node]:

            
            if node == 'B' and neighbor == 'G' and time >= TIME_LIMIT:
                continue

            new_armor = armor - cost
            new_time = time + cost
            new_visited_w = visited_w or (neighbor == 'W')
            new_repaired_b = repaired_b

            
            if neighbor == 'B' and not repaired_b:
                new_armor = MAX_ARMOR
                new_repaired_b = True

            h = heuristic(neighbor, new_visited_w)
            f_new = new_time + h

            heapq.heappush(
                pq,
                (f_new, neighbor, new_armor, new_time,
                 new_visited_w, new_repaired_b, path + [neighbor])
            )

    print("No solution found")

a_star()