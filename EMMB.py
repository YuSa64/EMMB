bl_info = {
    "name": "Toggle MMB",
    "author": "YuSa64",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > EMMB",
    "description": "Toggle Emulate 3 Button Mouse",
    "category": "3D View",
}

import bpy

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Toggle"

    def execute(self, context):
        # toggle the "Emulate 3 Button Mouse" preference
        bpy.context.preferences.inputs.use_mouse_emulate_3_button = not bpy.context.preferences.inputs.use_mouse_emulate_3_button
        return {'FINISHED'}

class SimplePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Toggle MMB"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EMMB"

    def draw(self, context):
        layout = self.layout

        # add a label to show the current status of the preference
        if bpy.context.preferences.inputs.use_mouse_emulate_3_button:
            layout.label(text="Emulate MMB: ON")
        else:
            layout.label(text="Emulate MMB: OFF")

        # add the toggle button
        layout.operator("object.simple_operator")

def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(SimplePanel)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(SimplePanel)

if __name__ == "__main__":
    register()
