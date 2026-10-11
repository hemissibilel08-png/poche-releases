#!/usr/bin/env python3
"""Verify the public binary and Sparkle feed using the pinned public key."""
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import plistlib
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

PUBLIC_KEY = 'Ehk536ED2OKI5bvDKUWlgKXjgOw8LCCK3K5qR/rQM0c='
root = Path(sys.argv[1] if len(sys.argv) > 1 else 'incoming')
manifest = json.loads((root / 'manifest.json').read_text())
version, build = manifest['version'], manifest['build']
assert re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version)
assert isinstance(build, int) and build > 0
archive = root / 'Poche.zip'
data = archive.read_bytes()
assert len(data) == manifest['length']
assert hashlib.sha256(data).hexdigest() == manifest['sha256']
assert (root / 'Poche.zip.sha256').read_text() == f'{manifest["sha256"]}  Poche.zip\n'

def verify(data, signature):
    signature = base64.b64decode(signature, validate=True)
    assert len(signature) == 64
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        (temp / 'public.der').write_bytes(bytes.fromhex('302a300506032b6570032100') + base64.b64decode(PUBLIC_KEY))
        (temp / 'data').write_bytes(data)
        (temp / 'signature').write_bytes(signature)
        subprocess.run([os.environ.get('OPENSSL', 'openssl'), 'pkeyutl', '-verify', '-pubin', '-inkey', str(temp / 'public.der'), '-keyform', 'DER', '-rawin', '-in', str(temp / 'data'), '-sigfile', str(temp / 'signature')], check=True, stdout=subprocess.DEVNULL)

verify(data, manifest['signature'])
feed = (root / 'appcast.xml').read_bytes()
match = re.search(rb'<!-- sparkle-signatures:\nedSignature: ([A-Za-z0-9+/=]+)\nlength: ([0-9]+)\n-->\s*$', feed)
assert match and int(match[2]) == match.start()
verify(feed[:int(match[2])], match[1])
ns = {'s': 'http://www.andymatuschak.org/xml-namespaces/sparkle'}
item = ET.fromstring(feed).find('channel/item')
assert item.findtext('s:version', namespaces=ns) == str(build)
assert item.findtext('s:shortVersionString', namespaces=ns) == version
enclosure = item.find('enclosure')
assert enclosure.attrib['url'] == f'https://github.com/hemissibilel08-png/poche-releases/releases/download/v{version}/Poche.zip'
assert enclosure.attrib['{'+ns['s']+'}edSignature'] == manifest['signature']
assert int(enclosure.attrib['length']) == len(data)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert all(n.startswith('Poche.app/') and '..' not in PurePosixPath(n).parts for n in z.namelist())
    info = plistlib.loads(z.read('Poche.app/Contents/Info.plist'))
    assert info['CFBundleIdentifier'] == 'local.bilel.poche'
    assert info['CFBundleVersion'] == str(build)
    assert info['CFBundleShortVersionString'] == version
    assert info['SUPublicEDKey'] == PUBLIC_KEY
    assert info['SURequireSignedFeed'] and info['SUVerifyUpdateBeforeExtraction']
    assert info['SUFeedURL'] == 'https://raw.githubusercontent.com/hemissibilel08-png/poche-releases/updates/appcast.xml'
print(f'Poche {version} : archive, contenu, empreinte et deux signatures Ed25519 vérifiés.')
if 'GITHUB_OUTPUT' in os.environ:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'version={version}\ntag=v{version}\nbuild={build}\n')
