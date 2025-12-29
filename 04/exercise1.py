from pathlib import Path

data_dir = "exercise/data"
data_dir_path = Path(data_dir).resolve()
print("===problem1===")
print(data_dir_path)

file_list = list(Path(data_dir).glob("*"))
print("------problem2------")
for path in enumerate(file_list):
    print(path[1])

print("------problem3------")
file_list = list(Path(data_dir).glob("**/*.png"))
print(len(file_list))