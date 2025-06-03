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

# Render the image using the 'render_img' module
img = render_img.render_img(faces, vertices, vcolors, depth, 'f')

# Stop measuring the execution time for rendering the image
end = time.time()

# Display the rendered image
plt.imshow(img)
plt.title('Flat Shading')
plt.show()

# Save the rendered image as 'shade_flat.png'
plt2.imsave('shade_flat.png', np.array(img))

