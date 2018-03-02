(TeX-add-style-hook
 "mqnotes"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("tufte-book" "a4paper" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("mdframed" "framemethod=TikZ")))
   (TeX-run-style-hooks
    "latex2e"
    "tufte-book"
    "tufte-book11"
    "amsmath"
    "cancel"
    "amsfonts"
    "amssymb"
    "graphicx"
    "siunitx"
    "physics"
    "nicefrac"
    "unicode-math"
    "mdframed"
    "xcolor"
    "mathrsfs")
   (TeX-add-symbols
    "Ham"
    "Hil"
    "oh"
    "moh"
    "eqdef")
   (LaTeX-add-labels
    "chap:iq"
    "sec:evol"
    "eq:xina"
    "eq:pina"
    "eq:cuatrbatman"
    "eq:matame")
   (LaTeX-add-counters
    "example"))
 :latex)

