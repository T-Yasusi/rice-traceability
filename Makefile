SOURCES = intro.md info_structure.md operation.md
OUTPUT  = index.md

$(OUTPUT) : $(SOURCES)
	cat $(SOURCES) > $(OUTPUT)
