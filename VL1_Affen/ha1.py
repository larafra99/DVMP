import bpy
import random 
import math 

SPACING = 5 #constanten upper cas
CIRCLE = 8

r = 5

bpy.ops.object.select_all(action='SELECT') # selektiert alle Objekte
bpy.ops.object.delete(use_global=False, confirm=False) # löscht selektierte objekte
bpy.ops.outliner.orphans_purge() # löscht überbleibende Meshdaten etc.



for i in range(CIRCLE):
    t = i/CIRCLE * 2 * math.pi
    rand_scale_x = random.uniform(0.5, 1.5)
    rand_scale_y = random.uniform(0.5, 1.5)
    rand_scale_z = random.uniform(0.5, 1.5)
    rand_scale_overall = random.uniform(0.5, 1.5)
    loc_x = math.cos(t)*SPACING
    loc_y = math.sin(t)*SPACING
    loc_z = 1
 
    bpy.ops.mesh.primitive_monkey_add(location=(loc_x, loc_y,0))
    bpy.context.object.scale = (rand_scale_x * rand_scale_overall,rand_scale_y * rand_scale_overall,rand_scale_z * rand_scale_overall)
    bpy.context.object.rotation_euler.z = t-math.pi/2
    bpy.ops.object.modifier_add ( type = 'SUBSURF')
    bpy.ops.object.shade_smooth()
    #my_monkey_mesh: bpy.types.Mesh = bpy.context.object.data #typen zuweisung
