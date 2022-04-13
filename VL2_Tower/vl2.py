import bpy
import typing 
import math 

class Tower():
    tower_radius: float = 3
    tower_height: float = 8
    roof_height: float = 2.5
    roof_overhang: float = 0.5

    window_num_circular: int = 5
    window_num_vertical: int = 3
    window_size: float = 1
    wall_thickness: float = 0.5

    PI2 = math.pi * 2

    def create_base_material(self) -> bpy.types.Material:
        mat_tower: bpy.types.Material= bpy.data.materials.new("Tower Base Material")
        mat_tower.use_nodes = True
        tree_tower: bpy.types.NodeTree = mat_tower.node_tree
        nodes: typing.List[bpy.types.Node] = mat_tower.node_tree.nodes
        nd_txbricks: bpy.types.Node = nodes.new("ShaderNodeTexBrick")
        nd_texcoord: bpy.types.Node = nodes.new("ShaderNodeTexCoord")
        tree_tower.links.new(nd_txbricks.outputs[0],tree_tower.nodes["Principled BSDF"].inputs[0])
        tree_tower.links.new(nd_texcoord.outputs[2], nd_txbricks.inputs[0])
        nd_txbricks.inputs[4].default_value = 10
        return mat_tower
    
    def create_roof_material(self) -> bpy.types.Material:
        mat_roof: bpy.types.Material= bpy.data.materials.new("Tower Roof Material")
        mat_roof.use_nodes = True
        mat_roof.node_tree.nodes["Principled BSDF"].inputs[0].default_value = [0.031414,0.386704, 0.160960, 1]
        return mat_roof
    
    def create_window_boolean(self):
        windows = []
        for i in range (self.window_num_circular):
            t = i/self.window_num_circular * 2 * math.pi
            x = math.cos(t) * self.tower_radius
            y = math.sin(t) * self.tower_radius
            bpy.ops.mesh.primitive_cube_add(location=(x,y,0))
            bpy.context.object.rotation_euler.z = t-math.pi / 2
            windows.append(bpy.context.object)

        for window in windows:
            window.select_set(True)
            
        bpy.ops.object.join()
        
    def generate_tower(self):
        bpy.ops.mesh.primitive_cylinder_add(
            location=(0, 0, self.tower_height/2),
            depth= self.tower_height,
            radius= self.tower_radius
        )
        tower_base = bpy.context.object
        tower_base.data.materials.append(self.create_base_material())

        bpy.ops.mesh.primitive_cone_add(
            depth= self.roof_height,
            location=(0, 0, self.tower_height + self.roof_height/2),
            radius1= self.tower_radius + self.roof_overhang
        )

        bpy.context.object.data.materials.append(self.create_roof_material())
        self.create_window_boolean()

bpy.ops.object.select_all(action='SELECT')#selektiert alle objekte
bpy.ops.object.delete(use_global=False, confirm= False) #löscht selektierte Objekte
bpy.ops.outliner.orphans_purge()

t = Tower()
t.generate_tower()