import bpy
import math

#Deselect anything else
bpy.ops.object.select_all(action='DESELECT')

#Select the Camera.
bpy.data.objects['Camera'].select_set(True)

#Reset all camera location to 0
bpy.ops.object.location_clear(clear_delta=False)
bpy.ops.object.rotation_clear(clear_delta=False)
bpy.ops.object.scale_clear(clear_delta=False)


# Rotate 90 
bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


# Move on Y
bpy.ops.transform.translate(value=(-0, -9.03681, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

# Change Output data
#bpy.context.scene.render.filepath = "//Render/Preview_"


# Good info @ https://www.youtube.com/watch?v=_vbod5s_EmQ 5:25
# TODO:
# Idea Later Check main object , select it, add acamera contstraint, that tracks to the object
# Create emthy obect that tracks the height, so we put it top, middle, bottom. 
