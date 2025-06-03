from typing import Tuple
import numpy as np
from typing import Tuple

def lookat(eye: np.ndarray, up: np.ndarray, target: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    #Calculates the rotation matrix and eye position for a camera lookat transformation.

    #Inputs:
      # eye (np.ndarray): The center of the camera.
      # up (np.ndarray): The up direction.
      # target (np.ndarray): The target point.
    #Outputs:
      #Tuple[np.ndarray, np.ndarray]: A tuple containing the rotation matrix and the eye position.
    

    # Calculate the forward vector by subtracting the target point from the eye position
    forward = target.T - eye.T
    # Normalize the forward vector to have unit length
    forward = forward/np.linalg.norm(forward)
    
    # Calculate the right vector by subtracting the projection of the up vector onto the forward vector from the up vector
    right = up.T - np.dot(up.T[0],forward[0]) * forward
    # Normalize the right vector to have unit length
    right = right/np.linalg.norm(right)
    
    # Calculate the orthonormal up vector by taking the cross product of the right and forward vectors
    u = np.cross(right[0], forward[0])  
    # Normalize the up vector to have unit length
    u= u / np.linalg.norm(u)
    
    # Construct the rotation matrix by arranging the u, right, and forward vectors as columns
    R = np.array([u, right[0], forward[0]]).T   
    
    # Create a tuple of the rotation matrix R and the eye position
    result_tuple = (R, eye)
    
    # Return the tuple
    return result_tuple

   

