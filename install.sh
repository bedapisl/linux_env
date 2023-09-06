
ln -sf ./dotfiles/vimrc ~/.vimrc
ln -sf ./dotfiles/bashrc ~/.bashrc

mkdir .config/Code/User/

ln -s ./dotfiles/vscode/keybindings.json ~/.config/Code/User/keybindings.json
ln -s ./dotfiles/vscode/settings.json ~/.config/Code/User/settings.json

mkdir ~/scripts

ln -s ./scripts/restart_network_manager.sh ~/scripts/restart_network_manager.sh
ln -s ./scripts/brightness.sh ~/scripts/brightness.sh

read -p "Git email: " git_email

git config --global user.email git_email
git config --global user.name "Bedrich Pisl"
git config --global core.editor "vim"

