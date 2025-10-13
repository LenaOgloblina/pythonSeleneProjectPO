import os


def resource_path(file_name):
    correct_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.dirname(correct_dir)
    resources_dir = os.path.join(project_root, 'tests', 'resources')
    file_path = os.path.join(resources_dir, file_name)
    return file_path

# def resource_path(file_name):
#     correct_dir = os.path.abspath(os.path.dirname(__file__))
#     resources_dir = os.path.join(correct_dir, 'tests', 'resources')
#     file_path = os.path.join(resources_dir, file_name)
#     return file_path

