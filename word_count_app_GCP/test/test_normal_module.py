import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join (parent_dir, "src")
sys.path.insert(0,src_dir)

import pytest
import string
from src.normal_module import SmallDatafile
from string import punctuation

path = "./data/tempest"
#pathname = "This is a test file \n We see how it goes"
def test_init_check_value_are_initialized():
    obj = SmallDatafile(path, 5)
    assert obj.num == 5, "Wrong Number"
    assert obj.pathname == path, "Wrong file directory"
    # test if those objects are empty
    assert len(obj.wordslist) == 0
    assert len(obj.sorted_word) == 0

def test_read_word():
    obj1 = SmallDatafile(path, 5)
    obj1.read_word()
    # Check if the lower transformation is successful
    assert obj1.chosenword.islower() == True
    # Check if the sorted word is list since we implement the print output as the list
    assert isinstance(obj1.sorted_word,list) == True
               