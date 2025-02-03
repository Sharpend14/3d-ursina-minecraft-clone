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
from direct.actor.Actor import Actor

app = Ursina(borderless=False)

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
class Camera(FirstPersonController):
    def __init__(self):
        super().__init__(
            gravity = 0.5,
            jump_up_duration = 0.5,
            jump_height = 2,
            fall_after = 0.3,
            speed = 9
        )
    def update(self):
        if self.y < -10:
            self.position = (0, 0, 0)
        if self.z > 26:
         if self.y < 15:
            self.position = (0, 30, 0)
        if self.y > 10:
         if self.y < 20:
            self.position = (0, 30, 0)
        super().update()
        

# class character(Entity):
#     def __init__(self):
#         super().__init__(
#             model = load_model('cube'),
#             texture='white_cube',
#             color = color.red,
#             position = (-0, -3, -8)     
#             )
        
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
    for x in range(3):
        voxel = plll(position=(x,0,z))

for z in range(4):
    for x in range(3):
        voxel = plll(position=(x,0,z+12))
        
for z in range(4):
    for x in range(3):
        voxel = plll(position=(x,0,z+20))
        
for z in range(4):
    for x in range(3):
        voxel = plll(position=(x,1,z+26))
        
        
for z in range(8):
    for x in range(3):
        voxel = plll(position=(x,30,z))

for z in range(4):
    for x in range(3):
        voxel = plll(position=(x,30,z+12))
        
for z in range(4):
    for x in range(3):
        voxel = plll(position=(x,30,z+20))
        
for z in range(4):
    for x in range(3):
        voxel = plll(position=(x,30,z+26))

        
        
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
        application.quit()
        #quit()
        
# def update():
#     print(player.y)
#     if player.y<-10:
#         player.y=20

print("Hello")

cam = Camera()

player = Entity(model='cube',
            texture='white_cube',
            color=color.hsv(60, 60, random.uniform(0.7, 1.0)),
                origin = (0, -0.5, 0),
                parent = cam)
# actor = Actor("sandman.geo.gltf")
# actor.reparentTo(cam)


camera.z = 0
camera.y = 0

def update():
    if held_keys['right arrow']:
        player.rotation_y -= 4
    if held_keys['left arrow']:
        player.rotation_y += 4
app.run()