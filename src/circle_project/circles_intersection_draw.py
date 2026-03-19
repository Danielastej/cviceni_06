import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):
    r1 = circle_1["r"]
    x1 = circle_1["x"]
    y1 = circle_1['y']
    r2 = circle_2["r"]
    x2 = circle_2["x"]
    y2 = circle_2['y']

    circle1 = plt.Circle((x1, y1), r1, fill=False, color="blue")
    circle2 =plt.Circle((x2, y2), r2, fill=False, color="red")

    fig, ax = plt.subplots()
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    plt.show()


draw_data({"x": 0, "y": 0, "r": 2}, {"x": 3, "y": 0, "r": 1})