import numpy as np

def light(point, normal, vcolor, cam_pos, ka, kd, ks, n, lpos, lint):    
# Calculates the light intensity at a given point on a surface.
# Inputs:
        # point (numpy.ndarray): The coordinates of the point on the surface.
        # normal (numpy.ndarray): The surface normal at the point.
        # vcolor (float): The color of the surface.
        # cam_pos (numpy.ndarray): The position of the camera.
        # ka (float): The ambient reflection coefficient.
        # kd (float): The diffuse reflection coefficient.
        # ks (float): The specular reflection coefficient.
        # n (float): The shininess coefficient.
        # lpos (numpy.ndarray): The positions of the light sources.
        # lint (numpy.ndarray): The intensities of the light sources.    
# Outputs:
        # numpy.ndarray: The total light intensity at the point.
 
    # Initialize the total light
    I = np.zeros((3,3))
    I_ambient = I[0]
    I_diffuse = I[1]
    I_specular = I[2]
    
    # Ambient light component
    lamb = lint[:,-1]
    I_ambient = ka * lamb
    
    # View direction
    V = cam_pos - point
    V = V / np.linalg.norm(V)
    
    # Iterate over each light source
    for i in range(lpos.shape[1]):
        # Light direction
        L = lpos[:,i].reshape((3,1)) - point
        L = L / np.linalg.norm(L)
        
        # Diffuse component
        cosa = np.dot(normal.T[0], L.T[0])
        I_diffuse += kd * lint[:, i] * cosa
        
        # Specular component
        R = 2 * np.dot(normal.T[0], L.T[0]) * normal - L
        R = R / np.linalg.norm(R)
        cosba= np.dot(V.T[0], R.T[0] )
        I_specular += ks * lint[:, i] * (cosba ** n)

    # Clip the intensity values to the range [0, 1]
    I=np.clip(I,0,1)
    I=np.clip(np.sum(I,axis=0)*vcolor,0,1)
    
    return I