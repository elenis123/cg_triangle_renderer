import numpy as np
import time
from transform import Transform
from render_object import render_object

import matplotlib.pyplot as plt
import matplotlib.image as plt_0

# Create three instances of the Transform class
transform0 = Transform()
transform1 = Transform()
transform2 = Transform()

# Load data from 'hw2.npy' file
data = np.load('hw2.npy', allow_pickle=True).item()

# Extract data from the loaded file
v_pos = data['v_pos']
v_clr = data['v_clr']
t_pos_idx = data['t_pos_idx']
eye = data['eye']
target = data['target']
up = data['up']
t_1 = data['t_1']
t_0 = data['t_0']
rot_axis_0 = data['rot_axis_0']
theta_0 = data['theta_0']
plane_w = data['plane_w']
plane_h = data['plane_h']
res_w = data['res_w']
res_h = data['res_h']
focal = data['focal']

# Render the object without any transformations
img = render_object(v_pos, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(1)
plt.imshow(img)
plt.title('Gouraud Shading')
plt.show()
plt_0.imsave('0.jpg', np.array(img))

# Rotate the object by theta_0 degrees around rot_axis_0
transform0.rotate(theta_0, rot_axis_0)
v_pos0 = transform0.transform_pts(v_pos)
img = render_object(v_pos0, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(2)
plt.imshow(img)
plt.title('Gouraud Shading Step theta_0')
plt.show()
plt_0.imsave('1.jpg', np.array(img))

# Translate the object by t_0 units
transform1.translate(t_0)
v_pos1 = transform1.transform_pts(v_pos0)
img = render_object(v_pos1, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(3)
plt.imshow(img)
plt.title('Gouraud Shading Step t_0')
plt.show()
plt_0.imsave('2.jpg', np.array(img))

# Translate the object by t_1 units
transform2.translate(t_1)
v_pos2 = transform2.transform_pts(v_pos1)
img = render_object(v_pos2, v_clr, t_pos_idx, plane_h, plane_w, res_h, res_w, focal, eye, up, target)
plt.figure(4)
plt.imshow(img)
plt.title('Gouraud Shading Step t_1')
plt.show()
plt_0.imsave('3.jpg', np.array(img))

print("Program has been completed!")
