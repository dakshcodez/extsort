# 🗂️ extsort

**extsort** is a lightweight Python utility that organizes files in a folder based on their file extensions. It helps keep your workspace clean by grouping files into language- or type-specific folders like python, video, pdf, and more.

---

## 📦 Features

- Automatically organizes files into folders by extension
- Deletes executable files for cleanup (optional behavior)
- Skips files with no extension
- Easy to configure using .env and a customizable mapping
- Written in clean, modular Python

---

## 📁 Example

Before:

```
/myfolder
├── main.py
├── resume.pdf
├── video.mp4
├── notes.txt
├── installer.run
```

After running `extsort`:

```
/myfolder
├── python/
│   └── main.py
├── pdf/
│   └── resume.pdf
├── video/
│   └── video.mp4
├── text_file/
│   └── notes.txt
```

> Executable file `installer.run` is deleted.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/dakshcodez/extsort.git
cd extsort
```

### 2. Install requirements

```bash
pip install python-dotenv
```

### 3. Set up your `.env`

Create a `.env` file in the root directory:

```env
FOLDER_PATH=/full/path/to/your/folder
```

### 4. Run the script

```bash
python main.py
```

---
