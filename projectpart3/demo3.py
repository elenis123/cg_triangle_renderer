import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as plt2
import time
from render_objectnew import render_object

# Load data
data = np.load("h3.npy", allow_pickle=True).tolist()
# print(data)
verts = data['verts']
vertex_colors =  data['vertex_colors']
face_indices = data['face_indices']
cam_eye = data['cam_eye']
cam_up = data['cam_up']
cam_lookat = data['cam_lookat']

ka = data['ka']
kd = data['kd']
ks = data['ks']
n = data['n']
light_positions = data['light_positions']
light_intensities = data['light_intensities']
Ia = data['Ia']

M = data['M']
N = data['N']
W = data['W']
H = data['H']
bg_color = data['bg_color']
focal = data['focal']
# Handle dimensions so that all vectors are 3xN
cam_eye = np.array([cam_eye]).T
cam_up = np.array([cam_up]).T
cam_lookat = np.array([cam_lookat]).T
light_intensities = np.array(light_intensities).T
Ia = np.array([Ia]).T
light_positions = np.array(light_positions)
bg_color = np.array(bg_color)

def render_and_save(shader, light_type, light_positions, light_intensities, filename):
    if light_type == 'ambient':
        ka = np.array(data['ka'])
        kd = np.zeros_like(np.array(data['kd']))
        ks = np.zeros_like(np.array(data['ks']))
    elif light_type == 'diffusion':
        ka = np.zeros_like(np.array(data['ka']))
        kd = np.array(data['kd'])
        ks = np.zeros_like(np.array(data['ks']))
    elif light_type == 'specular':
        ka = np.zeros_like(np.array(data['ka']))
        kd = np.zeros_like(np.array(data['kd']))
        ks = np.array(data['ks'])
    else:
        ka = np.array(data['ka'])
        kd = np.array(data['kd'])
        ks = np.array(data['ks'])
        
    img = render_object(shader, focal, cam_eye, cam_lookat, cam_up, bg_color, M, N, H, W, verts, vertex_colors, face_indices, ka, kd, ks, n, light_positions, light_intensities, Ia)
    plt.imshow(img)
    plt.title(f'{shader.capitalize()} Shading {light_type.capitalize()} Lighting')
    plt.show()
    plt2.imsave(filename, np.array(img))

# Render and save images for each shader type
shaders = ['gouraud', 'phong']
light_types = ['combined', 'ambient', 'diffusion', 'specular']

for shader in shaders:
    for light_type in light_types:
        render_and_save(shader, light_type, light_positions, light_intensities, f'{shader}_{light_type}.png')



print("Program has been exited successfully!")
