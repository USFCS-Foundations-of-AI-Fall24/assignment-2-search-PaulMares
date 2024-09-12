from collections import deque

from scipy.constants import sigma


## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            print("Goal found")
            ptr = next_state[0]
            while ptr is not None :
                print(ptr)
                ptr = ptr.prev
            print(f"Generated {states} states")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            states += len(successors)

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True, limit=0) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        if goal_test(next_state[0]):
            print("Goal found")
            ptr = next_state[0]
            while ptr is not None:
                print(ptr)
                ptr = ptr.prev
            print(f"Generated {states} states")
            return next_state
        elif next_state[0].depth <= limit or limit <= 0:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors
                                    if item[0] not in closed_list]

                for item in successors:
                    if any(item[0] is key or item[0] == key for key in closed_list):
                        print(item[0])
                        print(any(key if key == item[0] else None for key in closed_list))
                        print(item[0] in closed_list)
                        print()
                for s in successors:
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            states += len(successors)

## add iterative deepening search here
