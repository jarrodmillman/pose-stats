BUILDDIR := build
FILES := description summary
TEX := $(addprefix $(BUILDDIR)/,$(FILES:=.tex))

.PHONY: default clean $(FILES) grant
default: grant

$(BUILDDIR):
	mkdir -p $@

$(BUILDDIR)/%.tex: %.md
	pandoc --strip-comments -o $@ $<

grant: $(BUILDDIR) $(TEX)
	cp grant.{tex,bib} $(BUILDDIR)
	(cd $(BUILDDIR) && latexmk -pdf grant.tex)
	cp $(BUILDDIR)/grant.pdf .

clean: $(BUILDDIR)
	rm -rf $(BUILDDIR)
