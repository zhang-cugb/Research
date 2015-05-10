default: article.tex
	pdflatex -shell-escape article
	bibtex article
	pdflatex -shell-escape article
	pdflatex -shell-escape article
	pdflatex -shell-escape article

clean:
	rm -rf *.aux *.log *.blg *.bbl *.spl *.log *.out diagrams/*-eps-converted-to.pdf article.pdf *lof *toc
