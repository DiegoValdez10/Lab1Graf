from gl import Renderer, V2, color
import shaders

width = 500
height = 500

rend = Renderer(width, height)

rend.glClearColor(0, 0, 0)
rend.glClear()

# Obj1
vertices_obj1 = [
    V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345),
    V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385),
    V2(205, 410), V2(193, 383),
]

# Obj2
vertices_obj2 = [
    V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)
]

# Obj3
vertices_obj3 = [
    V2(377, 249), V2(411, 197), V2(436, 249)
]

# Obj4
vertices_obj4 = [
    V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52),
    V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230),
    V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180)
]

# Obj5
vertices_obj5 = [
    V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)from gl import Renderer, V2, color
import shaders

width = 500
height = 500

rend = Renderer(width, height)

rend.glClearColor(0, 0, 0)
rend.glClear()

# Obj1, Obj2, and Obj3 remain unchanged

# Obj4 (external contour)
vertices_obj4_external = [
    V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52),
    V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230),
    V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180)
]

# Obj5 (hole in Obj4)
vertices_obj5 = [
    V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)
]

# Draw function with simple clipping
def draw_object(vertices):
    for i in range(len(vertices) - 1):
        rend.glColor(1, 1, 1)
        rend.glLine(vertices[i], vertices[i + 1])

    rend.glColor(1, 1, 1)
    rend.glLine(vertices[-1], vertices[0])

# Draw objects using the draw_object function
draw_object(vertices_obj1)
draw_object(vertices_obj2)
draw_object(vertices_obj3)

# Draw Obj4 (external contour)
draw_object(vertices_obj4_external)

# Draw Obj5 (hole in Obj4)
draw_object(vertices_obj5)

rend.glRender()
rend.glFinish("output1.bmp")

]

# Draw function with clipping
def draw_object(vertices):
    for i in range(len(vertices) - 1):
        start = vertices[i]
        end = vertices[i + 1]
        if not is_inside(start) and not is_inside(end):
            continue
        start, end = clip_line(start, end)
        if start is not None and end is not None:
            rend.glColor(1, 1, 1)
            rend.glLine(start, end)

    if is_inside(vertices[0]):
        start = vertices[-1]
        end = vertices[0]
        if is_inside(end):
            start, end = clip_line(start, end)
            if start is not None and end is not None:
                rend.glColor(1, 1, 1)
                rend.glLine(start, end)

def is_inside(point):
    # Simple bounding box check for clipping
    return 0 <= point.x < width and 0 <= point.y < height

def clip_line(start, end):
    # Simple Cohen-Sutherland Line Clipping algorithm
    # (https://en.wikipedia.org/wiki/Cohen%E2%80%93Sutherland_algorithm)
    x_min, y_min = 0, 0
    x_max, y_max = width - 1, height - 1

    code_start = compute_outcode(start, x_min, y_min, x_max, y_max)
    code_end = compute_outcode(end, x_min, y_min, x_max, y_max)

    while True:
        if not (code_start | code_end):
            # Both points inside the window
            return start, end

        if code_start & code_end:
            # Both points outside the window and on the same side of the window
            return None, None

        # One of the points is outside the window, clip the line
        code = code_start if code_start else code_end
        x, y = start.x, start.y

        if code & 0b1000:  # Top
            x += (end.x - start.x) * (y_max - y) // (end.y - start.y)
            y = y_max
        elif code & 0b0100:  # Bottom
            x += (end.x - start.x) * (y_min - y) // (end.y - start.y)
            y = y_min
        elif code & 0b0010:  # Right
            y += (end.y - start.y) * (x_max - x) // (end.x - start.x)
            x = x_max
        elif code & 0b0001:  # Left
            y += (end.y - start.y) * (x_min - x) // (end.x - start.x)
            x = x_min

        if code == code_start:
            start = V2(x, y)
            code_start = compute_outcode(start, x_min, y_min, x_max, y_max)
        else:
            end = V2(x, y)
            code_end = compute_outcode(end, x_min, y_min, x_max, y_max)

def compute_outcode(point, x_min, y_min, x_max, y_max):
    code = 0
    if point.x < x_min:
        code |= 0b0001  # Left
    elif point.x > x_max:
        code |= 0b0010  # Right
    if point.y < y_min:
        code |= 0b0100  # Bottom
    elif point.y > y_max:
        code |= 0b1000  # Top
    return code

# Draw objects using the new draw_object function with clipping
draw_object(vertices_obj1)
draw_object(vertices_obj2)
draw_object(vertices_obj3)
draw_object(vertices_obj4)
draw_object(vertices_obj5)

rend.glRender()
rend.glFinish("output1.bmp")
