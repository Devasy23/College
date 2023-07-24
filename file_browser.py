# import os
# import json

# def create_file_structure_json(directory):
#     file_structure = {}
#     file_structure["semesters"] = []
#     for semester in os.listdir(directory):
#         semester_path = os.path.join(directory, semester)
#         if os.path.isdir(semester_path):
#             semester_dict = {"name": semester, "subjects": []}
#             for subject in os.listdir(semester_path):
#                 subject_path = os.path.join(semester_path, subject)
#                 if os.path.isdir(subject_path):
#                     subject_dict = {"name": subject, "practicals": [], "notes": [], "presentations": []}
#                     for file in os.listdir(subject_path):
#                         file_path = os.path.join(subject_path, file)
#                         if os.path.isfile(file_path):
#                             if file.endswith(".py"):
#                                 subject_dict["practicals"].append(file)
#                             elif file.endswith(".pdf"):
#                                 subject_dict["notes"].append(file)
#                             elif file.endswith(".pptx"):
#                                 subject_dict["presentations"].append(file)
#                     semester_dict["subjects"].append(subject_dict)
#             file_structure["semesters"].append([semester_dict])
#     with open("file_structure.json", "w") as f:
#         json.dump(file_structure, f, indent=4)

# if __name__ == "__main__":
#     create_file_structure_json("C:/Users/Owner/OneDrive - nirmauni.ac.in/Desktop/College")

import os
import json

def generate_file_structure(root_path):
    file_structure = create_folder_object(root_path)
    return file_structure

def create_folder_object(folder_path):
    folder_name = os.path.basename(folder_path)
    folder_object = {"name": folder_name, "path": folder_path, "contents": []}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            file_object = {"name": item}
            folder_object["contents"].append(file_object)
        elif os.path.isdir(item_path):
            subfolder_object = create_folder_object(item_path)
            folder_object["contents"].append(subfolder_object)
    return folder_object

def find_folder_by_path(data, folder_path):
    folders = folder_path.split('/')
    current_folder = data
    for folder in folders:
        current_folder = next((f for f in current_folder["contents"] if f["name"] == folder), None)
        if current_folder is None:
            return None
    return current_folder

# Specify the root folder path to generate the file structure
root_folder = "C:/Users/Owner/OneDrive - nirmauni.ac.in/Desktop/College"

# Generate the file structure
file_structure = generate_file_structure(root_folder)

# Save the file structure to file_structure.json
with open("file_structure.json", "w") as file:
    json.dump(file_structure, file, indent=4)

