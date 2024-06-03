from __future__ import annotations

from django import template
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe

import lucide as _lucide

register = template.Library()


@register.simple_tag
def lucide(name: str, *, size: int | None = 24, **kwargs: object) -> str:
    return _render_icon(name, size, **kwargs)


def _render_icon(name: str, size: int | None, **kwargs: object) -> str:
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    fixed_kwargs = {
        key: (value + "" if isinstance(value, SafeString) else value)
        for key, value in kwargs.items()
    }
    return mark_safe(_lucide._render_icon(name, size, **fixed_kwargs))
