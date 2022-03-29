import bpy
import random 

SPACING = 5 #constanten upper cas
ROWS = 5
COLS = 5

bpy.ops.object.select_all(action='SELECT') # selektiert alle Objekte
bpy.ops.object.delete(use_global=False, confirm=False) # löscht selektierte objekte
bpy.ops.outliner.orphans_purge() # löscht überbleibende Meshdaten etc.



for row in range(ROWS):
    for col in range(COLS):
        rand_scale_x = random.uniform(0.5, 1.5)
        rand_scale_y = random.uniform(0.5, 1.5)
        rand_scale_z = random.uniform(0.5, 1.5)
        rand_scale_overall = random.uniform(0.5, 1.5)
        rand_loc_z = random.uniform(-2, 2)
        rand_object_color = (random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1),1)
        
        bpy.ops.mesh.primitive_monkey_add(location=(row * SPACING, col * SPACING, rand_loc_z))
        bpy.context.object.scale = (rand_scale_x * rand_scale_overall,rand_scale_y * rand_scale_overall,rand_scale_z * rand_scale_overall)
        bpy.context.object.color = rand_object_color
        bpy.ops.object.modifier_add ( type = 'SUBSURF')
        bpy.ops.object.shade_smooth()
        my_monkey_mesh: bpy.types.Mesh = bpy.context.object.data #typen zuweisung
