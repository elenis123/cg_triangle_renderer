import numpy as np
from typing import Tuple
from world2view import world2view 

def perspective_project(pts: np.ndarray, focal: float, R: np.ndarray, t: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # Projects 3D points to 2D image plane and computes depth.
    #Inputs:
      # pts: 3D points
      # focal: focal length
      # R: rotation matrix
      # t: translation vector
    #Outputs:
      # pts_2d: 2D points
      # depth: depth of 3D points
    
    # Transform points to camera coordinate system
    pts_cam = world2view(pts, R, t)

    # Compute depth
    depth = pts_cam[-1]

    # Project points to 2D image plane
    pts_2d = focal * pts_cam[:2, :] / depth

    # Create a tuple of pts_2d and depth (converted to integer)
    Tuple=(pts_2d,depth.astype(int))

    # Return the tuple
    return Tuple

    
