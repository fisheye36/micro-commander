import time
from pathlib import Path


def getResource(rel_path):
    res_path = Path(__file__).parent.parent / 'res' / rel_path
    return res_path.resolve().as_posix()

def get_current_time():
    """Return Current Time in MS."""

    return int(round(time.time() * 1000))


if __name__ == '__main__':
    res = getResource("speech.png")
    print(res)
