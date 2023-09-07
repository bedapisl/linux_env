import argparse
import os
import shutil
import subprocess


BACKUP_FOLDER = "./backup"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-install", action="store_true")
    args = parser.parse_args()
    return args


def symlink_file(source: str, destination: str, backup=True) -> None:
    if backup and os.path.isfile(destination):
        os.makedirs(BACKUP_FOLDER, exist_ok=True)
        shutil.copyfile(destination, os.path.join(BACKUP_FOLDER, os.path.basename(destination)))

    output_dir = os.path.dirname(destination)

    os.makedirs(output_dir, exist_ok=True)

    if os.path.isfile(destination) or os.path.islink(destination):
        os.remove(destination)

    os.symlink(source, destination)


def run_subprocess(command):
    print(f"Executing: {command}")
    subprocess.run(command)


def main():
    args = parse_args()

    files = [
        ("dotfiles/vimrc", "~/.vimrc"),
        ("dotfiles/bashrc", "~/.bashrc"),
        ("dotfiles/vscode/keybindings.json", "~/.config/Code/User/keybindings.json"),
        ("dotfiles/vscode/settings.json", "~/.config/Code/User/settings.json"),
        ("scripts/restart_network_manager.sh", "~/scripts/restart_network_manager.sh"),
        ("scripts/brightness.sh", "~/scripts/brightness.sh")
    ]

    for source, destination in files:
        symlink_file(os.path.join(os.getcwd(), source), os.path.expanduser(destination))

    if args.full_install:
        git_email = input("Git email: ")

        run_subprocess(f"git config --global user.email {git_email}")
        run_subprocess('git config --global user.name "Bedrich Pisl"')
        run_subprocess('git config --global core.editor "vim"')


if __name__ == "__main__":
    main()


