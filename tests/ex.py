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


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None


def get_right_top(rectangle):
    start_point = get_start_point(rectangle)
    return make_decart_point(start_point['x'] + get_width(rectangle), start_point['y'])


def get_left_bottom(rectangle):
    start_point = get_start_point(rectangle)
    return make_decart_point(start_point['x'], start_point['y'] - get_height(rectangle))


def get_right_bottom(rectangle):
    start_point = get_start_point(rectangle)
    return make_decart_point(start_point['x'] + get_width(rectangle), start_point['y'] - get_height(rectangle))


def contains_origin(rectangle):
    a = get_start_point(rectangle)
    b = get_right_top(rectangle)
    c = get_left_bottom(rectangle)
    d = get_right_bottom(rectangle)
    return get_quadrant(a) == 2 and get_quadrant(d) == 4


def s():
    pass
