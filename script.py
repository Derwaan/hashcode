import sys

text = []

for line in open(sys.argv[1], 'r').readlines():
    text.append(line)

input = text[0].split()

R = int(input[0])
C = int(input[1])
F = int(input[2])
N = int(input[3])
B = int(input[4])
T = int(input[5])


class Route:
    def __init__(self, start_point, end_point, earliest_start, latest_finish):
        self.start_point = start_point
        self.end_point = end_point
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

routes = []

for i in range(1, N+1):
    input = text[i].split()
    a = input[0]
    b = input[1]
    x = input[2]
    y = input[3]
    s = input[4]
    f = input[5]

    route = Route((a,b), (x,y), s, f)
    routes.append(route)

print(routes)
