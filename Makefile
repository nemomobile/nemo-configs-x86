all:

install:
	mkdir -p $(DESTDIR)/var/lib/environment/nemo/
	install -D -m 644 *.conf $(DESTDIR)/var/lib/environment/nemo/

