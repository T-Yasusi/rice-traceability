SOURCES = intro.md info_structure.md operation.md
OUTPUT  = index.md

$(OUTPUT) : $(SOURCES)
	(for f in $(SOURCES); do \
		  cat $$f; \
		  printf "\n\n\n"; \
	done) > $(OUTPUT)

