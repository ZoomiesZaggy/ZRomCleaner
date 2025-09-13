import subprocess
import sys


def run_script(args):
    return subprocess.run(
        [sys.executable, "zrom_cleaner.py", *args], capture_output=True, text=True, check=True
    )


def test_trace_level_with_double_v():
    result = run_script(["-vv"])
    output = result.stdout + result.stderr
    assert "Trace level active" in output


def test_trace_level_not_enabled_with_single_v():
    result = run_script(["-v"])
    output = result.stdout + result.stderr
    assert "Trace level active" not in output
