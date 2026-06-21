# /home/raul/projects/sysmon/CONTRIBUTING.md

> "Executing contributing guide..."
> [OK] Guidelines loaded.
> [OK] Standards checked.
> [OK] Ready for pull requests.

Thank you for your interest in contributing to the Linux System Resource Monitor! All forms of contribution, bug reports, and documentation improvements are welcome.

---

## /usr/bin/prerequisites

Before you start, make sure you have the following system-level tools installed:

* **Python 3.6+** with Tkinter support.
* **GCC** (GNU Compiler Collection) or any standard C compiler.
* **GNU Make** for build automation.

On Debian or Ubuntu-based distributions, you can install these by running:
```bash
sudo apt update && sudo apt install -y python3-tk gcc make
```

---

## /home/raul/projects/sysmon/layout

The code is organized to cleanly separate interface logic, the background C engine, and static resources:

* `src/`: Contains all source files.
    * `assets/`: Static image files.
        * `logo.png`: Main graphical interface icon.
    * `main.py`: Main Python script. Draws the GUI and handles sensor queries.
    * `temperature.py`: Temperature sensor querying logic.
    * `cpu.c`: High-efficiency C engine that parses /proc/stat.
* `Makefile`: Automates building, running, and cleaning the repository.
* `requirements.txt`: Outlines system package requirements.
* `LICENSE`: Apache License 2.0.

---

## /usr/bin/workflow

Use the predefined Makefile tasks to facilitate your development cycle:

### 1. Compile the C Engine
Builds the src/cpu.c file and outputs the src/cpu_motor executable:
```bash
make
```

### 2. Run the Application
Builds the engine if missing and launches the graphical interface:
```bash
make run
```

### 3. Clean the Environment
Deletes the compiled binary and Python's caching directories (__pycache__):
```bash
make clean
```

---

## /etc/standards

When submitting pull requests, please respect the following guidelines:

### Python
* **Portability:** Avoid hardcoded relative file paths that assume a specific working directory (e.g. open('logo.png')). Always use `BASE_DIR = os.path.dirname(os.path.abspath(__file__))` and resolve paths via `os.path.join()`.
* **Readability:** Follow PEP 8 guidelines.
* **Error Handling:** Safely catch subprocess execution errors and file sensor read errors to prevent GUI crashes.

### C
* **Optimization and Safety:** Keep the C engine clean, fast, and optimized. Always release file descriptors using `fclose()`.
* **Output Format:** The C engine must output *only* the calculated usage percentage (e.g., `12.50%`) and exit with status `0` on success. This format ensures Python can parse it without issues.

---
"Programs must be written for people to read, and only incidentally for machines to execute." - Harold Abelson
