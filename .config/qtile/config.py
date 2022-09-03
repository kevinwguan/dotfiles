from config_gui import autostart
from config_keys import run_keys, run_mouse
from config_groups import run_groups
from config_layouts import run_layouts, run_floating_layout
from config_screens import run_screens, run_widget_defaults


# Configs
keys = run_keys()
groups = run_groups()
layouts = run_layouts()
widget_defaults = run_widget_defaults()
screens = run_screens()
mouse = run_mouse()
floating_layout = run_floating_layout()

# Defaults
extension_defaults = widget_defaults.copy()
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
