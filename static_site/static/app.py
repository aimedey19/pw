#!/usr/bin/env python

from coltrane import initialize, run

wsgi = initialize(ROOT_URLCONF="pw.urls", INSTALLED_APPS=["pw"])

if __name__ == "__main__":
    run()
