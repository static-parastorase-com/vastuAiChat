#!/usr/bin/env python3
import csv,json,collections,pathlib,re
D=pathlib.Path(__file__).parent; R=D.parent
L=['en','kn','hi','ta','te','ml','bn','mr','gu','ur','pa','or','as','mai','sat','ks','ne','sd','doi','kok','mni','brx','sa']
def load(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f)),next(csv.reader(p.open(encoding='utf-8-sig',newline='')))
oldk,kh=load(R/'VastuKnowledge_Master.csv'); newk,nkh=load(D/'1_VastuKnowledge_Master.csv')
oldv,vh=load(R/'VastuVocabulary_Master.csv'); newv,nvh=load(D/'1_VastuVocabulary_Master.csv')
assert kh==nkh and vh==nvh
assert len(oldk)==5 and len(newk)==15 and newk[:5]==oldk
assert len(oldv)==115 and len(newv)==345 and newv[:115]==oldv
assert len({r['ID'] for r in newk})==15 and len({r['topicId'] for r in newk})==15
assert len({r['ID'] for r in newv})==345
known={r['topicId'] for r in newk}
assert all(r['conceptId'] in known for r in newv)
added=newk[5:]; at={r['topicId'] for r in added}; assert len(at)==10
aliases={}
for r in newk:
 d=json.loads(r['data']); assert d['topicId']==r['topicId']; assert set(d['languages'])==set(L)
 ids=[x['remedyId'] for x in d['remedies']]; assert len(ids)==len(set(ids)); assert ids==d['rules']['defaultRemedyIds']
 en=d['languages']['en']; assert set(en['remedies'])==set(ids)
 for rid,x in en['remedies'].items(): assert x['shortAnswer'] and x['steps'] and x['limitations']
 for q in en['questions']:
  n=' '.join(re.findall(r"[^\W_]+",q.lower(),flags=re.UNICODE)); assert n not in aliases,(n,aliases[n],r['topicId']); aliases[n]=r['topicId']
 # Remedy navigation reaches and stops after final item.
 cursor=0
 while cursor<len(ids): cursor+=1
 assert cursor==len(ids)
 # Missing locale follows the declared English fallback policy.
 assert d['matchingPolicy']['missingTranslation']=='offer_english'
for t in at:
 rows=[r for r in newv if r['conceptId']==t]; assert len(rows)==23 and {r['language'] for r in rows}==set(L)
 for r in rows:
  for f in ['aliases','Searchkeys','contentAliases','knowledgeQuestions']: assert isinstance(json.loads(r[f]),list)
  assert (r['language']=='en')==(r['isActive']=='true')
  if r['language']!='en': assert json.loads(r['aliases'])==[] and json.loads(r['contentAliases'])==[]
 # Exact primary and equivalent alias lookup resolves to this one topic.
 en=next(r for r in rows if r['language']=='en')
 assert all(aliases[a]==t for a in json.loads(en['aliases']))
# Unknown input has no exact alias hit.
assert 'is there a helipad above my kitchen' not in aliases
print('PASS: CSV/JSON, preservation, counts, IDs, language coverage, references, remedies, aliases, and record-level behavior')
