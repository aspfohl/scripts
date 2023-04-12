import os
import time

from mcli.sdk import update_run_metadata

steps = 60
run_name = os.environ.get('RUN_NAME')

for step in range(steps):

    metadata = {
        "step": step,
        "last_updated": time.time(),
        "wallclock/remaining_estimate": f"{steps - step} seconds",
    }
    update_run_metadata(run_name, metadata)
    print(f"{step}: Updated metadata for {run_name} {metadata}")

    time.sleep(1)
