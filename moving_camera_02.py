import bpy 


#Deselect anything else
bpy.ops.object.select_all(action='DESELECT')

#Select the Camera.
bpy.data.objects['Camera'].select_set(True)