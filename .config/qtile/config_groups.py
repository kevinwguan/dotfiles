#!/usr/bin/env python3

from config_gui import groups_item, scratchpad
from libqtile.config import Group, Match, ScratchPad, DropDown


def run_groups():
    groups = []
    for i, j in enumerate(groups_item):
        k = i + 1
        x = str(k % 10)
        if k == 2:
            y = Group(
                x,
                label=' '.join((x, j)),
                matches=[Match(wm_class='thunderbird')],
            )
        elif k == 6:
            y = Group(
                x,
                label=' '.join((x, j)),
                matches=[
                    Match(wm_class='discord'),
                    Match(wm_class='Slack'),
                    Match(wm_class='zoom'),
                ],
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

            # define a drop down terminal.
            DropDown(
                "term",
                scratchpad["term"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # doom emacs
            DropDown(
                "doom",
                scratchpad["doom"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # qtile shell
            DropDown(
                "qtile",
                scratchpad["qtile"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # xfce
            DropDown(
                "xfce",
                scratchpad["xfce"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # resources
            DropDown(
                "htop",
                scratchpad["htop"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # nvidia
            DropDown(
                "nvidia",
                scratchpad["nvidia"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # pavucontrol
            DropDown(
                "pavucontrol",
                scratchpad["pavucontrol"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

            # rhythombox
            DropDown(
                "rhythmbox",
                scratchpad["rhythmbox"],
                x=0, y=0, width=1, height=1,
                warp_pointer=False,
            ),

        ]),
    )
