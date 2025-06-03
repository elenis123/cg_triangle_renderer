import numpy as np

def world2view(pts: np.ndarray, R: np.ndarray, c0: np.ndarray) -> np.ndarray:
    #Transforms 3D points from world coordinates to view coordinates.

    #Inputs:
        # pts (np.ndarray): Array of shape (3, N).
        # R (np.ndarray): Rotation matrix of shape (3, 3) representing the camera orientation.
        # c0 (np.ndarray): Array of shape (3,) representing the camera coordinates .

    #Output:
        #np.ndarray: Array of shape (3, N) representing the 3D points in view coordinates.
    p = (pts.T - c0.T)

    return np.dot(R.T, p.T)


