from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import os
import sys
sys.path.append(f'{os.getcwd()}/projects/graph')
sys.path.append(f'{os.getcwd()}/util')
print(f'{os.getcwd()}')
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open('/Users/scott/dev/lambda/CS/Graphs/projects/adventure/maps/main_maze.txt', "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


graph = {}
opposites = {'n': "s", "s": "n", "w": "e", "e": "w"}
outer_visited = set()

def dfs(starting_vertex):
    starting_vertex = player.current_room.id
    q = Queue()
    q.enqueue([starting_vertex])

    # created a set to store visited vertices
    visited = set()

    # while the queue is not empty
    while q.size() > 0:
        # dequeue the first path
        path = q.dequeue()
        # grab the last vertex from the path
        vertex = path[-1]

        # i think we need to travel to this vertex?
        if vertex not in visited:
            possible_directions = list([k for (k,v) in graph[vertex].items() if v == "?"])
            if len(possible_directions) > 0:
                # we found a place to go back to
                # return path
                # we need to traverse back
                for i in range(len(path) - 1):
                    current = path[i]
                    go_to = path[i + 1]
                    # find our direction
                    directions = graph[current].items()
                    for d in directions:
                        if d[1] == go_to:
                            player.travel(d[0])
                            traversal_path.append(d[0])
                            break
                break
                    

            else:
                visited.add(vertex)
                for vs in graph[vertex].items():
                    new_path = path.copy()
                    new_path.append(vs[1])
                    q.enqueue(new_path)

while len(graph.keys()) < len(room_graph):
    current_room = player.current_room.id

    if current_room not in graph:
        graph[current_room] = { item:"?" for item in player.current_room.get_exits() }

    possible_directions = list([k for (k,v) in graph[player.current_room.id].items() if v == "?"])

    
    if len(possible_directions) > 0:
        for i in range(len(possible_directions)):
            random_direction = possible_directions[i]
            player.travel(random_direction)
            if player.current_room.id in outer_visited:
                next_room = player.current_room.id
                graph[current_room][random_direction] = next_room
                graph[next_room][opposites[random_direction]] = current_room
                player.travel(opposites[random_direction])
                break
            else:
                traversal_path.append(random_direction)
                outer_visited.add(player.current_room.id)
                next_room = player.current_room.id
                graph[next_room] = { item:"?" for item in player.current_room.get_exits() }
                graph[next_room][opposites[random_direction]] = current_room
                graph[current_room][random_direction] = next_room
                break
    else:
        dfs(current_room)
        



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
