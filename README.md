# 3D-Model-Showcase
 A Blender Python script that automaticly generates images to showcase 3D Model.


This is how to use it.

1. Open up the python script called "Generate_360.py" in Blender and go the scripting tab.

2. Call the setup(object_name) function with the name of the 3D Object that is the highest on the z axis. In my case its "hair", so call I call setup("hair")

![](https://gyazo.com/fc015e69b6c9a51103d841b3cfbefa4a.png)

Make sure to call this function first and wait for it execute before calling or doing anything else.


3. We either run the function go_into_camera_view() to go into camera view or just press 0 on numpad.
Make sure, you no longer call the "setup()" function. Comment it out with #


4. Then we can run the preview_360(shading_type) function with the shading type: "MATERIAL", "WIREFRAME" or "RENDERED"

And once we do that, we will create 3 folders and in those you will see the images.
![](https://gyazo.com/dfb9ba5891bbb56069ff96f7f263337c.png)
![](https://gyazo.com/7fc17d64379c2655acc61c0dd1acd51f.png)


So in short:
1' Run setup("hair"), wait for it execute then comment it out with #. 2' press 0 on numpad. 3' run preview_360("WIREFRAME")


You can check out the [Youtube video how I made it and how to use it](https://youtu.be/qm8ZYKtM7Ho "Youtube Video Link")

