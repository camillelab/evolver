import bpy

# Open in Blender text editor
# Export the selected mesh with A-p

def write_some_data(context, filepath):
    obj = context.active_object
    fichier = open(filepath, 'w', encoding='utf-8')
    fichier.write('vertices\n')
    for i, v in enumerate(obj.data.vertices):
        fichier.write(f'{i + 1} {v.co.x} {v.co.y} {v.co.z}\n')
    
    edges = dict()
    fichier.write('\nedges\n')
    for i, e in enumerate(obj.data.edges):
        alpha = e.vertices[0]
        omega = e.vertices[1]
        edges[(alpha, omega)] = i + 1
        fichier.write(f'{i + 1} {alpha + 1} {omega + 1}\n')

    fichier.write('\nfaces\n')
    for i, f in enumerate(obj.data.polygons):
        l1 = list(f.vertices)
        l2 = l1[1:] + [l1[0]]
        elist = [str(edges[k]) if k in edges else '-'+str(edges[(k[1], k[0])])
                 for k in list(zip(l1, l2))]
        s = ' '.join(elist)
        fichier.write(f'{i + 1} {s}\n')
    
    fichier.close()

    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"

    # ExportHelper mixin class uses this
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.ce",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        return write_some_data(context, self.filepath)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="Text Export Operator")


def register():
    bpy.utils.register_class(ExportSomeData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.export_test.some_data('INVOKE_DEFAULT')
