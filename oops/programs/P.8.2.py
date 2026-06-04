# context_manager.py
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc, tb):
        self.f.close()
        # return False  # re-raise any exception if True/False as needed

with FileOpener("test.txt", "w") as f:
    f.write("Hello")

# using contextlib
from contextlib import contextmanager

@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()

with open_file("test2.txt", "w") as f:
    f.write("Hi again")
