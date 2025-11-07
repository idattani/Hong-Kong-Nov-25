
# Google Colab User Guide

Google Colaboratory (Colab) is a free, cloud-based Jupyter notebook environment provided by Google that allows you to write, execute, and share Python code through your browser.

---

## 1. Getting Started

### 1.1 What is Google Colab?
Google Colab provides a hosted environment for running Jupyter notebooks without requiring any local setup. It supports Python and provides free access to computing resources, including GPUs and TPUs.

### 1.2 How to Access Colab
- Go to [https://colab.research.google.com](https://colab.research.google.com)
- Log in with your Google account.
- You can either:
  - **Create a new notebook** (`File` → `New notebook`)
  - **Upload an existing notebook** (`File` → `Upload notebook`)
  - **Open from Google Drive** or **GitHub**.

---

## 2. Colab Interface Overview

### 2.1 Notebook Structure
- **Code cells**: Contain Python code that you can execute.
- **Text cells (Markdown)**: Contain formatted text, including equations, images, and links.
- **Output cells**: Display results, plots, or logs after code execution.

### 2.2 Toolbar Functions
- **File**: Create, open, upload, or download notebooks.
- **Edit**: Undo/redo, cut, copy, paste, or clear outputs.
- **View**: Toggle line numbers, output visibility, and themes.
- **Runtime**: Run, interrupt, or restart the runtime environment.
- **Tools**: Access keyboard shortcuts and settings.

---

## 3. Writing and Running Code

### 3.1 Running a Code Cell
- Press `Shift + Enter` or click the **Run** button.
- You can run all cells with `Runtime → Run all`.

### 3.2 Adding New Cells
- Add a **code cell** or **text cell** via the `+ Code` or `+ Text` buttons.

### 3.3 Editing Text Cells
Text cells use Markdown syntax. For example:

```markdown
# Heading 1
**Bold text** and *italic text*
- Bullet list item
1. Numbered item
```

---

## 4. Managing Files and Data

### 4.1 Accessing Google Drive
You can mount your Google Drive to Colab:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Once mounted, you can access files like any local directory under `/content/drive/MyDrive/`.

### 4.2 Uploading Files
- Click the **folder icon** on the left sidebar.
- Use the upload button to add local files.
- Alternatively, use:
```python
from google.colab import files
uploaded = files.upload()
```

---

## 5. Using GPUs and TPUs

### 5.1 Enabling Accelerated Hardware
- Go to `Runtime → Change runtime type`
- Under **Hardware accelerator**, select **GPU** or **TPU**.

### 5.2 Checking GPU Access
```python
!nvidia-smi
```

---

## 6. Installing and Importing Packages

You can install any Python package using `pip`:
```python
!pip install package_name
```

Example:
```python
!pip install numpy pandas matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

## 7. Sharing and Collaboration

### 7.1 Sharing Notebooks
Colab notebooks are stored in Google Drive and can be shared like any Google Doc:
- Click **Share**
- Choose permission levels: Viewer, Commenter, or Editor.

### 7.2 Version Control
- Use `File → Save a copy in Drive` for backup.
- You can also save to GitHub: `File → Save a copy to GitHub`.

---

## 8. Exporting and Downloading

You can download notebooks in several formats:
- `.ipynb` (native Jupyter format)
- `.py` (Python script)
- `.pdf` or `.html` via `File → Download`.

Example command:
```python
from google.colab import files
files.download('my_notebook.ipynb')
```

---

## 9. Useful Tips and Tricks

- Use `!` to run shell commands (e.g., `!ls`, `!pip install`).
- Use `%%time` or `%%timeit` for timing code execution.
- Use `%matplotlib inline` for displaying plots inline.
- Save checkpoints automatically by enabling “Save to Drive.”
- Use keyboard shortcuts like `Ctrl + M + B` to add a new cell below.

---

## 10. Troubleshooting Common Issues

| Problem | Possible Solution |
|----------|--------------------|
| **Runtime disconnects** | Reconnect or save work frequently. Consider using Colab Pro for longer sessions. |
| **Module not found** | Reinstall missing library with `!pip install module_name`. |
| **GPU not detected** | Ensure GPU is enabled under `Runtime → Change runtime type`. |
| **File not found** | Confirm file path or re-upload/mount Google Drive. |

---

## 11. Additional Resources

- [Colab Official Documentation](https://research.google.com/colaboratory/)
- [Jupyter Notebook Documentation](https://jupyter.org/documentation)
- [Google Colab GitHub Repository](https://github.com/googlecolab/colabtools)

---

**Author:** ChatGPT  
**Last Updated:** November 2025
