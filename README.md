OS Lab Experiment 1 – Process Management in Python

This repository contains the solution for Lab Experiment-1, demonstrating process creation and management in a Linux environment using Python's os and subprocess modules.

---

Description

This project simulates core operating system concepts by implementing various process management operations:

- Process Creation: Using os.fork() to spawn child processes.
- Command Execution: Using os.execvp() to run system commands from child processes.
- Zombie and Orphan Processes: Demonstrates the creation and handling of special process states.
- Process Inspection: Reads /proc filesystem entries to examine process details.
- Process Prioritization: Adjusts process priority using os.nice() to observe execution timing effects.

This lab provides a practical understanding of process behavior, inter-process communication, and priority scheduling.

---

Requirements

- Python 3.0 or above
- Linux-based OS (e.g., Ubuntu, Fedora, or WSL on Windows)
  Note: The script relies on os.fork() and the /proc filesystem, which are not available on native Windows.

---

File Structure

- process_management.py – Main Python script implementing all tasks.
- output.txt – Sample outputs generated after running the tasks.
- report.pdf – Lab report summarizing objectives, code, and results.
- README.txt – This file.

---

How to Run

1. Clone the repository

git clone https://github.com/Abhinav0791/Operating-System-Lab-Experiment_ENCS351
cd <repository-folder>

2. Make the script executable

chmod +x process_management.py

3. Run the script

The script supports specific tasks via command-line arguments:

Task 1 – Process Creation
Creates 3 child processes and prints their PID information:

python3 process_management.py --task1 3

---

Task 2 – Command Execution
Executes system commands (ls, date, ps) in child processes:

python3 process_management.py --task2 ls -l date "ps aux"

---

Task 3 – Zombie & Orphan Processes
Simulates special process states:

# Zombie process simulation
python3 process_management.py --zombie

# Orphan process simulation
python3 process_management.py --orphan

---

Task 4 – Inspect /proc
Inspect details of a specific process using its PID:

# Get the PID of your shell
echo $$

# Inspect the process
python3 process_management.py --inspect <PID>

---

Task 5 – Process Prioritization
Creates CPU-bound child processes with different nice values and measures execution times:

python3 process_management.py --priority

---

Notes

- Ensure you run the script on a Linux-like system; functionality depends on fork() and /proc.
- Use ps commands in a separate terminal to observe zombie or orphan processes in real-time.

---
