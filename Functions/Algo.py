from queue import PriorityQueue
from Constants import WIDTH, HEIGHT, av_width, av_height


def distance(pos1, pos2):
    '''
    Finds the distance between two positions
    :param pos1: tuple of coordinates of the first position
    :param pos2: tuple of coordinates of the second position
    :return: distance integer
    '''
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1-x2)+abs(y1-y2)


def algorithm(start, end, barriers, spots):
    '''
    Finds the shortest path between two given positions
    :param start: tuple of coordinates of the first position
    :param end: tuple of coordinates of the second position
    :param barriers: a list of tuples with the position of each barrier(walls)
    :param spots: list of tuples of all available positions
    :return: list of the best path in order
    '''
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for spot in spots}
    g_score[start] = 0
    f_score = {spot: float("inf") for spot in spots}
    f_score[start] = distance(start, end)
    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        neighbors = get_neighbors(current, barriers)

        print(f'{current} has the following:{neighbors}')

        if current == end:
            return construct_path(came_from, current, start)
        for neighbor in neighbors:
            temp_score = g_score[current] + 1
            if temp_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_score
                f_score[neighbor] = temp_score + distance(neighbor, end)
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)


def get_neighbors(pos, barriers):
    '''
    Gets a list of all neighbors of a given position
    :param pos: a tuple with the number of row and column
    :param barriers: a list of all the positions of the barriers
    :return: returns a list of the neighbors with the column and row of each one
    '''
    neighbors = []
    neighbor_1 = (pos[0]+1, pos[1])
    if neighbor_1 not in barriers and neighbor_1[0] < WIDTH/av_width - 1:
        neighbors.append(neighbor_1)
    neighbor_2 = (pos[0] - 1, pos[1])
    if neighbor_2 not in barriers and neighbor_2[0] > 0:
        neighbors.append(neighbor_2)
    neighbor_3 = (pos[0], pos[1]+1)
    if neighbor_3 not in barriers and neighbor_3[1] < HEIGHT/av_height - 1:
        neighbors.append(neighbor_3)
    neighbor_4 = (pos[0], pos[1]-1)
    if neighbor_4 not in barriers and neighbor_4[1] > 0:
        neighbors.append(neighbor_4)
    return neighbors


def construct_path(came_from, last, start):
    '''
    Called by algorithm function where it returns the best path in a list
    :param came_from: dictionary of every tuple and its origin
    :param last: a tuple with the position of the end of the path
    :param start: a tuple with the position of the start of the path
    :return: list of the path in order from the start to end node
    '''
    path = []
    while last in came_from:
        path.append(last)
        last = came_from[last]
    path.append(start)
    path = path[::-1]
    return path
