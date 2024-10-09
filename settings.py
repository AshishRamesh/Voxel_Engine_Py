from numba import njit
import numpy as np
import glm , math 

WIN_RES = glm.vec2(1280,720)

ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)


BG_COLOR = glm.vec3(0.1, 0.16, 0.25)