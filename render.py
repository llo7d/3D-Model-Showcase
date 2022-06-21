import bpy
from bpy import context

# Set save path
sce = bpy.context.scene.name

# Brakes if we have more then one images, so needs to be a for loop in the future.
bpy.data.scenes[sce].render.filepath = "//CloseUp/image" 

# Go into camera-view
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        area.spaces[0].region_3d.view_perspective = 'CAMERA'
        break

#TODO: 
# Toggle the viewport shading modes 
# Try to also "Render" not just viewport Render.
bpy.data.objects['Camera'].data.show_wire = True

# Render image through viewport
bpy.ops.render.opengl(write_still=True)
        

    



