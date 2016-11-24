import os
import unittest

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
  # let exception propagate if we just can't
  # cd into the specified directory
  os.chdir(whatever)

def get_parent_dir(directory):
    return os.path.abspath(directory)

def goUpOneDirectory():
    current_dirs_parent = get_parent_dir(os.getcwd())
    os.chdir(current_dirs_parent)

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testGetParentDir(self):
        print(get_parent_dir(os.getcwd()))

def main():
    unittest.main()

if __name__ == '__main__':
    main()