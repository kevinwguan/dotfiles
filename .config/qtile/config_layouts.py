#!/usr/bin/env python3

from config_gui import colors, sfactor
from libqtile import layout
from libqtile.config import Match


layout_theme = {
    "border_focus": colors["red"],
    "border_normal": colors["bg"],
    "border_width" : 2*sfactor,
    "margin": 10*sfactor,
}


def run_layouts():
    return [
        layout.MonadWide(**layout_theme),
        layout.MonadTall(**layout_theme),
        #layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
        #layout.MonadThreeCol(**layout_theme),
        #layout.Columns(**layout_theme),
        #layout.Bsp(**layout_theme),
        #layout.Matrix(**layout_theme),
        #layout.RatioTile(**layout_theme),
        #layout.Slice(**layout_theme),
        #layout.Spiral(**layout_theme),
        #layout.Stack(**layout_theme),
        #layout.Tile(**layout_theme),
        #layout.TreeTab(**layout_theme),
        #layout.VerticalTile(**layout_theme),
        #layout.Zoomy(**layout_theme),
    ]


def run_floating_layout():
    return layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class='xfce4-appfinder'),
            Match(wm_class='Steam'),
            Match(wm_class='discord'),
            Match(wm_class='Slack'),
            Match(wm_class='zoom'),
            Match(wm_class='confirmreset'),  # gitk
            Match(wm_class='makebranch'),  # gitk
            Match(wm_class='maketag'),  # gitk
            Match(wm_class='ssh-askpass'),  # ssh-askpass
            Match(title='branchdialog'),  # gitk
            Match(title='pinentry'),  # GPG key password entry
        ],
        border_focus=colors["blue"],
        border_normal=colors["bg"],
        border_width=0,
    )
