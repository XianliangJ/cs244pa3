import os
import sys

if len(sys.argv) != 3:
  print 'Usage: python graph_results.py <filename> <output_tsv>'

results = []

infile = open(sys.argv[1], 'r')
protocol = None
downlink = None
uplink = None
throughput = None
delay = None
avg_capacity = None
for line in infile:
  l = line.strip()
  if l in ['SPROUT', 'TCP VEGAS', 'TCP CUBIC']:
    if not protocol is None:
      results.append((protocol, downlink, uplink, throughput, delay, avg_capacity))
      protocol = None
      downlink = None
      uplink = None
      throughput = None
      delay = None
      avg_capacity = None
    protocol = l
  elif l.startswith('Down linkfile:'):
    downlink = l.split(':')[1]
  elif l.startswith('Up linkfile:'):
    uplink = l.split(':')[1]
  elif l.startswith('Average throughput:'):
    throughput = l.split(':')[1].split(' ')[0]
  elif l.startswith('95th percentile signal delay:'):
    delay = l.split(':')[1].split(' ')[0]
  elif l.startswith('Average capacity:'):
    avg_capacity = l.split(':')[1].split(' ')[0]

# now write it out nicely formatted
outfile = open(sys.argv[2], 'w')
outfile.write('protocol\tdownlink\tuplink\tthroughput\tdelay\tavg_capacity\n')
for result in results:
  outfile.write('\t'.join(result))
outfile.close()

# now make pretty graphs
