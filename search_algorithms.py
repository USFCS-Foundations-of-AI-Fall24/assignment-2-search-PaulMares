from collections import deque

from scipy.constants import sigma


## We will append tuples (state, "action") in the search queue
def breadth_first_search(start_state, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((start_state, ""))
    if use_closed_list :
        closed_list[start_state] = True
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
def depth_first_search(start_state, action_list, goal_test, use_closed_list=True, limit=0) :
    search_queue = deque()
    closed_list = {}
    states = 0

    search_queue.append((start_state, ""))
    if use_closed_list :
        closed_list[start_state] = True
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
        elif next_state[0].depth < limit or limit <= 0:
            successors = next_state[0].successors(action_list)
            if use_closed_list:
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors:
                    closed_list[s[0]] = True
            search_queue.extend(successors)
            states += len(successors)

## add iterative deepening search here
