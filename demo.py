import numpy as np
from affine_transform import affine_transform
from render_object import render_object
import matplotlib.pyplot as plt
import matplotlib

imgw = 512
imgh = 512
camw = 15
camh = 15
f = 70 

# Load data
data = np.load("hw2.npy", allow_pickle=True)
verts3d = data[()]['verts3d']
vcolors = data[()]['vcolors']
faces = data[()]['faces']
corg = data[()]['c_org']
clookat = data[()]['c_lookat']
cup = data[()]['c_up']
t_1 = data[()]['t_1']
t_2 = data[()]['t_2']
u = data[()]['u']
phi = data[()]['phi']

# Reshape data 
verts3d = np.transpose(verts3d)
vcolors = np.transpose(vcolors)
faces = np.transpose(faces)
corg = corg.reshape((3,1))
clookat = clookat.reshape((3,1))
corg = corg.reshape((3,1))
cup = cup.reshape((3,1))
t_1 = t_1.reshape((3,1))
t_2 = t_2.reshape((3,1))
u = u.reshape((3,1))

# 1st photo
I1 = render_object(verts3d,faces,vcolors,imgh,imgw,camh,camw,f,corg,clookat,cup)
matplotlib.image.imsave('I1.png', I1)

# 2nd photo
verts3d = affine_transform(verts3d,0,u,t_1)
I2 = render_object(verts3d,faces,vcolors,imgh,imgw,camh,camw,f,corg,clookat,cup)
matplotlib.image.imsave('I2.png', I2)

# 3rd photo
verts3d = affine_transform(verts3d,phi,u,np.zeros((3,1)))
I3 = render_object(verts3d,faces,vcolors,imgh,imgw,camh,camw,f,corg,clookat,cup)
matplotlib.image.imsave('I3.png', I3)

# 4th photo
verts3d = affine_transform(verts3d,0,u,t_2)
I4 = render_object(verts3d,faces,vcolors,imgh,imgw,camh,camw,f,corg,clookat,cup)
matplotlib.image.imsave('I4.png', I4)

# Below all the 4 images are plotted together
I = np.array([I1,I1,I2,I3,I4])
fig = plt.figure(figsize=(2,2))
for i in range(1,5):
    fig.add_subplot(2,2,i)
    plt.xlim([0, 512])
    plt.ylim([0, 512])
    plt.imshow(I[i])
plt.show()
