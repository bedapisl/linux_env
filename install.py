import argparse
import os
import shutil
import subprocess


# def read_file(filepath: str) -> str:
#     with open(filepath, "r") as input_file:
#         return input_file.read()


# def confirmation(question: str) -> bool:
#     question += " [y/n]"
#     answer = input(question)
#     while answer not in ["y", "n"]:
#         answer = input(question)

#     if answer == "y":
#         return True
#     elif answer == "n":
#         return False
#     else:
#         assert False

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

    if os.path.isfile(destination):
        os.remove(destination)
    os.symlink(source, destination)

    # copy = False
    # if os.path.isfile(destination):
    #     source_data = read_file(source)
    #     destination_data = read_file(destination)

    #     if source_data != destination_data:
    #         copy = confirmation(f"File {source} and  {destination} differs. Owerwrite?")
    # else:
    #     copy = True   

    # if copy:
    #     shutil.copyfile(source, destination)


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


