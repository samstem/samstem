from edbook.conf import *  # type: ignore
extensions.append('sphinxcontrib.katex')
extensions.remove('sphinx.ext.mathjax')

import sphinxcontrib.katex as katex

#latex_macros = r"""
#    \def \sclar          #1#2{\left\langle#1,#2\right\rangle}
#    \def \mol              {\text{mol}}
#    \def \e              #1{\mathrm{e}^{#1}}
#    \def \vec            #1{\mathbf{#1}}
#    \def \x                {\vec{x}}
#    \def \d                {\operatorname{d}\!}
#    \def \dirac          #1{\operatorname{\delta}\left(#1\right)}
#    \def \scalarprod   #1#2{#1\ \mathrm{#2}}
#    \def \bleh   #1#2{#1\ \mathrm{#2}}
#"""

# Translate LaTeX macros to KaTeX and add to options for HTML builder
#katex_macros = katex.latex_defs_to_katex_macros(latex_macros)
#katex_options = 'macros: {' + katex_macros + '}'

katex_options = r'''macros: {
  "\\SI": "{#1\\;\\mathrm{#2}}",
  "\\squared": "{^{2}}",
  "\\cubed": "{^{3}}",
  "\\per": "/",
  "\\tera": "T",
  "\\giga": "G",
  "\\mega": "M",
  "\\kilo": "k",
  "\\milli": "m",
  "\\micro": "μ",
  "\\nano": "n",
  "\\kilogram": "\\text{kg}\\,",
  "\\meter": "\\text{m}\\,",
  "\\second": "\\text{s}\\,",
  "\\ampere": "\\text{A}\\,",
  "\\kelvin": "\\text{K}\\,",
  "\\mol": "\\text{mol}\\,",
  "\\candela": "\\text{cd}\\,",
  "\\newton": "\\text{N}\\,",
  "\\hertz": "\\text{Hz}\\,",
  "\\pascal": "\\text{Pa}\\,",
  "\\volt": "\\text{V}\\,",
  "\\watt": "\\text{W}\\,",
  "\\joule": "\\text{J}\\,",
  "\\henry": "\\text{H}\\,",
  "\\farad": "\\text{F}\\,",
  "\\coulomb": "\\text{C}\\,",
  "\\ohm": "\\Omega\\,",
  "\\weber": "\\text{Wb}\\,",
  "\\tesla": "\\text{T}\\,",
  "\\degree": "\\text{deg}\\,"
  }'''

