import bpy 
import time


#Deselect all
bpy.ops.object.select_all(action='DESELECT')

# Create a empty cube as a target.
def create_target():
    
    objects = bpy.context.scene.objects

    for obj in objects:
        if obj.type == "EMPTY":
            print("Target Already Exists")
            return False
        else:
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

def move_target_face():
       
    #Grab current location or face or hair #x,y,z
    target_location = bpy.data.objects["hair"].location
    
    #Move to the target to that location
    bpy.data.objects['Target'].select_set(True)
    
    for i in range(3):
        bpy.context.object.location[i] = target_location[i]
        
    #Move the target on the z axis 2 int more.
    bpy.context.object.location[2] = target_location[2] -2
    
    #Set y location to 0
    bpy.context.object.location[1] = 0
    
    # Deselect All
    bpy.ops.object.select_all(action='DESELECT')
    

    
    
    print("hey")

def move_target_body():
    print("hey")

def move_target_long():
    print("hey")


def camera_face_preview():
    #move_target_face()
    
    # Create a list of poistions and then with for loop render each. 
    camera_positions = [[7.23, -10, 13.1],[]]

    # Deselect All
    bpy.ops.object.select_all(action='DESELECT')
    
    camera_obj = bpy.data.objects["Camera"]

    # Choose camera type 'PANO', 'PERSP' and 'ORTHO' 
    bpy.data.cameras['Camera'].type = 'ORTHO'

    #Select the Targget
    camera_obj.select_set(True)
    
    # Set camera location & rotation to 0
    
    for i in range(3):
        camera_obj.location[i] = 0
        camera_obj.rotation_euler[i] = 0
    
    
    
    # Camera position 1
    #bpy.ops.transform.translate(value=(-0, -9.03681, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    # Camera position 2
    #bpy.ops.transform.translate(value=(6.91913, -7.2602, 1.01801), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    # Camera position 3
    #bpy.ops.transform.translate(value=(0, 0, 28.404), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

camera_face_preview()