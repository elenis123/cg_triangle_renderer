import numpy as np
from calculate_normals import calculate_normals
from rasterize import rasterize
from lookat import lookat
from shade_gouraud import shade_gouraud
from shade_phong import shade_phong
from perspective_project import perspective_project

def render_object(shader, focal, eye, lookat_point, up, bg_color, M, N, H, W, verts, vert_colors, faces, ka, kd, ks, n, lpos, lint, lamb):
# Inputs:
        # shader: string, the shading technique to use ('gouraud' or 'phong')
        # focal: float, the focal length of the camera
        # eye: numpy array, the camera's position
        # lookat_point: numpy array, the point the camera is looking at
        # up: numpy array, the upward direction of the camera
        # bg_color: numpy array, the background color of the image
        # M, N, H, W: integers, the size of the image
        # verts: numpy array, the vertices of the object
        # vert_colors: numpy array, the colors of the vertices
        # faces: numpy array, the faces of the object
        # ka, kd, ks: floats, the ambient, diffuse, and specular coefficients
        # n: float, the exponent for the specular term
        # lpos: numpy array, the position of the light source
        # lint: float, the intensity
# Outputs:
        # img: numpy array: the rendered   
   
    #  Calculate the normal vectors
    normals = calculate_normals(verts, faces)  
    #  Project the vertices onto the camera's view plane
    (R,t) = lookat(eye, up, lookat_point)
    (pts_2d_proj, depth) = perspective_project(verts, focal, R, t)
    pts_2d = rasterize(pts_2d_proj, W, H, N, M)
    # Sort the faces based on depth
    new_depth = np.mean(depth[faces.T], axis=1)
    sorted_faces = np.argsort(-new_depth)
    faces = faces[:, sorted_faces]
    #  Create an image with the specified background color
    img = np.ones((M, N, 3)) * bg_color
    # Color the triangles based on the shader
    if shader == 'gouraud':
        for triangle in faces.T:
            verts_idx = pts_2d[:, triangle]
            colors = vert_colors.T[triangle]
            cnormals = normals[:, triangle]
            bcoords = np.mean(verts[:, triangle], axis=1).reshape((3,1))
            img = shade_gouraud(verts_idx, cnormals, colors, bcoords, eye, ka, kd, ks, n, lpos, lint, lamb, img)
                            
    elif shader == 'phong':
        for triangle in faces.T:
            verts_idx = pts_2d[:, triangle]
            colors = vert_colors.T[triangle]
            cnormals = normals[:, triangle]
            bcoords = np.mean(verts[:, triangle], axis=1).reshape((3,1))
            img = shade_phong(verts_idx, cnormals, colors, bcoords, eye, ka, kd, ks, n, lpos, lint, lamb, img)
    
    return img
