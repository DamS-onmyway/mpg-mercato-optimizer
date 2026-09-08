import json, urllib.request
from datetime import datetime, timezone

URL = 'https://www.foot-direct.com/france/ligue-1/blessures-et-suspensions'
OUT = 'data/blessures-public.json'
req = urllib.request.Request(URL, headers={'User-Agent':'Mozilla/5.0 (compatible; MPG-Mercato-Optimizer/1.0)'})
with urllib.request.urlopen(req, timeout=30) as r:
    html = r.read().decode('utf-8', errors='replace')

payload = {
    'source': URL,
    'updatedAt': datetime.now(timezone.utc).isoformat(),
    'html': html
}
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False)
print(f'Wrote {OUT}: {len(html)} bytes')
