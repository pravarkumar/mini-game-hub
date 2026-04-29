LATEX = report.tex
PDF = report.pdf

all: $(PDF)
$(PDF): $(LATEX)
	pdflatex $<	
	pdflatex $<

.PHONY clean:
	rm -f *.aux *.log *.pdf