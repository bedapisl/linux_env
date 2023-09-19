import argparse
import os
import shutil
import subprocess


BACKUP_FOLDER = "./backup"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-install", action="store_true", help="Use when installing for the first time.")
    parser.add_argument("--tag", type=str, default=None, required=False, help="Use files with tag in the name, e.g.: settings.small_display.json instead of settings.json, where tag is small_display")
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
        ("dotfiles/openbox/lxde-rc.xml", "~/.config/openbox/lxde-rc.xml"),
        ("scripts/restart_network_manager.sh", "~/scripts/restart_network_manager.sh"),
        ("scripts/brightness.sh", "~/scripts/brightness.sh"),
        ("scripts/fix_time.sh", "~/scripts/fix_time.sh")
    ]

    tag_used = False
    for source, destination in files:
        source = os.path.join(os.getcwd(), source)
        destination = os.path.expanduser(destination)
        if args.tag:
            dirname, filename = os.path.split(source)
            basename, extension = os.path.splitext(filename)
            source_with_tag = os.path.join(dirname, f"{basename}.{args.tag}{extension}")
            if os.path.exists(source_with_tag):
                source = source_with_tag
                tag_used = True

        symlink_file(source, destination)

    if args.tag and not tag_used:
        print(f"Warning: Tag {args.tag} was not used.")

    if args.full_install:
        git_email = input("Git email: ")

        run_subprocess(f"git config --global user.email {git_email}")
        run_subprocess('git config --global user.name "Bedrich Pisl"')
        run_subprocess('git config --global core.editor "vim"')


if __name__ == "__main__":
    main()


