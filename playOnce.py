bl_info = {
    "name": "Play Once",
    "author": "powersprouter",
    "version": (0,1,7),
    "blender":(3,4,1),
    "location": "View3D Sidebar (n-panel)",
    "description": "converts timeline play button to a single play",
    "warning":"",
    "wiki_url": "www.powersprouter.com",
    "category": "Mine",
    "support": "COMMUNITY",
}

import bpy

def play_once(scene):
    scene = bpy.data.scenes['Scene']
    frame_end = bpy.data.scenes['Scene'].frame_end    

    if scene.frame_current == frame_end:
        bpy.ops.screen.animation_cancel(restore_frame=False)
        remove_play_once(scene) #it removes handler immediately after the end frame is reached, resetting
        
def remove_play_once(scene):
    for h in bpy.app.handlers.frame_change_pre:
        if h.__name__ == 'play_once':
            bpy.app.handlers.frame_change_pre.remove(h)


class PLAYONCE_OT_play_once_operator(bpy.types.Operator):
    """turns on and off the playOnce play button in n-panel"""
    bl_idname = "object.play_once_operator"
    bl_label = "Play"
    
    def execute(self, context):

        if bpy.context.scene.play_once_prop:
            bpy.app.handlers.frame_change_pre.append(play_once)
            bpy.ops.screen.frame_jump(end=False)
            bpy.ops.screen.animation_play()
        
        else:
            bpy.ops.screen.animation_play()
   
        return {'FINISHED'}

class PLAYONCE_OT_remove_play_once_operator(bpy.types.Operator):
    """Removes Play Once in the handlers"""
    bl_idname = "object.remove_play_once_operator"
    bl_label = "Reset"
    
    def execute(self, context):
        scene = bpy.data.scenes['Scene']
        remove_play_once(scene)
        bpy.ops.screen.frame_jump(end=True)
        bpy.ops.screen.frame_jump(end=False)

        return {'FINISHED'}


class VIEW3D_PT_play_once_panel (bpy.types.Panel):
    bl_label = "Play Once"
    bl_idname = "PLAYONCE_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Play Once'

    def draw(self, context):
        scene = context.scene
        screen = context.screen
        layout = self.layout

        row = layout.row()
        row.prop(scene, "play_once_prop", text = "1x ON/OFF",)
        row = layout.row()
        row.operator("screen.frame_jump", text="", icon='REW').end = False
        row.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False
        if not screen.is_animation_playing:
            row.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
            row.operator("object.play_once_operator", text="", icon='PLAY')
        else:
            row.scale_x = 2
            row.operator("screen.animation_play", text="", icon='PAUSE')
            row.scale_x = 1
        row.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
        row.operator("screen.frame_jump", text="", icon='FF').end = True

#register multiple classes

classes = [
PLAYONCE_OT_play_once_operator,
PLAYONCE_OT_remove_play_once_operator,
VIEW3D_PT_play_once_panel,
]

def register():
    
##register new property for the checkbox bool    
    bpy.types.Scene.play_once_prop = bpy.props.BoolProperty(
    name="Play Once",
    description="Toggle on/off Play Once",
    default = False)
    
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():

##unregister new property for the checkbox bool     
    del bpy.types.Scene.play_once_prop    
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    

if __name__ == "__main__":
    register()
    