import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitilize(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("hello world") == "Hello world"

def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("  hello world  ") == "hello world  "
    assert string_utils.trim("") == ""

def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("", ",") == []

def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False

def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False

def test_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") is True
    assert string_utils.end_with("SkyPro", "y") is False

def test_is_empty(string_utils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("SkyPro") is False

def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

def test_list_to_string_empty(string_utils):
    assert string_utils.list_to_string([]) == ""