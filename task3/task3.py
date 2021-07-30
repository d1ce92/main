import sys
import re

values = open(sys.argv[2], 'r').read()
tests = open(sys.argv[1], 'r').read()

ids = re.findall(r'[0-9]+', values)
val = re.findall(r'.passed.|.failed.',values)

samples = []
for p,v in zip(ids,val):
    samples.append(re.findall(f'(id.: {p}.\n +.title.: .+.\n +.value.: )', tests))
    
edit_samples = [sample[0]+vl for sample,vl in zip(samples,val)]

for i,j in zip(ids,edit_samples):
    tests = re.sub(f'(id.: {i}.\n +.title.: .+.\n +.value.: ..)', j, tests)
out = open('report.json','w')
out.write(tests)


