import numpy as np
import time
import render_img

import matplotlib.pyplot as plt
import matplotlib.image as plt2

# Start measuring the execution time for data management
start = time.time()

# Load data from 'hw1.npy' file
data = np.load('hw1.npy', allow_pickle=True).item()

# Extract data from the loaded file
vertices = data['vertices']
faces = data['faces']
vcolors = data['vcolors']
depth = data['depth']

# Stop measuring the execution time for data management
end = time.time()


# Start measuring the execution time for rendering the image
start = time.time()

# Call the render_img function to generate the image
img = render_img.render_img(faces, vertices, vcolors, depth, 'g')

# Stop measuring the execution time for rendering the image
end = time.time()

# Display the image using matplotlib
plt.imshow(img)
plt.title('Gouraud Shading')
plt.show()

# Save the image as 'shade_gouraud.png'
plt2.imsave('shade_gouraud.png', np.array(img))