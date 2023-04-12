
import os, argparse, time
from mcli.sdk import update_run_metadata

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, required=True)
args = parser.parse_args()

run_name = os.environ.get('RUN_NAME')
metadata = {"step": args.n, "wallclock/remaining_estimate": f"{30 - args.n} seconds"}
update_run_metadata(run_name, metadata)
print(f"{args.n}: Updated metadata for {run_name} {metadata}")

time.sleep(1)
