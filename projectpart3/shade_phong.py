import numpy as np
import matplotlib.pyplot as plt
import time
from light import light
from vector_interp import vector_interp
def bresenham(vertice1:list, vertice2:list):
    # Bresenham's line algorithm for drawing a line between two vertices
    x1=vertice1[0]
    y1=vertice1[1]
    x2=vertice2[0]
    y2=vertice2[1]
    DeltaX=abs(x2-x1)
    DeltaY=abs(y2-y1)

    x=x1
    y=y1
    m=DeltaY-DeltaX
    if m>0: #check if slope is bigger than 1
        DeltaX,DeltaY=DeltaY,DeltaX #swap x and y coordinates
        x,y=y,x
        x1,y1=y1,x1
        x2,y2=y2,x2

    f=2*DeltaY-DeltaX
    new_coords=[]

    if m>0:
        new_coords.append([y,x])
    else:
        new_coords.append([x,y])
    for i in range(DeltaX): 
        if f>0:
            if y<y2:
                y=y+1
            else:
                y=y-1
            f=f+2*DeltaY-2*DeltaX
        else:
            f=f+2*DeltaY
        if x<x2:
            x=x+1
        else:
            x=x-1
        if m>0:
            new_coords.append([y,x])
        else:
            new_coords.append([x,y])
    return new_coords

def shade_phong(vertsp, vertsn, vertsc, bcoords, campos, ka, kd, ks, n, lpos, lint,lamb, X):
# Inputs:
    # vertsp: 3D coordinates of vertices
    # vertsn: Normal vectors at vertices
    # vertsc: Colors at vertices
    # bcoords: Barycentric coordinates of vertices
    # campos: Camera position
    # ka, kd, ks: Ambient, diffuse, specular coefficients
    # n: Phong exponent
    # lpos: Position of the light source
    # lint: Intensity of the light source
    # lamb: Ambient light intensity
    # X: Result image (numpy array)
# Outputs:
    # Y: Result image with shaded colors

    if vertsp.shape[1] != 2:
        vertsp = vertsp.T
    lint = np.concatenate((lint, lamb), axis=1)
    # Initialize the result image
    Y = X.copy()

    normals = np.zeros(X.shape)
    colors = np.zeros(X.shape)
    for i in range(3):
        x,y = vertsp[i]
        colors[x][y] = vertsc[i]
        normals[x][y] = vertsn[i]

    p = [bresenham(vertsp[i], vertsp[(i + 1) % 3]) for i in range(3)]

    # Color in the edges and vertices
    for i in range(3):
        j = (i + 1) % 3

        if vertsp[i][0] == vertsp[j][0]:
            if not vertsp[i][1] == vertsp[j][1]:
                for x, y in p[i]:
                    for k in range(3):
                        # Interpolate the normals and colors along the edge
                        normals[x][y] = vector_interp(vertsp[i], vertsp[j], vertsn[k][i], vertsn[k][j], y, 2)
                        colors[x][y] = vector_interp(vertsp[i], vertsp[j], vertsc[i][k], vertsc[j][k], y, 2)
                        # Apply lighting model to calculate the final color
                        Y[x][y] = light(bcoords, normals[x][y].reshape((3, 1)), colors[x][y], campos, ka, kd, ks, n,
                                        lpos, lint)
        else:
            for x, y in p[i]:
                for k in range(3):
                    # Interpolate the normals and colors along the edge
                    normals[x][y] = vector_interp(vertsp[i], vertsp[j], vertsn[i][k], vertsn[j][k], x, 1)
                    colors[x][y] = vector_interp(vertsp[i], vertsp[j], vertsc[i][k], vertsc[j][k], x, 1)
                    # Apply lighting model to calculate the final color
                    Y[x][y] = light(bcoords, normals[x][y].reshape((3, 1)), colors[x][y], campos, ka, kd, ks, n,
                                    lpos, lint)

    active_points = np.concatenate(p)

    first_scan = np.min(vertsp[:, 1])
    last_scan = np.max(vertsp[:, 1])

    for y in range(first_scan, last_scan):
        current_points = active_points[active_points[:, 1] == y][:, 0]

        if len(current_points) <= 1:
            continue

        xmin = np.min(current_points)
        xmax = np.max(current_points)
        v1 = colors[xmin, y]
        v2 = colors[xmax, y]
        n1 = normals[xmin, y]
        n2 = normals[xmax, y]
        for x in range(xmin, xmax):
            # Interpolate the normals and colors along the scanline
            normals[x][y] = [vector_interp([xmin, y], [xmax, y], n1[c], n2[c], x, 1) for c in range(3)]
            colors[x][y] = [vector_interp([xmin, y], [xmax, y], v1[c], v2[c], x, 1) for c in range(3)]
            # Apply lighting model to calculate the final color
            Y[x][y] = light(bcoords, normals[x][y].reshape((3, 1)), colors[x][y], campos, ka, kd, ks, n, lpos, lint)

    return Y