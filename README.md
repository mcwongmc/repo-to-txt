# Repo-to-TXT

A lightweight and flexible Python tool to generate a text representation of your repository structure and content.

## Features

- **Lightweight**: Pure Python implementation with minimal dependencies.
- **Flexible**: Customizable ignore lists and file extensions to scan.
- **Python-focused**: Designed for Python developers, but can be used for any repository.
- **Minimal dependencies**: Requires only PyYAML, ensuring easy setup and portability.

## Description

Repo-to-TXT is a simple yet powerful tool that scans your repository and generates a single text file containing:

1. A tree-like representation of your repository structure.
2. The content of specified files based on their extensions.

This tool is particularly useful for:

- Quickly sharing your project structure and key file contents.
- Creating a snapshot of your repository for documentation purposes.
- Facilitating code reviews by providing an easy-to-read overview of your project.

## How it works

1. The script reads configuration from YAML files:
   - `ignore-folder.yaml`: List of folders to ignore during scanning.
   - `scan-extension-list.yaml`: List of file extensions to include in the content copying process.

2. It generates a tree-like structure of your repository, excluding ignored folders and files.

3. For each file with a specified extension, it copies the content into the output file.

4. The result is saved in a single `repo-code.txt` file.

## Usage

1. Place the `repo_code.py` script in the root of your repository.
2. Create and configure the `ignore-folder.yaml` and `scan-extension-list.yaml` files.
3. Install the required dependencies:

```
pip install pyyaml
```


4. Run the script:
```
python repo_code.py
```


5. Find the generated `repo-code.txt` file in the same directory.

### **Using with LLMs**

Once you have the `repo-code.txt` file, you can leverage it with Language Learning Models (LLMs) for various purposes:

- **Attach to Supported Chats**: Upload the `repo-code.txt` to any chat platform that supports text file attachments, such as Google AI Studio.
- **Copy and Paste**: Copy the content of `repo-code.txt` and paste it directly into any LLM chat interface that can handle long contexts.
- **Ask Questions**: Use the uploaded or pasted code to ask questions, analyze the code, or get explanations from the LLM.

### **Code Privacy**

When using `repo-code.txt` with LLM providers, it's essential to be aware of their privacy policies:

- **Privacy Considerations**: Ensure you understand how the LLM provider handles and stores your data. Avoid sharing sensitive or proprietary code unless you are confident in the provider's privacy measures.
- **Responsibility Disclaimer**: This repository serves solely as a tool to generate text representations of your code. We are not responsible for any privacy issues that may arise from sharing your code with third-party LLM services.

## Configuration

### ignore-folder.yaml

List the folders you want to exclude from the scanning process. For example:

```yaml
- .git
- node_modules
- venv
```


### scan-extension-list.yaml 

List the file extensions you want to include in the content copying process. For example:
- .py
- .md
- .txt



## **Benefits**

- **Lightweight**: The script is small and efficient, with minimal impact on your system resources.
- **Flexible**: Easily customize which folders to ignore and which file types to include.
- **Python focus**: Designed with Python projects in mind, but versatile enough for any repository.
- **Minimal dependencies**: Requires only PyYAML, simplifying installation and reducing potential conflicts.

## **Requirements**

- Python 3.x
- [PyYAML](https://pyyaml.org/) 

## **Installation**

1. Clone this repository or download the `repo_code.py` file.
2. Install the required dependencies:
    
    ```
    
    pip install pyyaml
    
    ```
    
3. Place the script and configuration files in your repository root.

## **Contributing**

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/yourusername/repo-to-txt/issues) if you want to contribute.

## **License**

This project is licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0).

## **Author**

MC Wong

---

Happy coding!