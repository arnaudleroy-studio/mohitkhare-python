# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "mohitkhare"
copyright = "2026, Mohit Khare"
author = "Mohit Khare"
release = "0.1.0"

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_nav_header_background": "#2c3e50",
}

html_context = {
    "display_github": True,
    "github_user": "arnaudleroy-studio",
    "github_repo": "mohitkhare-python",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
