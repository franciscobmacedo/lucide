from __future__ import annotations

from jinja2 import DictLoader
from jinja2 import Environment

from lucide.jinja import lucide


def make_environment(index_template: str) -> Environment:
    env = Environment(loader=DictLoader({"index": index_template}))
    env.globals.update(
        {
            "lucide": lucide,
        }
    )
    return env


def test_success_icon():
    env = make_environment('{{ lucide("a-arrow-down") }}')
    template = env.get_template("index")

    result = template.render()

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M3.5 13h6" />\n  <path d="m2 16 4.5-9 4.5 9" />\n  <path d="M18 7v9" />\n  <path d="m14 12 4 4 4-4" />\n</svg>'
        # fmt: on
    )


def test_success_icon_path_attr():
    env = make_environment('{{ lucide("a-arrow-down", stroke_linecap="butt") }}')
    template = env.get_template("index")

    result = template.render()

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M3.5 13h6" stroke-linecap="butt" />\n  <path d="m2 16 4.5-9 4.5 9" stroke-linecap="butt" />\n  <path d="M18 7v9" stroke-linecap="butt" />\n  <path d="m14 12 4 4 4-4" stroke-linecap="butt" />\n</svg>'
        # fmt: on
    )


def test_success_icon_complete():
    env = make_environment(
        '{{ lucide("a-arrow-down", size=48, class="h-4 w-4", ' + 'data_test="a < 2") }}'
    )
    template = env.get_template("index")

    result = str(template.render())

    assert result == (
        # fmt: off
        '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" data-test="a &lt; 2">\n  <path d="M3.5 13h6" />\n  <path d="m2 16 4.5-9 4.5 9" />\n  <path d="M18 7v9" />\n  <path d="m14 12 4 4 4-4" />\n</svg>'
        # fmt: on
    )


def test_success_icon_size_none():
    env = make_environment('{{ lucide("a-arrow-down", size=None) }}')
    template = env.get_template("index")

    result = template.render()

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M3.5 13h6" />\n  <path d="m2 16 4.5-9 4.5 9" />\n  <path d="M18 7v9" />\n  <path d="m14 12 4 4 4-4" />\n</svg>'
        # fmt: on
    )
