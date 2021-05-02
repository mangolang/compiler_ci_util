#!/usr/bin/env python3

from sys import stderr, exit, argv

try:
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError as ex:
    print(ex)
    stderr.write('\nfailed to import urllib, maybe not using python3?\n')
    exit(1)

if len(argv) < 2:
    stderr.write('\nargument should be the path to a Cargo.lock file\n\n')
    exit(1)

path = argv[1]
try:
    with open(path, 'r') as fh:
        data = fh.read()
except HTTPError as ex:
    print(ex)
    stderr.write('\nfailed to download file, maybe it has moved, or there is a connection problem\n\n'.format(url))
    exit(1)

started = False
deps = {}
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
        deps[name] = version
        name = None

print('\n'.join('{} = "{}"'.format(name, version) for (name, version) in sorted(deps.items())))

