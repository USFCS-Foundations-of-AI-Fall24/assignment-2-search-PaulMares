from queue import PriorityQueue
from math import sqrt
from Graph import Graph, Edge

class map_state():
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location:str="1,1", mars_graph:Graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "%s (%d %d)" % (self.location, self.g, self.h)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == "1,1"


def a_star(start_state:map_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    search_queue.put(start_state)
    state = start_state
    closed_list = {start_state: True}
    states_count = 1

    while search_queue.qsize() > 0 and not test_goal(state):
        state = search_queue.get()
        for i in state.mars_graph.get_edges(state.location):
            new_state = map_state(i.dest, state.mars_graph, prev_state=state, g=(state.g + i.val), h=heuristic_fn(i.dest))
            if use_closed_list:
                if new_state not in closed_list:
                    closed_list[new_state] = True
                else:
                    continue
            search_queue.put(new_state)
            states_count += 1

    print("States generated: %d" % states_count)

    return state if test_goal(state) else None


def str_to_loc(str_loc):
    return int(str_loc[0]), int(str_loc[2])

def loc_to_str(loc):
    return "%d,%d" % (loc[0], loc[1])

## default heuristic - we can use this to implement uniform cost search
def h1(state):
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state:str) -> int:
    loc = str_to_loc(state)
    return int(sqrt((loc[0]-1)**2 + (loc[1]-1)**2))

def test_goal(state):
    return state.is_goal()

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()
    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            locs = lines[i].split()
            start = locs[0][0:3]
            graph.add_node(start)
            for j in range(1, len(locs)):
                graph.add_edge(Edge(start, locs[j]))
    return graph

if __name__ == "__main__":
    full_graph = read_mars_graph("marsMap.txt")
    init_state = map_state(location="8,8", mars_graph=full_graph, h=sld("8,8"))
    end_state = a_star(init_state, sld, test_goal, True)
    while end_state is not None:
        print(end_state)
        end_state = end_state.prev_state