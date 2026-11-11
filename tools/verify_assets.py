from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[1]
spec=json.loads((root/'asset-payloads.json').read_bytes())
for name,row in spec['files'].items():
    path=root/'dist'/name
    assert path.resolve().is_relative_to((root/'dist').resolve()) and path.is_file() and not path.is_symlink()
    raw=path.read_bytes()
    assert len(raw)==row['bytes'] and sha256(raw).hexdigest()==row['sha256'],name
files=[p for p in (root/'dist').rglob('*') if p.is_file()]
assert sum(p.stat().st_size for p in files)<spec['maxSiteBytes']
assert {p.relative_to(root/'dist').as_posix() for p in files}==set(spec['files'])|{'.nojekyll','asset-manifest.json'}
print('Verified',len(spec['files']),'immutable payloads,',sum(p.stat().st_size for p in files),'site bytes')
