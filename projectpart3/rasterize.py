import numpy as np

def rasterize(pts_2d: np.ndarray, plane_w: int, plane_h: int, res_w: int, res_h: int) -> np.ndarray:
    # Rasterize the incoming 2d points from the camera plane to image pixel coordinates
    #Inputs:
        # pts_2d: 2D points
        # plane_w: width of the camera plane
        # plane_h: height of the camera plane
        # res_w: width of the image
        # res_h: height of the image
    #Outputs:
        # P_rast: 2D points in the rasterized image

    # Remove any points outside of the camera 
    if np.any((pts_2d[0] < -plane_w/2) | (pts_2d[0] > plane_w/2)) or np.any((pts_2d[1] < -plane_h/2) | (pts_2d[1] > plane_h/2)):
        x = np.logical_and(pts_2d[0] >= -plane_w/2, pts_2d[0] <= plane_w/2)
        y = np.logical_and(pts_2d[1] >= -plane_h/2, pts_2d[1] <= plane_h/2)
        final = np.logical_and(x, y)
        print(pts_2d.shape)
        pts_2d = pts_2d[:, final]
        print(pts_2d.shape)

    # Calculate the ratio between the resolution and the plane dimensions
    w_a = [(res_w - 1) / plane_w]
    h_a = [(res_h - 1) / plane_h]
    
    ratio = np.array([w_a, h_a])
    
    # Calculate the offset to center the points
    offset = np.array([[plane_w / 2], [plane_h / 2]])
    
    # Apply the offset and ratio to the 2D points and round the result
    P_rast = np.round((pts_2d + offset) * ratio).astype(int)
  
    return P_rast

