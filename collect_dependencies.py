#!/usr/bin/env python3

from sys import stderr, exit
try:
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError as ex:
    print(ex)
    stderr.write('\nfailed to import urllib, maybe not using python3?\n')
    exit(1)

url = 'https://raw.githubusercontent.com/mangolang/compiler/master/Cargo.lock'
try:
    data = urlopen(url).read().decode('utf-8')
except HTTPError as ex:
    print(ex)
    stderr.write('\nfailed to download file, maybe it has moved, or there is a connection problem\n\n'.format(url))
    exit(1)

started = False
deps = []
name = None
for line in data.splitlines():
    if line.startswith('[['):
        assert name is None
        started = True
    if not started:
        continue
    if line.startswith('name = '):
        name = line[8:-1]
    if line.startswith('version = '):
        version = line[11:-1]
        assert name is not None
        deps.append((name, version))
        name = None

print('\n'.join('{} = "{}"'.format(*dep) for dep in deps))

