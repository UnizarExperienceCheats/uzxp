notes:
	@python -W ignore metaplot.py
	@cd figures && python plotfigs.py && asy *.asy
	@texfot -q lualatex fesiII.tex > /dev/null
	@texfot -q --ignore "This is" --ignore "Overfull" --ignore "arginpar" --ignore "bibentry" lualatex fesiII.tex
	@rm -f *pyg *rip *aux *log *out
