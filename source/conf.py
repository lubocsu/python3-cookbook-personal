# -*- coding: utf-8 -*-
#
# python3-cookbook documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 19 03:21:45 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ['chinese_search']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'python3-cookbook'
copyright = u'2015, 熊能'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0.0'

exclude_patterns = []

html_theme = 'default'

# html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'python3-cookbook doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements={# The paper size ('letterpaper' or 'a4paper').
'papersize':'a4paper',# The font size ('10pt', '11pt' or '12pt').
'pointsize':'12pt','classoptions':',oneside','babel':'',#必須
'inputenc':'',#必須
'utf8extra':'',#必須
# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{ctex}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
% \setCJKmainfont{WenQuanYi Micro Hei}
% \setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
% \setCJKfamilyfont{song}{WenQuanYi Micro Hei}
% \setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\usepackage{titlesec}
\newcommand{\sectionbreak}{\clearpage}
\newcommand\normalsectioning{\setcounter{secnumdepth}{2}}
\newcommand\specialsectioning{\setcounter{secnumdepth}{-2}}
"""}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'python3-cookbook.tex', u'《Python Cookbook》第三版',
   u'熊能', 'howto'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'python3-cookbook', u'《Python Cookbook》第三版',
     [u'熊能'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'python3-cookbook', u'《Python Cookbook》第三版',
   u'熊能', 'python3-cookbook', '《Python Cookbook》第三版',
   'Miscellaneous'),
]


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'sphinx_rtd_theme'
# otherwise, readthedocs.org uses their theme by default, so no need to specify it
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'navigation_depth': 2,
}

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))
