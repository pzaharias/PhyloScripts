'''
Created on Sep 13, 2021
original author: Paul Zaharias

This script takes an rooted tree as an input and will print the smallest list of tips between the two root child nodes. If the two child nodes have the same number of tips, then it prints the first list. 
'''

import dendropy
import sys
import argparse

def main(args):
    
    rootedTree = dendropy.Tree.get(path=args.Rooted_tree, schema="newick", preserve_underscores=True)

    root = rootedTree.seed_node

    child_node = []
    for child in root.child_nodes():
        child_node.append(child)

    outgroups = []
    if len(child_node[0].leaf_nodes()) == len(child_node[1].leaf_nodes()):
        outgroups = [n.taxon.label for n in child_node[0].leaf_nodes()]
    elif len(child_node[0].leaf_nodes()) > len(child_node[1].leaf_nodes()):
        outgroups = [n.taxon.label for n in child_node[1].leaf_nodes()]
    elif len(child_node[0].leaf_nodes()) < len(child_node[1].leaf_nodes()):
        outgroups = [n.taxon.label for n in child_node[0].leaf_nodes()]

    for outgroup in outgroups:
        print(outgroup)

if __name__ == "__main__":
    sys.setrecursionlimit(10000) # allow for deepcopying really large trees

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--Rooted_tree", type=str,
                        help="Input rooted tree", required=True)

    main(parser.parse_args())