def vector_interp(p1, p2, V1, V2, coord, dim):
    #function for performing linear interpolation between two points
    if dim==1:  # Check if horizontal interpolation (x)
        if p1[0]==p2[0]:  # Check if x-coordinates of points are equal
            V=(V1+V2)/2  
        else:
            V= V1+(coord-p1[0])*(V2-V1)/(p2[0]-p1[0])  # Perform linear interpolation for x-coordinate

    elif dim==2:  # Check if vertical interpolation (y)
        if  p1[1]==p2[1]:  # Check if y-coordinates of points are equal
            V=(V1+V2)/2  
        else:
            V= V1+(coord-p1[1])*(V2-V1)/(p2[1]-p1[1])  # Perform linear interpolation for y-coordinate
    return V  
