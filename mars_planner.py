## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
import search_algorithms

class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, holding_tool=False, charged=False):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_sample = holding_sample
        self.holding_tool = holding_tool
        self.charged=charged
        self.prev = None
        self.depth = 0

    ## you do this.
    def __eq__(self, other):
       return (self.loc == other.loc and
               self.sample_extracted == other.sample_extracted and
               self.holding_sample == other.holding_sample and
               self.holding_tool == other.holding_tool and
               self.charged == other.charged)

    def __repr__(self):
        return (f"Location: {self.loc}".ljust(19, " ") +
                f"Sample Extracted?: {self.sample_extracted}".ljust(26, " ") +
                f"Holding Sample?: {self.holding_sample}".ljust(24, " ") +
                f"Holding Tool?: {self.holding_tool}".ljust(22, " ") +
                f"Charged?: {self.charged}".ljust(17, " ") +
                f"Depth: {self.depth}")

    def __hash__(self):
        return ("%s %s %s %s %s" % (self.loc,
                                     self.sample_extracted,
                                     self.holding_sample,
                                     self.holding_tool,
                                     self.charged)).__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state):
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev = state
    r2.depth += 1
    return r2

def move_to_station(state):
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    r2.depth += 1
    return r2

def move_to_battery(state):
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    r2.depth += 1
    return r2
# add tool functions here

def drop_sample(state):
    r2 = deepcopy(state)
    if state.holding_sample and state.loc == "station":
        r2.holding_sample = False
    r2.prev = state
    r2.depth += 1
    return r2

def charge(state):
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "battery":
        r2.charged = True
    r2.prev = state
    r2.depth += 1
    return r2

def pick_up_tool(state):
    r2 = deepcopy(state)
    if not state.holding_tool and state.loc == "station":
        r2.holding_tool = True
    r2.prev = state
    r2.depth += 1
    return r2

def drop_tool(state):
    r2 = deepcopy(state)
    if state.holding_tool and state.loc == "station":
        r2.holding_tool = False
    r2.prev = state
    r2.depth += 1
    return r2

def use_tool(state):
    r2 = deepcopy(state)
    if state.holding_tool and not state.sample_extracted and state.loc == "sample":
        r2.sample_extracted = True
        r2.holding_sample = True
    r2.prev = state
    r2.depth += 1
    return r2


action_list = [charge, drop_sample,
               pick_up_tool, drop_tool, use_tool,
               move_to_sample, move_to_battery, move_to_station]

def battery_goal(state):
    return state.loc == "battery"

def move_to_sample(state):
    return (state.loc == "sample" and
            state.holding_tool)

def remove_sample(state):
    return (state.loc == "sample" and
            state.holding_sample and
            state.sample_extracted)

def return_to_charger(state):
    return state.loc == "battery"

def mission_complete(state):
    return (state.loc == "battery" and
            state.charged and
            state.sample_extracted and
            not state.holding_sample)


if __name__=="__main__":
    s = RoverState()
    result = search_algorithms.breadth_first_search(s, action_list, mission_complete )[0]
#    result = search_algorithms.breadth_first_search(result, action_list, remove_sample)[0]
#    result = search_algorithms.breadth_first_search(result, action_list, mission_complete)[0]
    print(result)



