#!/usr/bin/env python3

# Used in keys, groups, layouts, and screens (4)
import os, subprocess
from libqtile import hook


# Variables
fhd = 144
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


def run_sfactor():
    if dpi.stdout:
        if int(dpi.stdout) == qhd:
            return 2
        else:
            return 1
    else:
        return 1


def run_hidpi():
    if dpi.stdout:
        if int(dpi.stdout) == qhd:
            return "env GDK_SCALE=2 GDK_DPI_SCALE=0.5" + ' '
        else:
            return ''
    else:
        return ''


# What if everything was a dict?
hidpi = run_hidpi()
gui = {
    "1": "firefox",
    "2": "thunderbird",
    "3": hidpi+"thunar",
    "4": "pycharm",
    "5": "idea",
    #"6": "",
    "7": "zotero",
    "8": "mathematica",
    #"9": "",
    #"0": "",
    #"": "",
    "c": "calibre",
    "d": "discord",
    "l": "libreoffice",
    "n": "notion-app",
    "p": "xfce4-display-settings --minimal",
    "s": "slack",
    "t": "xfce4-terminal",
    "z": "zoom",
    "space": "rofi -show",
    #"": "xfce4-screenshooter",
    #"": "xfce4-session-logout",
    #"": "xfce4-appfinder",
    #"": "",
}

# Colors
sfactor = run_sfactor()
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
