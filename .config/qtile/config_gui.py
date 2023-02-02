#!/usr/bin/env python3

import os, subprocess
from libqtile import hook
from libqtile.utils import guess_terminal


"""Only file to modify."""
# Variables
fhd = 120
qhd = 192
dpi = subprocess.run(
    "cat ~/dpi",
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
"""Look at pkglist | aurlist"""
dgpu = "prime-run" + ' '
hidpi = run_hidpi()
sfactor = run_sfactor()
terminal = guess_terminal(preference="kitty")
wallpaper = "/usr/share/backgrounds/archlinux/simple.png"
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
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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
    "spotify": "env LD_PRELOAD=/usr/lib/spotify-adblock.so spotify",
    "itunes": hidpi+"rhythmbox",
}
# Keys only
gui = {
    #"": "",
    "d-term": hidpi+"xfce4-terminal",
    "appfinder": hidpi+"xfce4-appfinder",
    "display": hidpi+"xfce4-display-settings --minimal",
    "screenshooter": hidpi+"xfce4-screenshooter",
    "logout": hidpi+"xfce4-session-logout",
    "lock": hidpi+"xflock4",
    #"": "",
    "grave": "rofi -show-icons -dpi 1 -show",
    "0": "notion-app",
    "1": hidpi+"thunar",
    "2": "firefox",
    "3": "thunderbird",
    "4": hidpi+"zotero",
    "5": hidpi+"virt-manager",
    "6": "timeshift-launcher",
    "space": "rofi -show-icons -dpi 1 -show drun",
    "dgpu": dgpu+"rofi -show-icons -dpi 1 -show drun",
    #"": "",
}
