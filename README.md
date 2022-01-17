# Is a single Embedding Enough? Learning Node Representations that Capture Multiple Social Contexts
This project is based on two papers, one directly and another one indirectly:
1. Main Paper: [Is a Single Embedding Enough? Learning Node Representations that Capture Multiple Social Contexts](https://arxiv.org/abs/1905.02138)
2. Extension: [Ego-splitting Framework: from Non-Overlapping to Overlapping Clusters](https://www.kdd.org/kdd2017/papers/view/ego-splitting-framework-from-non-overlapping-to-overlapping-clusters)

# Resources and Codes of the Mentioned Papers
1. SPLITTER: https://github.com/benedekrozemberczki/Splitter
2. Persona Graph: https://github.com/google-research/google-research/tree/master/graph_embedding/persona

# Datasets Used
1. Epinions social network: [soc-epinions](https://snap.stanford.edu/data/soc-Epinions1.html)
2. Wikipedia vote network: [wiki-vote](https://snap.stanford.edu/data/wiki-Vote.html)
3. High Energy Physics - Theory collaboration network: [ca-HepTh](https://snap.stanford.edu/data/ca-HepTh.html)
4. ca-AstroPh: [Astro Physics collaboration network](https://snap.stanford.edu/data/ca-AstroPh.html)
5. Human Protein-Protein interaction network: [PPI](https://snap.stanford.edu/biodata/datasets/10000/10000-PP-Pathways.html)

# Baselines
## Non-embedding Baselines
1. Jaccard Coefficient (J.C.)
2. Common Neighbours (C.N.)
3. Adamic Adar (A.A.)

## Embedding Baselines
1. [Laplacian EigenMaps](https://github.com/JAVI897/Laplacian-Eigenmaps)
2. [Node2Vec](https://github.com/aditya-grover/node2vec)
3. [DNGR](https://github.com/apoorvavinod/DNGR)
4. [Asymmetric](https://github.com/google/asymproj_edge_dnn)
5. [M-NMF](https://github.com/benedekrozemberczki/M-NMF)

# Claims 
## Abstract
1. reducing the error in link prediction by up to 90%.
2. effective visual analysis of the learned community structures.

## Introduction
1. ego-net based techniques can lead to improvements in embedding methods as well. (P. 5)
2. a natural embedding method based on the persona graph outperforms many embedding baselines in the task of link prediction. (P. 5)

## Task: Link Prediction
Link prediction (network reconstruction) is the best way to analyze an unsupervised network embedding's performance; as it is a primary task (unlike node classification - a secondary task that involves a labeling process that may be uncorrelated with the graph itself).

## Experimental Results
### Non-embedding Methods
1. Simply applying the persona preprocessing to the non-embedding baselines does not consistently improve the results over using them in the original graph.
   1. improvements were only observed in two of five datasets.
   2. sometimes even strong losses happened in applying this simple preprocessing, especially for sparse graphs such as ca-HepTh.
   3. This confirms that the gains observed in SPLITTER do not come merely from the preprocessing.

### Embedding Methods
1. at the same level of dimensionality, SPLITTER always outperforms all other baselines.
   1. the improvement is particularly significant in the largest graph epinions where SPLITTER using size 8 embeddings improves AUC-ROC by a factor of 40% (90% reduction in error) even when compared with the best baseline with 128 dimensions.
2. achieving close to optimal performance in two of the other largest graphs, wiki-vote and ca-AstoPh.
3. AUC-ROC of SPLITTER is higher than every other baseline using about 16pbar (average number of personas per node) dimensions for all datasets, except one which is M-NMF on ca-HepTh dataset.

### Task: Visualization
1. the persona graph community structure is clearer than the one in the original graph.
2. more separated embeddings (in 2D) in contrast to M-NMF.