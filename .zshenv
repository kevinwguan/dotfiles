# Utilize all cores for makepkg
export MAKEFLAGS="-j$(nproc)"

# Java programs
export _JAVA_AWT_WM_NONREPARENTING=1

# HiDPI
export QT_AUTO_SCREEN_SCALE_FACTOR=1

# Qt
export QT_QPA_PLATFORMTHEME=qt5ct
