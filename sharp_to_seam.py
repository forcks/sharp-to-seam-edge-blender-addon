import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.utils import register_class, unregister_class
from bpy.props import IntProperty,FloatVectorProperty,PointerProperty
from random import randint

bl_info = {
    "name": "Make sharp edges to seam edges",
    "description": "Make sharp edges to seam edges on the selected object. Addon made specifically for Pavel Ryzhkov",
    "author": "Forcks",
    "version": (1, 0),
    "blender": (3,4,1),
    "location": "View3D > UI > make sharp to seam",
    "warning": "",
    "category": "Edit Mesh",
}

class Make_sharp_to_seam(Operator):
    bl_idname = "scene.sharp_to_seam"
    bl_label = "Sharp to seam"
    
    def Sharp_To_Seam(self):
        bpy.ops.object.mode_set(mode='OBJECT')
        me = bpy.context.object.data
        for e in me.edges:
            if e.use_edge_sharp:
                e.select = True
        bpy.ops.object.mode_set(mode='EDIT') 
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.mesh.mark_seam(clear=False)

        
            
    def execute(self, context):
        self.Sharp_To_Seam()
        return {"FINISHED"}

class OBJECT_PT_Sharp_to_seam(Panel):
    bl_label = "sharp to seam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "make sharp to seam"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("scene.sharp_to_seam")
        

classes = [
    Make_sharp_to_seam,
    OBJECT_PT_Sharp_to_seam
]

def register():
    for cl in classes:
        register_class(cl)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
if __name__ == '__main__':
    register()
    