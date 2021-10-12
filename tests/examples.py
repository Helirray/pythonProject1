import math


def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(abs((x1 - x2)) ** 2 + abs((y1 - y2)) ** 2)


def get_mid_point(point1, point2):
    return {'x': (point1['x'] + point2['x']) / 2,
            'y': (point1['y'] + point2['y']) / 2
            }


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def make_segment(point1, point2):
    return {"begin_point": point1, "end_point": point2}


def get_begin_point(segment):
    return segment["begin_point"]


def get_end_point(segment):
    return segment["end_point"]


def get_mid_point_of_segment(segment):
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    x = (get_x(begin_point) + get_x(end_point)) / 2
    y = (get_y(begin_point) + get_y(end_point)) / 2

    return make_decart_point(x, y)


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


def get_angle(point):
    return point["angle"]


def get_radius(point):
    return point["radius"]


def get_x1(point):
    return get_radius(point) * math.cos(get_angle(point))


def get_y1(point):
    return get_radius(point) * math.sin(get_angle(point))


def make_rectangle(p, width, height):
    return {'start_point': p,
            'width': width,
            'height': height
            }


def get_start_point(rectangle):
    return rectangle['start_point']


def get_width(rectangle):
    return rectangle['width']


def get_height(rectangle):
    return rectangle['height']












segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
print(get_begin_point(segment))  # (3, 2)
