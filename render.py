import bpy
import os
from bpy import context

# Set save path
sce = bpy.context.scene.name

path = r"E:\Zudrit Studios\Projects\Peter Lloyd Youtube\3 - why learn code\3D-Model-Showcase\CloseUp"

lst=os.listdir(path)

file_number = 0 

# Inscrease file_number based on last rendered file.
for i in lst:
    if int(i[3:-4]) <= file_number:
        file_number += 1
        
    

#print(lst)

# Brakes if we have more then one images, so needs to be a for loop in the future.
bpy.data.scenes[sce].render.filepath = "//CloseUp/cl_" + str(file_number) 

# Go into camera-view
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        area.spaces[0].region_3d.view_perspective = 'CAMERA'
        area.spaces[0].shading.type = 'MATERIAL'

        break
    
#TODO: 
# Toggle the viewport shading modes 
# Try to also "Render" not just viewport Render.
# bpy.data.objects['Camera'].data.show_wire = True

# Render image through viewport
bpy.ops.render.opengl(write_still=True)
        

    



