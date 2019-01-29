#Finds longest repeat that occurs k times in a seq
from __future__ import print_function
from trienode import TrieNode as tn 
import sys

node_nums = {'node1': tn("", None)}
edge_info = []

#Parses input 
with open(sys.argv[1]) as f:

	seq = f.readline().rstrip()
	k = int(f.readline())

	for line in f:
		edge_info.append(line.split())

#Constructs trie
for edge in edge_info:

	if not edge[1] in node_nums:
		node_nums[edge[1]] = tn(seq[int(edge[2]) - 1: int(edge[2]) + int(edge[3]) - 1], node_nums[edge[0]])

	node_nums[edge[0]].addChild(node_nums[edge[1]])


#Ascends trie through terminal nodes to count leaves for internal nodes
for node in node_nums.values():

	if len(node.children) == 0:
		node_trace = node

		while node_trace.parent:
			node_trace.parent.leaves += 1
			node_trace = node_trace.parent

#Looks for longest substring
lsub = ""
for node in node_nums.values():

 	if node.leaves >= k:
 		tsub = node.seq
 		node_trace = node

 		while node_trace.parent:
  			tsub = node_trace.parent.seq + tsub
 			node_trace = node_trace.parent

 		if len(tsub) > len(lsub):
 			lsub = tsub

print(lsub)

