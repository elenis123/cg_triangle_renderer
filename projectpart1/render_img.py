import numpy as np
import f_shading
import g_shading
import numpy as np

def render_img(faces, vertices, vcolors, depth, shading):
    # Renders an image based on the given faces, vertices, vertex colors, depth, and shading type.
        # faces (numpy.ndarray): representing the indices of the vertices that form each triangle.
        # vertices (numpy.ndarray): representing the 3D coordinates of the vertices.
        # vcolors (numpy.ndarray): representing the RGB color values of each vertex.
        # depth (numpy.ndarray): representing the depth values of each pixel in the image.
        # shading (str): The type of shading to apply. Valid values are 'f' for flat shading and 'g' for Gouraud shading.
   
    img = np.ones((512, 512, 3)) #white background
    K = faces.shape[0]
    triangle_depth = np.zeros(K)
    
    # Calculate the depth for each triangle
    for i in range(K):
        triangle_depth[i] = np.mean(depth[faces[i, :]])
    
    # Sort the triangles based on depth
    b = np.argsort(triangle_depth)[::-1]
    faces = faces[b, :]
    
    if shading == 'f':
        # Render the image using flat shading for all triangles
        for k in range(K):
            triangle_vertices = vertices[faces[k]]
            triangle_color = vcolors[faces[k]]
            img = f_shading.f_shading(img, triangle_vertices, triangle_color)
            
    elif shading == 'g':
        # Render the image using Gouraud shading for all triangles
        for k in range(K):
            triangle_vertices = vertices[faces[k]]
            triangle_color = vcolors[faces[k]]
            img = g_shading.g_shading(img, triangle_vertices, triangle_color)
    
            
    else:
        raise ValueError('Invalid shading type')
    
    return img