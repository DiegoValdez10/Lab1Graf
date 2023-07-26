from gl import Renderer, V2, color
import shaders

width = 1080
height = 1080

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
    V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)
]

def draw_object(vertices):
    for i in range(len(vertices) - 1):
        rend.glColor(1, 1, 1)
        rend.glLine(vertices[i], vertices[i + 1])

    rend.glColor(1, 1, 1)
    rend.glLine(vertices[-1], vertices[0])

draw_object(vertices_obj1)
draw_object(vertices_obj2)
draw_object(vertices_obj3)
draw_object(vertices_obj4)
draw_object(vertices_obj5)
rend.glRellenar(vertices_obj1)
rend.glRellenar(vertices_obj2)
rend.glRellenar(vertices_obj3)
rend.glRellenar(vertices_obj4)
rend.glRellenar(vertices_obj5)

rend.glRender()
rend.glFinish("output1.bmp")

