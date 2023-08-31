

ln -s ./dotfiles/vimrc ~/.vimrc
ln -s ./dotfiles/bashrc ~/.bashrc


ln -s ./dotfiles/vscode/keybindings.json ~/.config/Code/User/keybindings.json
ln -s ./dotfiles/vscode/settings.json ~/.config/Code/User/settings.json


mkdir ~/scripts

ln -s ./scripts/restart_network_manager.sh ~/scripts/restart_network_manager.sh
ln -s ./scripts/brightness.sh ~/scripts/brightness.sh

read -p "Git email: " git_email

git config --global user.email git_email
git config --global user.name "Bedrich Pisl"
git config --global core.editor "vim"

