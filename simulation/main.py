
from pathlib import Path
from generate_samples import generate_save_data



if __name__ == "__main__":
    file_path =  Path(__file__).resolve().parent.parent / "Data/sample1.csv"
    print(file_path)
    generate_save_data(file_path, seed=200)