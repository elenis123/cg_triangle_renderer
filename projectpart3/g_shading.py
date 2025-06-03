import numpy as np
import time
import vector_interp

import matplotlib.pyplot as plt


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


def g_shading(img, vertices, vcolors):
    # Perform Gouraud shading on the image using the given vertices and vertex colors
    
    
    p1 = bresenham(vertices[0], vertices[1])# Bresenham's line algorithm for drawing a line between two vertices
    p2 = bresenham(vertices[1], vertices[2])
    p3 = bresenham(vertices[2], vertices[0])

    
    p1 = sorted(p1, key=lambda x: x[0])# Sort the points of the triangle by x-coordinate
    p2 = sorted(p2, key=lambda x: x[0])
    p3 = sorted(p3, key=lambda x: x[0])

    # Convert vertices to list
    vertices_list = vertices.tolist()
    
    # Iterate over the points in p1 and fill in the corresponding colors in the image
    for point in p1:
        if point not in vertices_list:
            if abs(vertices[0][0] - vertices[1][0]) > abs(vertices[0][1] - vertices[1][1]):
                img[point[1]][point[0]] = vector_interp.vector_interp(vertices[0], vertices[1], vcolors[0], vcolors[1], point[0], 1)
            else:
                img[point[1]][point[0]] = vector_interp.vector_interp(vertices[0], vertices[1], vcolors[0], vcolors[1], point[1], 2)
        else:
            index = vertices_list.index(point) if point in vertices_list else vertices.index(point)
            img[point[1]][point[0]] = vcolors[index]

    # Repeat the same process for p2 and p3
    for point in p2:
        if point not in vertices_list:
            if abs(vertices[1][0] - vertices[2][0]) > abs(vertices[1][1] - vertices[2][1]):
                img[point[1]] [point[0]] = vector_interp.vector_interp(vertices[1], vertices[2], vcolors[1], vcolors[2], point[0], 1)
            else:
                img[point[1]] [point[0]] = vector_interp.vector_interp(vertices[1], vertices[2], vcolors[1], vcolors[2], point[1], 2)
        else:
            index = vertices_list.index(point) if point in vertices_list else vertices.index(point)
            img[point[1]] [point[0]] = vcolors[index]

    for point in p3:
        if point not in vertices_list:
            if abs(vertices[2][0] - vertices[0][0]) > abs(vertices[2][1] - vertices[0][1]):
                img[point[1]] [point[0]] = vector_interp.vector_interp(vertices[2], vertices[0], vcolors[2], vcolors[0], point[0], 1)
            else:
                img[point[1]] [point[0]] = vector_interp.vector_interp(vertices[2], vertices[0], vcolors[2], vcolors[0], point[1], 2)
        else:
            index = vertices_list.index(point) if point in vertices_list else vertices.index(point)           
            img[point[1]][point[0]] = vcolors[index]

    
    fisrt_scan = min(p1[0][0], p2[0][0], p3[0][0])#first scan line according to the value of first point of each side
    last_scan = max(p1[-1][0], p2[-1][0], p3[-1][0])#last scan line according to the value of last point of each side

    # Iterate over the scan lines
    for scan in range(fisrt_scan, last_scan + 1):
        active_points = []
        # Find the active points on the current scan line
        for point in p1:
            if point[0] == scan:
                active_points.append(point)
        for point in p2:
            if point[0] == scan:
                active_points.append(point)
        for point in p3:
            if point[0] == scan:
                active_points.append(point)
        if len(active_points) == 0:
            continue
        else:
            min_active_points = np.array(active_points).min(axis=0)[1]#min value of columns of active points
            max_active_points = np.array(active_points).max(axis=0)[1]#max value of columns of active points

        for i in range(min_active_points+1, max_active_points):
            if [i,scan] in active_points:
                continue
            else:
                # Interpolate the color for the current pixel
                img[i,scan] = vector_interp.vector_interp([min_active_points,scan], [max_active_points,scan], img[min_active_points][scan], img[max_active_points][scan], i, 1)

    return img


