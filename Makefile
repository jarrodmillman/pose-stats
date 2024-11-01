BUILDDIR := build
FILES := data-management description facilities summary
TEX := $(addprefix $(BUILDDIR)/,$(FILES:=.tex))
SVGS := $(wildcard figures/*.svg)
FIGURES := $(addprefix $(BUILDDIR)/,$(SVGS:.svg=.pdf))
DROPBOX := ~/Dropbox/docs/bids/2023-NSF-POSE/proposal

.PHONY: default clean $(FILES) grant
default: grant

$(BUILDDIR):
	mkdir -p $@/figures

$(BUILDDIR)/%.tex: %.md
	pandoc --strip-comments -o $@ $<

$(BUILDDIR)/figures/%.pdf: figures/%.svg
	inkscape --export-filename=$@ $<

grant: $(BUILDDIR) $(TEX) $(FIGURES)
	cp grant.{tex,bib} $(BUILDDIR)
	(cd $(BUILDDIR) && latexmk -pdf grant.tex)
	cp $(BUILDDIR)/grant.pdf .

clean: $(BUILDDIR)
	rm -rf $(BUILDDIR)

submit: grant
	python split_pdf.py build/grant.pdf
	rm $(DROPBOX)/*.pdf
	cp build/[0,1]*.pdf $(DROPBOX)
