#!/usr/bin/env python3

from config_gui import colors, sfactor
from libqtile import bar, widget
from libqtile.config import Screen


wallpaper = "~/Pictures/wallpaper/webb4k.png"
systray = widget.Systray(icon_size=16*sfactor)


def run_widget_defaults():
    return dict(
        font="Inconsolata, Font Awesome",
        fontsize=22*sfactor,
        padding=10*sfactor,
        background=colors["bg"],
        foreground=colors["fg"],
    )


def run_screens():
    screens = []
    screens.append(
        Screen(
            bottom=bar.Bar(
                [
                    widget.CurrentLayoutIcon(scale=2/3),
                    widget.GroupBox(
                        highlight_method="text",
                        active=colors["green"],
                        this_current_screen_border=colors["magenta"],
                        visible_groups=[str(x) for x in range(10)],
                    ),
                    systray,
                    widget.Spacer(),
                    widget.Bluetooth(
                        hci="/dev_7C_58_CA_00_33_DB",
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                    widget.Wlan(
                        format="{essid:0.6} ({percent:2.0%})",
                        max_chars=13,
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                    widget.Volume(
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                    widget.Backlight(
                        backlight_name="intel_backlight",
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                    widget.Battery(
                        format="{percent:2.0%}",
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                    widget.Clock(
                        format="%Y-0%m-%d %a",
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                    widget.Clock(
                        format="%I:%M:%S %p",
                        fmt="{}"+' '+"<span foreground='{}'></span>".format(colors["yellow"])),
                ],
                24*sfactor,
                background=colors["bg"],
            ),
            wallpaper=wallpaper,
            wallpaper_mode="fill",
        ),
    )
    return screens
