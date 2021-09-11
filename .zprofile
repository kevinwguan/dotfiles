if [ "$(tty)" = "/dev/tty1" ]; then
	# Utilize all cores for makepkg
	export MAKEFLAGS="-j$(nproc)"
	# Qt theming
	export QT_QPA_PLATFORMTHEME=qt5ct
	# Java programs
	export _JAVA_AWT_WM_NONREPARENTING=1
	# Wayland session
	exec sway
fi
