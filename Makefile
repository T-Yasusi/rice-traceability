SOURCES = intro.md info_structure.md table_structure.md operation.md summary.md
OUTPUT  = index.md

$(OUTPUT) : $(SOURCES)
	(for f in $(SOURCES); do cat $$f; done) > $(OUTPUT)

