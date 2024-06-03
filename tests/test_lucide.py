from __future__ import annotations

from xml.etree import ElementTree

import pytest

import lucide


def test_load_icon_success_outline():
    svg = lucide._load_icon("a-arrow-down")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_solid():
    svg = lucide._load_icon("a-arrow-down")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_mini():
    svg = lucide._load_icon("a-arrow-down")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_fail_unknown():
    with pytest.raises(lucide.IconDoesNotExist) as excinfo:
        lucide._load_icon("hoome")

    assert excinfo.value.args == ("The icon 'hoome' does not exist.",)
