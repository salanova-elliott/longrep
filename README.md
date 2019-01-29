# Rosalind
## LREP: Finding the Longest Multiple Repeat

A repeated substring of a string *s* of length *n* is simply a substring that appears in more than one location of *s*; more specifically, a k-fold substring appears in at least k distinct locations.

The suffix tree of *s*, denoted *T(s)*, is defined as follows:

  * *T(s)* is a rooted tree having exactly *n* leaves.
  * Every edge of *T(s)* is labeled with a substring of *s~*, where *s~* is the string formed by adding a placeholder symbol $ to the end of *s*.
  * Every internal node of *T(s)* other than the root has at least two children; i.e., it has degree at least 3.
  * The substring labels for the edges leading from a node to its children must begin with different symbols.
  * By concatenating the substrings along edges, each path from the root to a leaf corresponds to a unique suffix of *s~*.

**Given:** A DNA string *s* (of length at most 20 kbp) with $ appended, a positive integer *k*, and a list of edges defining the suffix tree of *s*. Each edge is represented by four components:

1. the label of its parent node in *T(s)*
2. the label of its child node in *T(s)*
3. the location of the substring *t* of *s~* assigned to the edge
4. the length of *t*.

**Return:** The longest substring of *s* that occurs at least *k* times in *s*. (If multiple solutions exist, you may return any single solution.)

## Example use
```python longrep.py test_lrep.py```
