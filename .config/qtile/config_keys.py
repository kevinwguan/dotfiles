#!/usr/bin/env python3

from config_gui import gui, colors
from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from libqtile import extension


mod = "mod1"
logo = "mod4"


def run_keys():
    keys = [
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [logo, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([logo, "control"], "Return", lazy.spawn(gui["d-term"]), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([logo], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([logo, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
        Key([logo], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([logo, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([logo, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        #Key([logo], "r", lazy.spawn(gui["appfinder"]), desc="Spawn a command"),

        # System
        Key([logo], "p", lazy.spawn(gui["display"])),
        Key([], "Print", lazy.spawn(gui["screenshooter"])),
        Key([mod, "control"], "Delete", lazy.spawn(gui["logout"])),
        Key([mod, "control"], "l", lazy.spawn(gui["lock"]), desc="Lock Qtile"),
        Key([mod], "Tab", lazy.screen.toggle_group(), desc=""),
        Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc=""),
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc=""),
        Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
        # Media
        Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl --player=rhythmbox,spotify previous")),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl --player=rhythmbox,spotify play-pause")),
        Key([], "XF86AudioNext", lazy.spawn("playerctl --player=rhythmbox,spotify next")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
        # Speed-Dial
        Key([mod], "grave", lazy.spawn(gui["grave"]), desc=""),
        Key([logo], "0", lazy.spawn(gui["0"]), desc=""),
        Key([logo], "1", lazy.spawn(gui["1"]), desc=""),
        Key([logo], "2", lazy.spawn(gui["2"]), desc=""),
        Key([logo], "3", lazy.spawn(gui["3"]), desc=""),
        Key([logo], "4", lazy.spawn(gui["4"]), desc=""),
        Key([logo], "5", lazy.spawn(gui["5"]), desc=""),
        Key([logo], "space", lazy.spawn(gui["space"]), desc=""),
        Key([logo, "control"], "space", lazy.spawn(gui["dgpu"]), desc=""),
    ]
    config_keys_group(keys)
    config_keys_scratchpad(keys)
    config_keys_dmenu(keys)

    return keys


def config_keys_group(keys):
    for i in range(10):
        name = str(i)
        keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], name, lazy.group[name].toscreen(toggle=False),
                desc="Switch to group {}".format(name)),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], name, lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(name)),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ])


def config_keys_scratchpad(keys):
    keys.extend([
        # ScratchPad DropDown
        Key([mod], 'Return', lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([mod, "shift"], 'Return', lazy.group['scratchpad'].dropdown_toggle('doom')),
        Key([mod, "control"], '1', lazy.group['scratchpad'].dropdown_toggle('qtile')),
        Key([mod, "control"], '2', lazy.group['scratchpad'].dropdown_toggle('xfce')),
        Key([mod, "control"], '3', lazy.group['scratchpad'].dropdown_toggle('htop')),
        Key([mod, "control"], '4', lazy.group['scratchpad'].dropdown_toggle('nvidia')),
        Key([mod], 'minus', lazy.group['scratchpad'].dropdown_toggle('pavucontrol')),
        Key([mod], 'equal', lazy.group['scratchpad'].dropdown_toggle('spotify')),
        Key([logo], 'Return', lazy.group['scratchpad'].dropdown_toggle('notion')),
    ])


def config_keys_dmenu(keys):
    keys.extend([
        Key(['mod4'], 'r', lazy.run_extension(extension.DmenuRun(
            dmenu_prompt=">",
            #dmenu_font="Andika-8",
            background=colors["bg"],
            foreground=colors["fg"],
            selected_background=colors["bg"],
            selected_foreground=colors["yellow"],
            #dmenu_height=24,  # Only supported by some dmenu forks
        ))),
    ])


def run_mouse():
    return [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
    ]
