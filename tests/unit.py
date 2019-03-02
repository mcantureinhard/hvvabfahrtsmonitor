import pytest
from hvvabfahrtsmonitor.hvvabfahrtsmonitor import HvvAbfahrtsmonitor


def test_init():
    obj = HvvAbfahrtsmonitor("hvv.json", "hvv-schema.json")
    assert obj != None

def test_regex():
    obj = HvvAbfahrtsmonitor("hvv.json", "hvv-schema.json")

    match_positive_integer = obj.regex.search("+5")
    assert match_positive_integer.group(1) == "+"
    assert match_positive_integer.group(2) == "5"

    match_signless_integer = obj.regex.search("5")
    assert match_signless_integer == None

    match_negative_integer = obj.regex.search("-3")
    assert match_negative_integer.group(1) == "-"
    assert match_negative_integer.group(2) == "3"

    match_zero = obj.regex.search("+0")
    assert match_zero.group(1) == "+"
    assert match_zero.group(2) == "0"

def test_request():
    obj = HvvAbfahrtsmonitor("hvv.json", "hvv-schema.json")

    assert obj._request("") == None
    assert obj._request("www.google.com") == None
    assert obj._request("https://abfahrten.hvv.de/api/monitors/a038583f-f72b-4e4e-ba22-9d9903ced316") != None
