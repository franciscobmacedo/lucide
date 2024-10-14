# lucide
<p align="start">
  <a href="https://github.com/franciscobmacedo/lucide">
    <img src="https://raw.githubusercontent.com/franciscobmacedo/lucide/refs/heads/main/docs/images/logo.png" alt="Lucide - Beautiful & consistent icon toolkit made by the community. Open-source project and a fork of Feather Icons." width="200">
  </a>
</p>

<a href="https://github.com/franciscobmacedo/lucide/actions?workflow=CI">
    <img
        src="https://img.shields.io/github/actions/workflow/status/franciscobmacedo/lucide/main.yml.svg?branch=main&style=for-the-badge"
        alt="CI"
        style="max-width: 100%;"
    >
</a>
<a href="https://pypi.org/project/lucide/">
    <img
        src="https://img.shields.io/pypi/v/lucide.svg?style=for-the-badge"
        alt="pypi"
        style="max-width: 100%;"
    >
</a>
<a href="https://github.com/psf/black">
    <img
        src="https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge"
        alt="black"
        style="max-width: 100%;"
    >
</a>
<a href="https://github.com/pre-commit/pre-commit">
    <img
        src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge"
        alt="pre-commit"
        style="max-width: 100%;"
    >
</a>


Use [lucide icons](https://lucide.dev/) in your Django and Jinja templates.

## Requirements

Python 3.8 to 3.12 supported.

Django 3.2 to 5.0 supported.

## Usage

The `lucide` package supports both Django templates and Jinja templates.
Follow the appropriate guide below.

### Django templates

1.  Install with `python -m pip install lucide[django]`.

2.  Add to your `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        ...,
        "lucide",
        ...,
    ]
    ```

3. Now your templates can load the template library with:

    ```django
        {% load lucide %}
    ```

Alternatively, make the library available in all templates by adding it to [the builtins option](https://docs.djangoproject.com/en/stable/topics/templates/#django.template.backends.django.DjangoTemplates>):

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # ...
        "OPTIONS": {
            # ...
            "builtins": [
                ...,
                "lucide.templatetags.lucide",
                ...,
            ],
        },
    }
]
```

The library provides one tag (`lucide`) to render SVG icons which can take these arguments:

- `name`, positional: the name of the icon to use. You can see the icon names on the [lucide grid](https://lucide.dev/icons/).

- `size`, keyword: an integer that will be used for the width and height attributes of the output `<svg>` tag.
  Defaults to the icons’ designed sizes, `24`.
  It can also be `None`, in which case no width or height attributes will be output.

- Any number of keyword arguments.
  These will be added as attributes in the output HTML.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. `data-` attributes.


Most attributes will be added to the `<svg>` tag containing the icon, but these attributes will be attached to the inner `<path>` tags instead:

  - `stroke-linecap`
  - `stroke-linejoin`
  - `vector-effect`

> Note: unlike the SVG code you can copy from [lucide grid](https://lucide.dev/icons/), there is no default `class`.

#### Examples

An "a-arrow-down” icon:

```django
    {% lucide "a-arrow-down" %}
```

The same icon at 40x40 pixels, and a CSS class:

```django
    {% lucide "a-arrow-down" size=40 class="mr-4" %}
```

That icon again, but with the paths changed to a narrower stroke width, and a "data-controller" attribute declared:

```django
    {% lucide "a-arrow-down" stroke_width=1 data_controller="language" %}
```

### Jinja templates

1. Install with `python -m pip install lucide[jinja]`.

2. Adjust your Jinja `Environment` to add the global `lucide` function from `lucide.jinja`.
   For example:

   ```python
       from lucide.jinja import lucide
       from jinja2 import Environment

       env = Environment()
       env.globals.update({
               "lucide": lucide
           }
       )
    ```
3. Now in your templates you can call that function, which will render the corresponding `<svg>` icons. The function takes these arguments:

- `name`, positional: the name of the icon to use.
  You can see the icon names on the [lucide grid](https://lucide.dev/icons/)

- `size`, keyword: an integer that will be used for the width and height attributes of the output `<svg>` tag.
  Defaults to the icons’ designed sizes, `24`.
  Can be `None`, in which case no width or height attributes will be output.

- Any number of keyword arguments.
  These will be added as HTML attributes to the output HTML.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. `data-` attributes.

Most attributes will be added to the `<svg>` tag containing the icon, but these attributes will be attached to the inner `<path>` tags instead:

  - `stroke-linecap`
  - `stroke-linejoin`
  - `vector-effect`

> Note: unlike the SVG code you can copy from [lucide grid](https://lucide.dev/icons/), there is no default `class`.

#### Examples

An "a-arrow-down” icon:

```jinja
    {{ lucide("a-arrow-down") }}
```

The same icon at 40x40 pixels and a CSS class:

```jinja
    {{ lucide("a-arrow-down", size=40, class="mr-4") }}
```

That icon again, but with the paths changed to a narrower stroke width, and a "data-controller" attribute declared:

```jinja
    {{ lucide("a-arrow-down", stroke_width=1, data_controller="language") }}
```

## Acknowledgements

This package is heavely inspired by [Adam Johnson's heroicons](https://github.com/adamchainz/heroicons). It's actually mostly copied from it so a huge thanks Adam!
