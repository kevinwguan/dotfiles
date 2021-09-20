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
# More alias assignments
alias pkglist='pacman -Qqen'
alias aurlist='pacman -Qqm'
alias doom='~/.emacs.d/bin/doom'
alias orphans='pacman -Qttdq | sudo pacman -Rns -'
alias config='cd && /usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
