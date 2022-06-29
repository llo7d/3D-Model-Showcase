import bpy 
import os
import pathlib



#Deselect all
bpy.ops.object.select_all(action='DESELECT')


def delete_all_cameras_and_empty_objects():


    # Delete all the Camera Objetcs
    bpy.ops.object.select_all(action='DESELECT')
    
    for o in bpy.context.scene.objects:
        if o.type == 'CAMERA':
            o.select_set(True)
        else:
            o.select_set(False)
    
    bpy.ops.object.delete()
    
    
    # Delete the Empty objects
    bpy.ops.object.select_all(action='DESELECT')
    
    for o in bpy.context.scene.objects:
        if o.type == 'EMPTY':
            o.select_set(True)
        else:
            o.select_set(False)
            
  
    bpy.ops.object.delete()
    
    
    # Save and re-open the file to clean up the data blocks
    bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
    bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)

    
def create_settings():
    # Disable Simplfy
    # File format PNG, Color: RGBA, FILM: Enable Transparent, Resolution 1920x1080, 100% Resolution
    print("maybe some settings defaults need to be created")
    

# Create a empty cube as a target.
def create_target_and_camera():
    
    
    # Creating the Camera    
    camera_data = bpy.data.cameras.new(name='Camera')
    camera_object = bpy.data.objects.new('Camera', camera_data)
    bpy.context.scene.collection.objects.link(camera_object)
        
    
    # Creating empty box with the name Target
    o = bpy.data.objects.new( "empty", None )
    bpy.context.scene.collection.objects.link( o )

    o.empty_display_size = 2
    o.empty_display_type = 'CUBE'

    o.select_set(True)

    for obj in bpy.context.selected_objects:
        obj.name = "Target"
       
       
    # Adding the "Track to" constraint to the camera.
    constraint = bpy.data.objects["Camera"].constraints.new(type='TRACK_TO')
    constraint.target = bpy.data.objects["Target"]
    
    # Deselecting all if anything was selected
    bpy.ops.object.select_all(action='DESELECT')
       
    

  
def create_folders():
    #Here with the provide path to the file we create the required folders. Very shit, should be done alot better.
    #current_directory = os.path.abspath(__file__) #+  "/"+"360"+"/"+"WIREFRAME"
    
    # TODO: Create "Material/Wireframe/Rendered" folders.
    # bpy.data.filepath
    # Leaf directory 
    directory = "360/WIREFRAME"
     
    # Parent Directories 
    #parent_dir = bpy.data.filepath
    
    
    pwd = bpy.data.filepath
    parent = os.path.join(pwd, os.pardir)
    file_root_path = os.path.abspath(parent)
    
    pathlib.Path(file_root_path + '/360/WIREFRAME').mkdir(parents=True, exist_ok=True) 
    pathlib.Path(file_root_path + '/360/MATERIAL').mkdir(parents=True, exist_ok=True)
    pathlib.Path(file_root_path + '/360/RENDERED').mkdir(parents=True, exist_ok=True)
    
    
            
def move_target_body(object_name):
    
    print(object_name)
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
  
     
def render(shading_type):

     
    sce = bpy.context.scene.name
    file_number = 0 
    
    # Initialize Path
    bpy.data.scenes[sce].render.filepath = "//"+"360"+"/"+shading_type + "/" + "360"+"_" + str(file_number) 

    # Getting the path:
    # function that checks if this is wireframe/material and auto goes to that path, but his is too manual.
    path = r'E:\Zudrit Studios\Projects\_BLRDY_\02_3D_Disney_Style\06_3D_White_Teen_Girl(D)\White Teen Girl (Waitriss)\Rigged'
    nPath = path + "/" + "360" + "/" + shading_type

    
    lst=os.listdir(nPath)


    # Inscrease file_number based on last rendered file.
    for i in lst:
        if int(i[4:-4]) <= file_number:
            file_number += 1
        
            
            
    # Changes the path based if new_number ( I think this can be shorter ) 
    bpy.data.scenes[sce].render.filepath = "//"+"360"+"/"+shading_type + "/" + "360"+"_" + str(file_number) 

    # Getting info about the screen to toggle the xray??????
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        
        
    # Go into camera-view
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            area.spaces[0].shading.type = str(shading_type)
            
            if area.spaces[0].shading.show_xray_wireframe:
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.view3d.toggle_xray(override)
            


        # Disable / Enable "Show_Overlays"
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.overlay.show_overlays = False
                
                    
        
        
    # Render image through viewport
    #bpy.ops.render.opengl(write_still=True)
    
    if shading_type != "RENDERED":
        bpy.ops.render.opengl(write_still=True)
    else:
        bpy.ops.render.render(write_still=True)  
    
        

# This is the first function you should call to setup the file to generate the images.
def initial_setup():
    
    print("hey")
    
        
    # Delete all cameras ( X )
    #delete_all_cameras_and_empty_objects():
    
    # This function creates a camera that tracks the target (It also creates the Empty Box Target) 
    # create_target_and_camera() ( X )
    
    # This function creates all the folders required for a 360 render.
    # Provide a path to the current file location.
    # create_folders()
    
    # This function moves the target to the middle of the 3d object.
    # move_target_body()
        
    # Settings, like transparent background, 1920x1080 res etc...
    # create_settings()
        
        


    


# This is the second function you should call with the type of shading you want for yout 360
# Shading Type, Shading type name, 
def preview_360(preview_type):
    #move_target_face()
    
    # List of camera angels # xyz
    camera_locations = [
        [0,-42,9.5],
        [29.9,-29.9,9.5],
        [29.9,29.9,9.5],
        [0,42,9.5],
        [-29.9,29.9,9.5],
    ]

    # Deselect All
    bpy.ops.object.select_all(action='DESELECT')
    
    camera_obj = bpy.data.objects["Camera"]

    # Choose camera type 'PANO', 'PERSP' and 'ORTHO' 
    bpy.data.cameras['Camera'].type = 'PERSP'

    #Select the Targget
    camera_obj.select_set(True)
    
    # Reset he camera location
    for i in range(3):
        camera_obj.location[i] = 0
        camera_obj.rotation_euler[i] = 0

    # Loop trough list of poses and then viewport render
    for i in camera_locations:
        # change position
        for j in range(3):
            camera_obj.location[j] = i[j]
        
        # render ( # Shading Type, Shading type name, Path ? )
        render(preview_type)
        
        # Reset he camera location
        for i in range(3):
            camera_obj.location[i] = 0
            camera_obj.rotation_euler[i] = 0
            
            
            
        
create_folders()
    
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

#preview_360("MATERIAL")
#preview_360("WIREFRAME")
#preview_360("RENDERED")



#Instructions:
# Start with create_folder and provide the current blender file path as a r"string"
# Run "delete_all_cameras_and_targets" 
# Run "create_camera_target"
# Create good instructions to also use for github ( generate 5 images of a 360 of a model in Wireframe,solid and render view )
# TODO:
# Create a function that is called "Initial setup" that has the, delte cameras, create camera, create target etc... 

# 
# 1.
# 2.
#
#
#
    