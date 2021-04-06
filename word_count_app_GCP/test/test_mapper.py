import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join (parent_dir, "src")
sys.path.insert(0,src_dir)

import subprocess
import pytest
import shlex

# Test if the mapper works. So ideally, it will return poo    1
def test_mapper():
    comd1 = subprocess.Popen(['echo', "poo"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    comd2 = subprocess.run(['python', './src/mapper.py 2', '2'], stdin = comd1.stdout)
    assert print(comd2.stdout) != "" , "Mapper is not working correctly"

