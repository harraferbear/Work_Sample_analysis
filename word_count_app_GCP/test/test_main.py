import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join (parent_dir, "src")
sys.path.insert(0,src_dir)

from src.main import prompt1, prompt2, prompt3
import builtins

input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs

def test_prompt1():
    set_keyboard_input(["1"])

    prompt1()

    output = get_display_output()

    assert output != ""

def test_prompt2():
    set_keyboard_input(["1"])

    prompt2()

    output = get_display_output()

    assert output != ""

def test_prompt3():
    set_keyboard_input([".data/file"])

    prompt3()

    output = get_display_output()

    assert output !=""