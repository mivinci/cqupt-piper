import base64
from os import remove


def b64enc(s: any) -> str:
    if not isinstance(s, str):
        s = str(s)
    return base64.b64encode(str.encode(s)).decode()


def b64dec(s: str) -> str:
    return base64.b64decode(s).decode()


def b64_fwrite(filename: str, data: any) -> int:
    try:
        with open(filename, 'w') as f:
            return f.write(b64enc(data))
    except FileExistsError:
        raise


def b64_fread(filename: str) -> str:
    try:
        with open(filename, 'r') as f:
            return b64dec(f.read())
    except FileExistsError:
        remove(filename)
        raise