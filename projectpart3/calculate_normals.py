import numpy as np

def calculate_normals(verts, faces):
# Inputs:
        # verts (np.ndarray): Array of shape (3, N) representing the 3D vertices.
        # faces (np.ndarray): Array of shape (3, M) representing the faces of the mesh.
# Outputs: 
        # normals (np.ndarray): Array of shape (3, N) representing the normals for each vertex.

    # Number of vertices
    Nv = verts.shape[1]
    # Number of faces
    Nf = faces.shape[1] 
    
    # Initialize the normals array
    normals = np.zeros(verts.shape)
    
    for triangle in range(faces.shape[1]):
        # Get the indices of the vertices for the current triangle
        n1, n2, n3 = faces[:, triangle]
        # Get the coordinates of the vertices for the current triangle
        A, B, C = verts.T[faces[:,triangle]]
        # Compute the edge vectors
        AB = B - A
        BC = C - B 
        # Compute the normal for the triangle using the cross product
        ABxBC = np.cross(AB, BC)
        
        if not np.all(ABxBC == 0):
            # Add the normal to each vertex of the triangle
            normals[:, n1] += ABxBC
            normals[:, n2] += ABxBC
            normals[:, n3] += ABxBC

    # Normalize the normals for each vertex
    for i in range(verts.shape[1]):
        norm = np.linalg.norm(normals[:, i])
        if norm != 0:
            normals[:, i] /= norm
    
    return normals
