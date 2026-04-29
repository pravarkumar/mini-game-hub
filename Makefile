LATEX = mini-game-hub-report.tex
PDF = mini-game-hub-report.pdf

all: $(PDF)
$(PDF): $(LATEX)
	pdflatex $<	
	pdflatex $<

.PHONY clean:
	rm -f *.aux *.log *.pdf