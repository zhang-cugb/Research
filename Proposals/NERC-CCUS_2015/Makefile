#! /bin/bash


default: Outline_ReactiveCCS.pdf 

Outline_ReactiveCCS.pdf: Outline_ReactiveCCS.tex

%.pdf:	%.tex
	rm -f $*.pdf
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<
	if fgrep "Rerun to" $*.log; then $(MAKE) --assume-new $< $@;fi

clean:
	rm -rf *.aux *.log *.blg *.bbl *.spl *.log *.out *-eps-converted-to.pdf *.pdf *lof *toc \
	*.pdf
