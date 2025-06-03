import numpy as np
from typing import Tuple
from render_img import render_img
from rasterize import rasterize
from lookat import lookat
from perspective_project import perspective_project

import matplotlib.pyplot as plt

def render_object(v_pos: np.ndarray, v_clr: np.ndarray, t_pos_idx: np.ndarray, plane_h: int, plane_w: int, res_h: int, res_w: int, focal: float, eye: np.ndarray, up: np.ndarray, target: np.ndarray) -> np.ndarray:
    #Renders an object using the given parameters.
    #Inputs:
        # v_pos (np.ndarray): Array of vertex positions.
        # v_clr (np.ndarray): Array of vertex colors.
        # t_pos_idx (np.ndarray): Array of triangle position indices.
        # plane_h (int): Height of the plane.
        # plane_w (int): Width of the plane.
        # res_h (int): Height of the resulting image.
        # res_w (int): Width of the resulting image.
        # focal (float): Focal length.
        # eye (np.ndarray): Position of the eye.
        # up (np.ndarray): Up vector.
        # target (np.ndarray): Target position.

    #Outputs:
        #np.ndarray: Rendered image.


    # Calculate the transformation matrix (R) and translation vector (t) using the lookat function
    (R, t) = lookat(eye, up, target)

    # Perform perspective projection on the vertex positions
    (pts_2d, depth) = perspective_project(v_pos, focal, R, t)

    # Rasterize the projected points to obtain the vertices
    vertices = rasterize(pts_2d, plane_w, plane_h, res_w, res_h).T

    # Render the image using the 2D vertices, triangle position indices, vertex colors, and depth
    return render_img(t_pos_idx, vertices, v_clr, depth, 'g')



