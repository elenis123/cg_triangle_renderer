import numpy as np
from light import light 
from g_shading import g_shading 

def shade_gouraud(vertsp, vertsn, vertsc, bcoords, cam_pos, ka, kd, ks, n, lpos, lint, lamb, X):
# Inputs: 
        # vertsp: numpy.ndarray, the vertices of the triangle  
        # vertsn: numpy.ndarray, the normals of the vertices
        # vertsc: numpy.ndarray, the colors of the vertices
        # bcoords: numpy.ndarray, the barycentric coordinates of the triangle
        # cam_pos: numpy.ndarray, the position of the camera
        # ka: numpy.ndarray, the ambient reflection coefficient
        # kd: numpy.ndarray, the diffuse reflection coefficient
        # ks: numpy.ndarray, the specular reflection coefficient
        # n: numpy.ndarray, the shininess coefficient
        # lpos: numpy.ndarray, the positions of the light sources
        # lint: numpy.ndarray, the intensities of the light sources
        # lamb: numpy.ndarray, the ambient light intensity
        # X: numpy.ndarray, the image to be shaded
#  Outputs:
        # Y: numpy.ndarray, the shaded image 
    
    
    color = np.zeros((3,3))  # Initialize an array to store the colors
    
    lint = np.concatenate((lint, lamb), axis=1)  # Concatenate the light intensity and ambient light
    
    # Calculate the color for each vertex
    for i in range(3):
        vertex_color = vertsc[i]  # Get the color of the vertex
        normal = vertsn[:, i].reshape((3, 1))  # Get the normal vector of the vertex
        color[i] = light(bcoords, normal, vertex_color, cam_pos, ka, kd, ks, n, lpos, lint)  # Calculate the light intensity for the vertex
  
    # Apply Gouraud shading to the given vertices
    if vertsp.shape[1] != 2:
        vertsp = vertsp.T  # Transpose the vertex positions if necessary
    Y = g_shading(X, vertsp, color)  # Apply Gouraud shading to the given vertices and colors
    return Y  # Return the shaded image


