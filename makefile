SRC_DIR=./
DST_DIR=internal/mocks

# Detecta se está no Windows
ifeq ($(OS),Windows_NT)
	SHELL := powershell.exe
	.SHELLFLAGS := -NoProfile -ExecutionPolicy Bypass -Command
	GENERATE_MOCKS = ./generate-mocks.ps1
else
	INTERFACE_FILES := $(shell find $(SRC_DIR) -path ./vendor -prune -o -type f -name "*.go" -print | xargs grep -l "type . interface" || true)

	GENERATE_MOCKS = \
		@echo ">> Gerando mocks recursivamente..."; \
		rm -rf $(DST_DIR); \
		mkdir -p $(DST_DIR); \
		for file in $(INTERFACE_FILES); do \
			name=$$(basename $$file .go); \
			dir=$$(dirname $$file | sed 's|.*/||'); \
			dest_file=$(DST_DIR)/mock_$${dir}_$${name}.go; \
			echo ">> Gerando mock: $$file -> $$dest_file"; \
			mockgen -source=$$file -destination=$$dest_file -package=mocks; \
		done
endif

mocks:
	$(GENERATE_MOCKS)