all:

install:
	mkdir -p $(DESTDIR)/var/lib/environment/nemo/
	mkdir -p $(DESTDIR)/var/lib/environment/compositor/
	install -D -m 644 conf/*.conf $(DESTDIR)/var/lib/environment/nemo/
	install -D -m 644 conf/compositor/*.conf $(DESTDIR)/var/lib/environment/compositor/
	install -D -m 644 prjconf/x86-prjconf.xml $(DESTDIR)/usr/share/prjconf/x86-prjconf.xml
