PYTHON = python

SCRIPT = do_not_use_this_in_apple_store.py

all: install
	make run IMG=./img/handsome.png

run: $(SCRIPT)
	$(PYTHON) $(SCRIPT) $(IMG)

install:
	pip install pillow numpy

help:
	@echo "사용법:"
	@echo "    make run IMG=path/to/image"
	@echo "    make install  # pillow 및 numpy 설치"

clean:
	rm -f *.pyc
