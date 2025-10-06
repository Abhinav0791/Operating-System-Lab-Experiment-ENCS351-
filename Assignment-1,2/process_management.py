#!/usr/bin/env python3
import os
import time
import subprocess

def task1_create_children(n=3):
    print(f"\n--- Task 1: Creating {n} child processes ---")
    children = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child #{i}: PID={os.getpid()}, PPID={os.getppid()}")
            os._exit(0)
        else:
            children.append(pid)
    for _ in range(len(children)):
        os.wait()

def task2_exec_commands(cmds=None):
    if cmds is None:
        cmds = [['/bin/ls', '-l'], ['/bin/date'], ['/bin/ps', 'aux']]
    print("\n--- Task 2: Executing commands ---")
    for i, cmd in enumerate(cmds):
        pid = os.fork()
        if pid == 0:
            try:
                os.execvp(cmd[0], cmd)
            except Exception:
                os._exit(1)
        else:
            os.wait()

def task3_zombie_and_orphan():
    print("\n--- Task 3: Zombie and Orphan Demo ---")
    pid = os.fork()
    if pid == 0:
        os._exit(0)
    else:
        time.sleep(5)
        subprocess.run(["ps", "-el"])
        os.wait()
    pid2 = os.fork()
    if pid2 == 0:
        time.sleep(4)
        print(f"Orphan child PID={os.getpid()} new PPID={os.getppid()}")
        os._exit(0)
    else:
        return

def task4_inspect_proc(pid):
    print(f"\n--- Task 4: Inspecting /proc/{pid} ---")
    base = f"/proc/{pid}"
    try:
        with open(os.path.join(base, "status")) as f:
            print("\n".join(f.read().splitlines()[:10]))
    except Exception:
        pass
    try:
        print("exe ->", os.readlink(os.path.join(base, "exe")))
    except Exception:
        pass
    try:
        print("open fds ->", os.listdir(os.path.join(base, "fd")))
    except Exception:
        pass

def cpu_intensive_work(n=2000000):
    s = 0
    for i in range(n):
        s += i % 7
    return s

def task5_priority_nice(children=3):
    print("\n--- Task 5: Priority Demo ---")
    results = {}
    for i in range(children):
        r, w = os.pipe()
        pid = os.fork()
        if pid == 0:
            os.close(r)
            try:
                os.nice(i * 5)
            except Exception:
                pass
            start = time.time()
            cpu_intensive_work()
            end = time.time()
            os.write(w, f"{os.getpid()},{i*5},{end-start}\n".encode())
            os.close(w)
            os._exit(0)
        else:
            os.close(w)
            data = os.read(r, 1024).decode().strip()
            if data:
                pid_s, nice_s, dur_s = data.split(",")
                results[int(pid_s)] = (int(nice_s), float(dur_s))
            os.close(r)
            os.wait()
    for pid, (nice_v, dur) in results.items():
        print(f"{pid} -> nice={nice_v}, time={dur:.3f}s")

def main():
    task1_create_children(3)
    task2_exec_commands()
    task3_zombie_and_orphan()
    task4_inspect_proc(os.getpid())
    task5_priority_nice(3)

if __name__ == "__main__":
    main()
