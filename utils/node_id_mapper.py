import pandas as pd
import networkx as nx
from pathlib import Path


def text_to_zeroed_csv(path):
    dataset_name = str(path.split('/')[-1]).replace('.txt','')
    
    df = pd.read_csv(path, skiprows=3, delimiter='\t')
    df = df.rename(columns={'# FromNodeId':'Source','ToNodeId':'Target'})
    
    G = nx.from_pandas_edgelist(df,'Source','Target')
    nodes = G.number_of_nodes()
    edges = G.number_of_edges()
    
    from_list = list(df['Source'].unique())
    to_list = list(df['Target'].unique())
    node_ids = list(set(list(from_list + to_list)))

    node_ids.sort()
    
    d = {}
    for value, index in enumerate(node_ids):
        d[index] = value
        
    df_id = pd.DataFrame.from_dict(d.items(), orient='columns')
    df_id.columns=['main_node_id','mapped_node_id']

    df['Source'] = df['Source'].map(d)
    df['Target'] = df['Target'].map(d)

    df.to_csv('datasets/normalized_id/{}(corrected_index).csv'.format(dataset_name), index=False)
    df_id.to_csv('mapping_data/{}(mapped_id).csv'.format(dataset_name))
    
    return(f'Number of nodes in the graph: {nodes}', f'Number of edges in the graph: {edges}')


if __name__=='__main__':
    files = Path('datasets/main').glob('*.txt')
    for file in files:
        text_to_zeroed_csv(str(file))