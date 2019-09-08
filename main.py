from CQUPTPiper.piper import cli
from sys import stdout
import time


if __name__ == "__main__":
    cli()

    # for i in range(10):
    #     print("Loading" + "." * i)
    #     stdout.write("\033[F") # Cursor up one line
    #     time.sleep(0.5)
