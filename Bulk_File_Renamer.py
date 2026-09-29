
from pathlib import Path


class FileRenamer:
    def __init__(self, folder, prefix="photo_"):
        self.folder = folder
        self.prefix = prefix

    def get_files(self):
        return [f for f in self.folder.iterdir() if f.is_file()]

    def build_new_name(self, file, index):
        return f"{self.prefix}{index}{file.suffix}"

    def rename_all(self):
        files = self.get_files()
        for i, file in enumerate(sorted(files), start=1):
            new_name = self.build_new_name(file, i)
            file.rename(self.folder / new_name)
            print(f"Renamed {file.name} -> {new_name}")


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    renamer = FileRenamer(folder=script_dir / "Images", prefix="photo_")
    renamer.rename_all()
