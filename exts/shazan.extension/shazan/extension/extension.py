import omni.ext
import omni.ui as ui
import omni.kit.commands as command


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[shazan.extension] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class ShazanExtensionExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[shazan.extension] shazan extension startup")

        self._window = ui.Window("Learning Extension", width=300, height=300)
        with self._window.frame:
            with ui.VStack():

                def on_click(prim_type):
                    command.execute("CreateMeshPrimWithDefaultXform",prim_type=prim_type)

                ui.Label("Create me the following")
                ui.Button("Create a Cone",clicked_fn=lambda: on_click("Cone"))
                ui.Button("Create a Cube",clicked_fn=lambda: on_click("Cube"))
                ui.Button("Create a Cylinder",clicked_fn=lambda: on_click("Cylinder"))
                ui.Button("Create a Disk",clicked_fn=lambda: on_click("Disk"))
                ui.Button("Create a Plane",clicked_fn=lambda: on_click("Plane"))
                ui.Button("Create a Sphere",clicked_fn=lambda: on_click("Sphere"))
                ui.Button("Create a Torus",clicked_fn=lambda: on_click("Torus"))

    def on_shutdown(self):
        print("[shazan.extension] shazan extension shutdown")
