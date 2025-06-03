import numpy as np

class Transform:
    #Interface for performing affine transformations
    
    def __init__(self):
        #Initialize a Transform object.
        self.mat = np.eye(4)  # Initialize with identity matrix

    def rotate(self, theta: float, u: np.ndarray) -> None:
        #Rotate the transformation matrix.
        #Input:
            # theta (float): The angle of rotation in radians.
            # u (np.ndarray): The axis of rotation as a 3-element vector.
        #Output:
            # None
        assert len(u) == 3 #u must be a 3-element vector
        
        c = np.cos(theta)
        s = np.sin(theta)
        ux, uy, uz = u
        #construct the rotation matrix
        R = np.array([[c + ux**2 * (1 - c), ux * uy * (1 - c) - uz * s, ux * uz * (1 - c) + uy * s, 0],
                      [uy * ux * (1 - c) + uz * s, c + uy**2 * (1 - c), uy * uz * (1 - c) - ux * s, 0],
                      [uz * ux * (1 - c) - uy * s, uz * uy * (1 - c) + ux * s, c + uz**2 * (1 - c), 0],
                      [0, 0, 0, 1]])
        #update the transformation matrix
        self.mat = np.dot(self.mat, R)

    def translate(self, t: np.ndarray) -> None:
        #Translate the transformation matrix.
        
        #Input:
            #t (np.ndarray): The translation vector as a 3-element vector.
        
        #Output:
            #None
        assert len(t) == 3 #t must be a 3-element vector
        #update the transformation matrix
        self.mat[:3, 3] = np.add(self.mat[:3, 3], t)
        
    def transform_pts(self, pts: np.ndarray) -> np.ndarray:
        #Transform the specified points according to our current matrix.
        
        #Inputs:
            #pts (np.ndarray): The points to be transformed as a 3xN array.
        
        #Outputs:
            #np.ndarray: The transformed points as a 3xN array.
        
        #add a row of ones to the points
        pts_h = np.vstack((pts, np.ones((1, pts.shape[1]))))
        transformed_pts = np.dot(self.mat, pts_h)
        
        return transformed_pts[:3, :]
    
    

