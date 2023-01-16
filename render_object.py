from project_cam_lookat import project_cam_lookat
from rasterize import rasterize
from render import render

def render_object(verts3d,faces,vcolors,imgh,imgw,camh,camw,f,corg,clookat,cup):
    
    shade_t = "gouraud"
    # Take a "photograph" of the object (from 3d space to 2d space)
    verts2d, depth = project_cam_lookat(f,corg,clookat,cup,verts3d)
    # Clipping
    verts2d = rasterize(verts2d,imgh,imgw,camh,camw)
    # Paint the traingles
    I = render(verts2d,faces,vcolors,depth,shade_t)

    return I