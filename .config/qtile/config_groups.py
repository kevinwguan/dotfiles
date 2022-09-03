#!/usr/bin/env python3

from config_gui import gui, hidpi
from libqtile.config import Group, Match, ScratchPad, DropDown
from libqtile.utils import guess_terminal


spotify = "env LD_PRELOAD=/usr/lib/spotify-adblock.so spotify"
terminal = guess_terminal(preference="alacritty")
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


def run_groups():
    groups = []
    for i, j in enumerate(groups_item):
        k = i + 1
        x = str(k % 10)
        if k == 2:
            y = Group(
                x,
                label=' '.join((x, j)),
                matches=[Match(wm_class='Thunderbird')],
            )
        elif k == 6:
            y = Group(
                x,
                label=' '.join((x, j)),
                matches=[
                    Match(wm_class='Slack'),
                    Match(wm_class='zoom'),
                    Match(wm_class='discord')
                ],
                layout="max",
            )
        elif k == 7:
            y = Group(
                x,
                label=' '.join((x, j)),
                matches=[Match(wm_class='Zotero')],
            )
        elif k == 8:
            y = Group(
                x,
                label=' '.join((x, j)),
                matches=[Match(wm_class='Mathematica')],
            )
        else:
            y = Group(
                x,
                label=' '.join((x, j))
            )
        groups.append(y)
    config_scratchpad(groups)
    return groups


def config_scratchpad(groups):
    # Scratchpad
    groups.append(
        ScratchPad("scratchpad", [

            # Doom emacs
            DropDown(
                "emacs",
                "emacs",
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # define a drop down terminal.
            DropDown(
                "term",
                terminal,
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # Qtile shell
            DropDown(
                "qtile shell",
                terminal+' '+"--hold -e qtile shell",
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # Xfce
            DropDown(
                "xfce",
                hidpi+"xfce4-settings-manager",
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # Pavucontrol
            DropDown(
                "pavucontrol",
                hidpi+"pavucontrol",
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # Spotify
            DropDown(
                "spotify",
                spotify,
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # Launcher
            DropDown(
                "xfce4-appfinder",
                hidpi+"xfce4-appfinder",
                x=0.25, y=0.25, width=0.50, height=0.50,
                warp_pointer=False,
            ),

        ]),
    )
