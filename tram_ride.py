
def min_travel_cost(N,start,finish,ticket_cost):    # N = no. of stations
    if start == finish:
        return 0

    #  adjust the index according to the stations there cant be station 0 - 1 therefore 
    start -= 1
    finish -= 1

    # minimum clockwise cost:
    i = start      # if start is station 1 it will be converted to index 0
    cw_cost = 0    # at start ticket cost will be 0    eg: ticket_cost = [5,10,15,20]  start = 1   finish = 2         
    while i != finish:     
        cw_cost += ticket_cost[i]    # from station 1 - 2  cw_cost = {staion[1] or ticket_cost[0]} + cw_cost = 5 + 0 = 5 
        i = (i + 1) % N    # move one step forwward

    # for minimum anti-clockwise cost:
    i = start
    ac_cost = 0
    while i != finish:
        i = (i - 1 + N) % N     # move one step backward
        ac_cost += ticket_cost[i]

    return min(cw_cost,ac_cost)

N = 4
ticket_cost = [5, 10, 15, 20]   # station1 to station 2 = 5/-
start = 3
finish = 2

print(min_travel_cost(N, start, finish, ticket_cost))


