from flask import Flask, render_template
import json
import networkx as nx

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def graph_to_json():

    json_file = {}

    neighborhood_file = open('/Users/julioadl/Desktop/Neighborhoods/net.txt', 'r')
    neighborhood_dict = eval(neighborhood_file.read())

    Graph = nx.from_dict_of_lists(neighborhood_dict)

    nodes = Graph.nodes()
    list_of_nodes = []

    id_of_nodes = {}
    i = 0
    for node in nodes:
        id_of_nodes[node] = i
        i += 1

    for node in nodes:
        node_info = {}
        node_info['name'] = str(node)
        list_of_nodes.append(node_info)

    edges = Graph.edges()
    list_of_edges = []
    for node in nodes:
        neighbors = Graph.neighbors(node)
        for neighbor in neighbors:
            edge_info = {}
            edge_info['source'] = id_of_nodes[node]
            edge_info['target'] = id_of_nodes[neighbor]
            edge_info['value'] = 1
            list_of_edges.append(edge_info)

    json_file['nodes'] = list_of_nodes
    json_file['links'] = list_of_edges

    json_file = json.dumps(json_file)

    return json_file

if __name__ == '__main__':
    app.run(debug = True)
