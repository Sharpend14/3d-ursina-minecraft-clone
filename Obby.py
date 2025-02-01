'''
Disclaimer: This solution is not scalable for creating a big world.
Creating a game like Minecraft requires specialized knowledge and is not as easy
to make as it looks.

You'll have to do some sort of chunking of the world and generate a combined mesh
instead of separate blocks if you want it to run fast. You can use the Mesh class for this.

You can then use blocks with colliders like in this example in a small area
around the player so you can interact with the world.
'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

#Define a Voxel class.
#By setting the parent to scene and the model to 'cube' it becomes a 3d button.
#Define a plll class.
#By setting the parent to scene and the model to 'cube' it becomes a 3d ppp.
#define a voxel class
#by setting the parent to scene and the model to 'cube' it becomes a 3d character.
class Voxel(Button):
    def __init__(self, position=(0,0,20)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.200,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(0.7, 1.0)),
            highlight_color=color.blue,
        )
class character(Entity):
    def __init__(self):
        super().__init__(
            model = load_model('cube'),
            texture='white_cube',
            color = color.red,
            position = (-0, -3, -8)
        )
class plll(Button):
    def __init__(self, position=(0,0,20)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.200,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(0.7, 1.0)),
            highlight_color=color.blue,
        )


for z in range(8):
    for x in range(8):
        voxel = plll(position=(x,0,z))

for z in range(4):
    for x in range(8):
        voxel = plll(position=(x,0,z+12))
        
        
def input(key):
    print(key)
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=100)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    if key == 'escape':
        #window.exit_button.visible = True
        print("bye")
        app.application.quit()
        #quit()

print("Hello")

cam = FirstPersonController(gravity = 0.15,
                            jump_up_duration = 3,
                            jump_height = 3,
                            fall_after = 1)

player = Entity(model='cube',
            texture='white_cube',
            color=color.hsv(1, 1, random.uniform(0.7, 1.0)),
                origin = (0, -0.5, 0),
                parent = cam)
camera.z = -5
camera.y = -0.5

def update():
    if held_keys['right arrow']:
        player.rotation_y -= 4
    if held_keys['left arrow']:
        player.rotation_y += 4
app.run()