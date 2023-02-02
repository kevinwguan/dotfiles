# Include
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.config/zsh/alias.zsh
# Set
HISTFILE=~/.zhistory
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# Interface
autoload -Uz compinit promptinit
compinit
promptinit
prompt walters

# Completion
zstyle ':completion:*' menu select
setopt COMPLETE_ALIASES
# Data loss prevention
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'
#alias ls='ls -a --color=auto'
alias nless='/usr/share/nvim/runtime/macros/less.sh'
# More alias assignments
alias pkglist='pacman -Qqen'
alias aurlist='pacman -Qqm'
alias doom='~/.emacs.d/bin/doom'
alias orphans='pacman -Qttdq | sudo pacman -Rns -'
alias true-orphans='pacman -Qtdq | sudo pacman -Rns -'
alias pkgless='comm -23 <(pacman -Qqen | sort) <({ pacman -Qqg base-devel xorg xfce4 xfce4-goodies; expac -l '\n' '%E' base; } | sort -u)'
alias config='cd && /usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias keyring='sudo pacman -Sy archlinux-keyring && sudo pacman -Su'
alias dotdesktop='cd /usr/share/applications/ && ls /usr/share/applications/'
alias dotlogin='echo /etc/systemd/logind.conf'
alias fhd='xfconf-query -c xsettings -p /Xft/DPI -s 120'
alias qhd='xfconf-query -c xsettings -p /Xft/DPI -s 192'
