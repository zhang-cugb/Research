
default:	article.pdf, Highlights.pdf, Manuscript_IJNMF.pdf

article.pdf:		article.tex
Highlights.pdf: 	Highlights.tex
Manuscript_IJNMF.pdf:	Manuscript_IJNMF.tex

%.pdf:	%.tex
	rm -f $*.pdf
	pdflatex $<
	pdflatex $<	
	if fgrep "Rerun to" $*.log; then $(MAKE) --assume-new $< $@;fi

.PHONY: clean clean-pdf

# We don't rm *.ps because that might clobber image files. Instead, put any
# ps files which should go in $(PSFILES)
clean:	*.pdf
	rm $(TARGETS)*.aux *.log *.bbl *.blg *.toc *.lof *ind *idx *ilg *nav *snm \
*.out *pdf *.pdftex *_tex.pdf *.pdftex_t *.pstex *.pstex_t *~\
$(addsuffix .png, $(XFIG_IMAGES)) 2>/dev/null||true

htclean_%:
	rm $*.4ct $*.4tc $*.css $*.idv $*.lg $*.tmp $*.xref *.html 2>/dev/null||true
clean-aux:
		rm $(TARGETS)*.aux *.log *.bbl *.blg *.toc *.lof *ind *idx *ilg *nav *snm \
*.out diagrams/*-eps-converted-to.pdf
clean-pdf: 
		rm *.pdf

