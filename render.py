import bpy
import os
#from bpy import context

# Set save path
sce = bpy.context.scene.name

#path = r"E:\Zudrit Studios\Projects\Peter Lloyd Youtube\3 - why learn code\3D-Model-Showcase\CloseUp"
path = r"E:\Zudrit Studios\Projects\_BLRDY_\02_3D_Disney_Style\06_3D_White_Teen_Girl(D)\White Teen Girl (Waitriss)\Rigged\CloseUp"

lst=os.listdir(path)

print(lst)

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
    
    
# Render image through viewport
bpy.ops.render.opengl(write_still=True)
#bpy.ops.render.render(write_still=True)        

    



