class TrieNode:

	def __init__(self, seq, par):
		self.seq = seq
		self.parent = par

		self.leaves = 0
		self.children = []

	def addChild(self, child):
		self.children.append(child)

	def __repr__(self):
		if self.parent:
			return "Parent: {} children: {} leaves {} {}".format(self.parent.seq, len(self.children), self.leaves, self.seq)
		else:
			return "ROOT children: {} {}".format(len(self.children), self.seq)