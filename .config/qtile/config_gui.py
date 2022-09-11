#!/usr/bin/env python3

import os, subprocess
from libqtile import hook
from libqtile.utils import guess_terminal


# Variables
fhd = 120
qhd = 192
dpi = subprocess.run(
    "xfconf-query -c xsettings -p /Xft/DPI",
    capture_output=True,
    shell=True,
)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


def run_hidpi():
    if dpi.stdout:
        if int(dpi.stdout) == qhd:
            return "env GDK_SCALE=2 GDK_DPI_SCALE=0.5" + ' '
        else:
            return ''
    else:
        return ''


def run_sfactor():
    if dpi.stdout:
        if int(dpi.stdout) == qhd:
            return 2
        else:
            return 1
    else:
        return 1


# What if everything was a dict?
dgpu = "prime-run" + ' '
hidpi = run_hidpi()
sfactor = run_sfactor()
terminal = guess_terminal(preference="alacritty")
wallpaper = "~/Pictures/wallpaper/webb4k.png"
bluetooth = "/dev_7C_58_CA_00_33_DB"
# Colors
colors = {
    "bg":      '#282828',
    "red":     '#cc241d',
    "green":   '#98971a',
    "yellow":  '#d79921',
    "blue":    '#458588',
    "magenta": '#b16286',
    "cyan":    '#689d6a',
    "fg":      '#ebdbb2',
}
# Groups (but not dict...)
groups_item = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
# Keys and Groups
scratchpad = {
    "term": terminal,
    "doom": "emacs",
    "qtile": terminal+' '+"--hold -e qtile shell",
    "xfce": hidpi+"xfce4-settings-manager",
    "htop": terminal+' '+"--hold -e htop",
    "nvidia": hidpi+"nvidia-settings",
    "pavucontrol": hidpi+"pavucontrol",
    "rhythmbox": hidpi+"rhythmbox",
}
# Keys only
gui = {
    #"": "",
    "grave": "rofi -show window",
    "1": "firefox",
    "2": "thunderbird",
    "3": hidpi+"thunar",
    "space": "rofi -show drun",
    "dgpu": dgpu+"rofi -show drun",
    "spotify": "env LD_PRELOAD=/usr/lib/spotify-adblock.so spotify",
    "d-term": hidpi+"xfce4-terminal",
    "appfinder": hidpi+"xfce4-appfinder",
    "display": hidpi+"xfce4-display-settings --minimal",
    "screenshooter": hidpi+"xfce4-screenshooter",
    "logout": hidpi+"xfce4-session-logout",
    "lock": hidpi+"xflock4",
    #"": "",
}
