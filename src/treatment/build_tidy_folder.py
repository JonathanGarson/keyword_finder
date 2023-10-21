import os
import shutil

def move_docx_files(input_path:str, output_path:str):
    '''Move all docx files from input_path to output_path'''
    for file in os.listdir(input_path):
        if file.endswith(".docx"):
            shutil.move(os.path.join(input_path, file), output_path)

def move_xlsx_files(input_path:str, output_path:str):
    '''Move all xlsx files from input_path to output_path'''
    for file in os.listdir(input_path):
        if file.endswith(".xlsx"):
            shutil.move(os.path.join(input_path, file), output_path)

if __name__ == '__main__':
    # Get the current working directory
    cwd = os.getcwd()

    # Define the folder structure
    folders_to_create = [
        "data/raw",
        "data/text/raw_docx",
        "data/text/treated_docx"
    ]

    # Create the folders
    for folder in folders_to_create:
        os.makedirs(os.path.join(cwd, folder), exist_ok=True)

    # Move the docx files
    move_docx_files(r"./", r"./data/text/raw_docx")
    move_xlsx_files(r"./", r"./data/raw")