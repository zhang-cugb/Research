default: 	Manuscript_ViscousInstabilities_KC.tex
		pdflatex -shell-escape Manuscript_ViscousInstabilities_KC
		bibtex Manuscript_ViscousInstabilities_KC
		pdflatex -shell-escape Manuscript_ViscousInstabilities_KC
		pdflatex -shell-escape Manuscript_ViscousInstabilities_KC
		pdflatex -shell-escape Manuscript_ViscousInstabilities_KC

template: article.tex
	pdflatex -shell-escape article
	bibtex article
	pdflatex -shell-escape article
	pdflatex -shell-escape article
	pdflatex -shell-escape article

clean:
	rm -rf *.aux *.log *.blg *.bbl *.spl *.log *.out *-eps-converted-to.pdf article.pdf \
	Manuscript_ViscousInstabilities_KC.pdf *lof *toc
