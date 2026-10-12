import base64,hashlib,json,os,pathlib,re,subprocess,sys,tempfile
root=pathlib.Path(sys.argv[1]);manifest=json.loads((root/'manifest.json').read_text())
assert re.fullmatch(r'0\.\d+\.\d+-beta\.\d+',manifest['version'])
assert manifest['tag']=='windows-v'+manifest['version'] and isinstance(manifest['build'],int) and manifest['build']>0
assert re.fullmatch(r'[a-f0-9]{40}',manifest['source'])
assert set(manifest['assets'])=={'Poche-Windows-x64.exe','LISEZ-MOI-Windows.txt','Poche-Windows-apercu.png'}
with tempfile.TemporaryDirectory() as d:
 p=pathlib.Path(d);(p/'public.der').write_bytes(bytes.fromhex('302a300506032b6570032100')+base64.b64decode('Ehk536ED2OKI5bvDKUWlgKXjgOw8LCCK3K5qR/rQM0c='))
 for name,metadata in manifest['assets'].items():
  data=(root/name).read_bytes();assert len(data)==metadata['length'] and 0<len(data)<100_000_000
  assert hashlib.sha256(data).hexdigest()==metadata['sha256']
  signature=base64.b64decode(metadata['signature'],validate=True);assert len(signature)==64;(p/'sig').write_bytes(signature)
  subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(p/'public.der'),'-keyform','DER','-rawin','-in',str(root/name),'-sigfile',str(p/'sig')],check=True,stdout=subprocess.DEVNULL)
  if name.endswith('.exe'):assert data[:2]==b'MZ'
assert (root/'Poche-Windows-x64.exe.sha256').read_text()==manifest['assets']['Poche-Windows-x64.exe']['sha256']+'  Poche-Windows-x64.exe\n'
if 'GITHUB_OUTPUT' in os.environ:
 with open(os.environ['GITHUB_OUTPUT'],'a') as f:f.write('tag='+manifest['tag']+'\nversion='+manifest['version']+'\n')
print('Fichiers Windows et signatures Ed25519 vérifiés.')
