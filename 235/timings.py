import os
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path(os.getenv("TMP", "/tmp"))
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    pass
