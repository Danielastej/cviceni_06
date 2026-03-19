def radius_sum(r1, r2):
    soucet = r1 + r2
    return soucet

def euclid_distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d

def has_intersection(circle_1, circle_2):
    r1 = circle_1["r"]
    x1 = circle_1["x"]
    y1 = circle_1['y']
    r2 = circle_2["r"]
    x2 = circle_2["x"]
    y2 = circle_2['y']

    soucet = radius_sum(r1, r2)
    vzdalenost = euclid_distance(x1, y1, x2,y2)
    if soucet >vzdalenost:
        prunik = 0
        is_intersects = False
    elif soucet == vzdalenost:
        prunik = 1
        is_intersects = True
    else:
        prunik = 2
        is_intersects = True

    slovnik = {
        "intersects": is_intersects,
        "intersections_count": prunik,
    }
    return slovnik
