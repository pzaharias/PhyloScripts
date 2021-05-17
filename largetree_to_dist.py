#! /usr/bin/env python3
'''
Paul Zaharias 2021
Create ultra-large distance matrix from patristic distances by printing one line at a time (thus avoid storing all distances in memory).
'''

import treeswift
import argparse

def main(args):
    
    #include branch lengths or not
    if args.Branch_lengths:
        tree = treeswift.read_tree_newick(args.Input_tree)
    else :
        tree = treeswift.read_tree_newick(args.Input_tree)
        for node in tree.traverse_postorder():
            node.set_edge_length(1)

    #create list of leaves
    leaves = []
    for node in tree.traverse_preorder():
        if node.is_leaf() == True:
            leaves.append(node)
    #open file for reading and appending
    with open(args.Output_matrix, 'a+') as f:
        #write number of leaves (required for phylip format)
        f.write(str(len(leaves)) + '\n')
        for i in range(len(leaves)):
            #write name of the leave i at the beginning of each line
            f.write(str(leaves[i]) + ' ')
            for j in range(len(leaves)):
                dist = tree.distance_between(leaves[i], leaves[j])
                distance = str(dist)
                #write distances to i from all leaves j on the same line
                f.write(distance + ' ')
            #go the the next line 
            f.write('\n')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--Input_tree", type=str,
                        help="Input tree in newick format", required=True)
    parser.add_argument('-o', "--Output_matrix", type=str, 
                        help="name for the distance matrix output file", required=True)
    parser.add_argument('-b', '--Branch_lengths', action='store_true',
                        help="If specified then distances are weighted according to branch length")
    main(parser.parse_args())
