import sys
import queue

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
    def __init__(self, id, start_point, end_point, earliest_start, latest_finish):
        self.id = id
        self.start_point = start_point
        self.end_point = end_point
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

    def distance(self):
        return abs(self.start_point[0] - self.end_point[0]) + abs(self.start_point[1] - self.end_point[1])

    def __str__(self):
        return "%s %s %s %s %s" % (self.start_point, self.end_point,
                                self.earliest_start, self.latest_finish,
                                self.distance())


class Car:
    def __init__(self, car_id):
        self.car_id = car_id
        self.routes = []
        self.count = 0

    def add_route(self, route):
        self.routes.append(route)
        self.count += route.distance()

    def __eq__(self, other):
        if self.count == other.count:
            return True

    def __lt__(self, other):
        if self.count < other.count:
            return True

    def __gt__(self, other):
        if self.count > other.count:
            return True

    def __str__(self):
        output = str(len(self.routes))
        for route in self.routes:
            output +=" " + str(route.id)
        return output

routes = []
cars_queue = queue.PriorityQueue()

for i in range(1, F+1):
    cars_queue.put(Car(i))

for i in range(1, N+1):
    input = text[i].split()
    a = int(input[0])
    b = int(input[1])
    x = int(input[2])
    y = int(input[3])
    s = int(input[4])
    f = int(input[5])

    route = Route(i-1, (a,b), (x,y), s, f)
    routes.append(route)


routes.sort(key=lambda x: (x.earliest_start, x.distance()))

for route in routes:
    free_car = cars_queue.get()
    free_car.add_route(route)
    cars_queue.put(free_car)

while not cars_queue.empty():
    print(cars_queue.get())
