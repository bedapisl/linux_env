import os


def read_file(filepath: str) -> str:
    with open(filepath, "r") as input_file:
        return input_file.read()


def confirmation(question: str) -> bool:
    question += " [y/n]"
    answer = input(question)
    while answer not in ["y", "n"]:
        answer = input(question)

    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        assert False


def copy_file(source: str, destination: str) -> None:
    copy = False
    if os.path.isfile(destination):
        source_data = read_file(source)
        destination_data = read_file(destination)

        if source_data != destination_data:
            copy = confirmation(f"File {source} and  {destination} differs. Owerwrite?")
    else:
        copy = True   

    if copy:
        shutil.copyfile(source, destination)


def main():
    files = [
        ("dotfiles/vimrc", "~/.vimrc"),
        ("dotfiles/bashrc", "~/.vimrc"),




if __name__ == "__main__":



