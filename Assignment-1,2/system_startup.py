#!/usr/bin/env python3
import multiprocessing
import logging
import time
import random

def setup_logger():
    logging.basicConfig(
        filename="process_log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(processName)s - %(message)s"
    )

def system_process(task_name, duration=None):
    if duration is None:
        duration = random.uniform(1.0, 3.0)
    logging.info(f"{task_name} started")
    time.sleep(duration)
    logging.info(f"{task_name} ended")

def main():
    setup_logger()
    print("System Starting...")
    logging.info("System Starting...")
    tasks = [
        ("Init-Subsystem", 2.0),
        ("Network-Manager", 2.5),
        ("Logger-Service", 1.5),
        ("Scheduler", 2.2)
    ]
    procs = []
    for name, dur in tasks:
        p = multiprocessing.Process(target=system_process, args=(name, dur), name=name)
        procs.append(p)
        p.start()
    for p in procs:
        p.join()
    print("System Shutdown.")
    logging.info("System Shutdown.")

if __name__ == "__main__":
    main()
