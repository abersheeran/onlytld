import os
import copy

from onlytld import set_datapath, get_tld
from onlytld.data import datapath


def test_set_datapath():
    _backup = copy.copy(datapath)
    set_datapath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "list.dat"))

    assert get_tld("abersheeran.com") == "com"
    assert get_tld("aber.sh") is None

    set_datapath(_backup)
