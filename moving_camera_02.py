import bpy 


#Deselect all
bpy.ops.object.select_all(action='DESELECT')

# Check if we alrdy have a target, if not, create it.
def create_target():
    
    objects = bpy.context.scene.objects

    for obj in objects:
        if obj.type == "EMPTY":
            print("bingo")
            return False
            break;
        else:
            create_target()
            o = bpy.data.objects.new( "empty", None )

            # due to the new mechanism of "collection"
            bpy.context.scene.collection.objects.link( o )

            # empty_draw was replaced by empty_display
            o.empty_display_size = 2
            o.empty_display_type = 'CUBE'

            o.select_set(True)

            for obj in bpy.context.selected_objects:
                obj.name = "Target"
       
            return True
#Select the Camera.
#bpy.data.objects['Camera'].select_set(True)

def create_camera_target(camera,target):
    
    
    camera_obj = bpy.data.objects[camera]
    target_obj = bpy.data.objects[target]
    
    
    constraint = camera_obj.constraints.new(type='TRACK_TO')
    constraint.target = target_obj
    # deselect all if anything was selected
    bpy.ops.object.select_all(action='DESELECT')
    return True

    
 
# create_camera_target('Camera', "Target")

# Deselect All
bpy.ops.object.select_all(action='DESELECT')

#Select the Targget
bpy.data.objects['Camera'].select_set(True)

#Reset all camera location to 0
bpy.ops.object.location_clear(clear_delta=False)
bpy.ops.object.rotation_clear(clear_delta=False)
bpy.ops.object.scale_clear(clear_delta=False)


# Camera position 1
#bpy.ops.transform.translate(value=(-0, -9.03681, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

# Camera position 2
#bpy.ops.transform.translate(value=(6.91913, -7.2602, 1.01801), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

# Camera position 3
#bpy.ops.transform.translate(value=(0, 0, 28.404), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
