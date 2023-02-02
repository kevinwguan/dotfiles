#!/bin/zsh
startxfce4 &
xfsettingsd &
picom &
emacs --daemon &
xrandr --output eDP-1 --scale 1.5
