from pathlib import Path


def getResource(rel_path):
    res_path = Path(__file__).parent.parent / 'res' / rel_path
    return res_path.resolve().as_posix()


if __name__ == '__main__':
    res = getResource("speech.png")
    print(res)
