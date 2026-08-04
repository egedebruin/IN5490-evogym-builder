#!/usr/bin/env python3

import subprocess
from pathlib import Path

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

HPC = "eged@hpc.robin.uiocloud.no"

REMOTE_RESULTS = "~/evogym-bayesian-optimization/in5490/"

LOCAL_RESULTS = "../evogym-bayesian-optimization/in5490"

# ---------------------------------------------------------------------


def run(cmd):
    print("> " + " ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True)


print("\n=== Copying results from HPC ===\n")

run([
    "rsync",
    "-avz",
    "--progress",
    f"{HPC}:{REMOTE_RESULTS}",
    str(LOCAL_RESULTS),
])

print("\nDone!")
print(f"Results copied to:\n{LOCAL_RESULTS}")