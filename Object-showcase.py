import bpy 
import os



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
    
    
def viewport_render(render_type):

    # Getting the path:
    # print("File      Path:",os.path.dirname(os.path.abspath(__file__)))
    print(render_type)
    path = r"E:\Zudrit Studios\Projects\_BLRDY_\02_3D_Disney_Style\06_3D_White_Teen_Girl(D)\White Teen Girl (Waitriss)\Rigged\CloseUp"
    lst=os.listdir(path)

    print(lst)

    file_number = 0 

    # Inscrease file_number based on last rendered file.
    for i in lst:
        if int(i[3:-4]) <= file_number:
            file_number += 1
            
        
    sce = bpy.context.scene.name

    # Brakes if we have more then one images, so needs to be a for loop in the future.
    bpy.data.scenes[sce].render.filepath = "//CloseUp/cl_" + str(file_number) 

    # Go into camera-view
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            area.spaces[0].shading.type = 'MATERIAL'
                
        # Disable / Enable "Show_Overlays"
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.overlay.show_overlays = True
                break
        break
    # Render image through viewport
    bpy.ops.render.opengl(write_still=True)
    
        


def camera_face_preview():
    #move_target_face()
    
    # List of camera angels # xyz
    camera_locations = [
        [7.23,-10,13.1],
        [10.3,0.17,12.6],
        [-0.4,8,11],
    ]

        
    # Create a list of poistions and then with for loop render each. 
    #camera_positions = [[7.23, -10, 13.1],[]]

    # Deselect All
    bpy.ops.object.select_all(action='DESELECT')
    
    camera_obj = bpy.data.objects["Camera"]

    # Choose camera type 'PANO', 'PERSP' and 'ORTHO' 
    bpy.data.cameras['Camera'].type = 'ORTHO'

    #Select the Targget
    camera_obj.select_set(True)
    

    # Loop trough list of poses and then viewport render
    for i in camera_locations:
        
        # change position
        for j in range(3):
            camera_obj.location[j] = i[j]
        
        # render
        viewport_render("Close_Up")
        
        # reset camera location
        for i in range(3):
            camera_obj.location[i] = 0
            camera_obj.rotation_euler[i] = 0
    
        
    
camera_face_preview()