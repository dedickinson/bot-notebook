#!/usr/bin/env python

# This is a small test to help wrangle TLS/SSL issues, especially 
# when using APIs from Azure, AWS etc. 
# 
# If you run `./cert_check.py https://www.google.com` 
#   and get a `urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]`
#   and are on OSX you need to `sudo port install curl-ca-bundle`
#
# See also:
#   - https://docs.python.org/3/library/urllib.request.html 
#   - https://access.redhat.com/articles/2039753

import urllib.request as urllib2
import sys

req = urllib2.Request(sys.argv[1], headers={'User-Agent':'Mozilla/5.0'})
urllib2.urlopen(req)