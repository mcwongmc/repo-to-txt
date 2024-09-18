import os
import yaml

def read_yaml_file(file_path):
    print(f"Reading YAML file: {file_path}")
    with open(file_path, 'r') as file:
        content = yaml.safe_load(file)
        print(f"Raw YAML content: {content}")
        if isinstance(content, str):
            result = content.split()
        else:
            result = content or []
        print(f"Processed YAML content: {result}")
        return result

def is_ignored_path(path, ignore_folders):
    result = any(ignore_folder in path for ignore_folder in ignore_folders)
    print(f"Checking if path '{path}' is ignored: {result}")
    return result

def get_repo_structure(root_dir, ignore_folders, ignore_files):
    print(f"Getting repo structure. Root: {root_dir}, Ignore folders: {ignore_folders}, Ignore files: {ignore_files}")
    structure = []
    for root, dirs, files in os.walk(root_dir):
        print(f"Processing directory: {root}")
        if is_ignored_path(root, ignore_folders):
            print(f"Ignoring directory: {root}")
            dirs[:] = []  # Don't traverse into ignored directories
            continue
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        structure.append(f'{indent}{os.path.basename(root)}/')
        for file in files:
            if file not in ignore_files:
                structure.append(f'{indent}    {file}')
    return '\n'.join(structure)

def copy_file_content(file_path):
    print(f"Copying content of file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    root_dir = '.'  # Assuming the script is run from the repo root
    print(f"Root directory: {root_dir}")

    ignore_folders = read_yaml_file('ignore-folder.yaml')
    print(f"Ignore folders: {ignore_folders}")

    scan_extensions = read_yaml_file('scan-extension-list.yaml')
    print(f"Scan extensions: {scan_extensions}")

    ignore_files = {'repo-code.txt', 'repo-code.py'}
    print(f"Ignore files: {ignore_files}")

    with open('repo-code.txt', 'w', encoding='utf-8') as output_file:
        print("Writing repo structure...")
        output_file.write("# Repo Structure\n")
        repo_structure = get_repo_structure(root_dir, ignore_folders, ignore_files)
        output_file.write(repo_structure)
        output_file.write("\n\n")

        print("Copying code from files...")
        for root, dirs, files in os.walk(root_dir):
            print(f"Processing directory: {root}")
            if is_ignored_path(root, ignore_folders):
                print(f"Ignoring directory: {root}")
                dirs[:] = []  # Don't traverse into ignored directories
                continue
            for file in files:
                if file not in ignore_files and any(file.endswith(ext) for ext in scan_extensions):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, root_dir)
                    print(f"Writing content of file: {relative_path}")
                    output_file.write(f"---\n# {relative_path}\n")
                    output_file.write(copy_file_content(file_path))
                    output_file.write("\n")

        print("Writing end of repo...")
        output_file.write("---\nEnd of repo")

    print("Process completed.")

if __name__ == "__main__":
    main()