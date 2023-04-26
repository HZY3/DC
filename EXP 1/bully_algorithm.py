import time
import random

class Node:
    def __init__(self, id, coordinator=None):
        self.id = id
        self.coordinator = coordinator
        self.nodes = [1, 2, 3, 4, 5]  # list of all node ids in the system
    
    def start_election(self):
        # Election message is sent to all nodes with higher ids
        higher_nodes = [node_id for node_id in self.nodes if node_id > self.id]
        for node_id in higher_nodes:
            print(f"Node {self.id} sending ELECTION message to node {node_id}")
        
        # Wait for responses from higher nodes
        time.sleep(2)  # wait for 2 seconds
        responses = [random.choice([True, False]) for _ in range(len(higher_nodes))]
        
        if all(responses):  # if all higher nodes respond positively
            self.become_coordinator()
        else:
            self.propagate_election()
    
    def propagate_election(self):
        # Election message is forwarded to all nodes with higher ids
        higher_nodes = [node_id for node_id in self.nodes if node_id > self.id]
        for node_id in higher_nodes:
            print(f"Node {self.id} forwarding ELECTION message to node {node_id}")
            node = nodes[node_id - 1]
            node.handle_election(self.id)
    
    def handle_election(self, election_id):
        if self.id > election_id:
            # Respond with OK message if this node has higher id than the election initiator
            print(f"Node {self.id} responding with OK message to node {election_id}")
            nodes[election_id - 1].handle_ok()
        else:
            # Forward the election message to higher nodes
            self.propagate_election()
    
    def handle_ok(self):
        # If this node receives an OK message, it is not the coordinator. Election is over.
        print(f"Node {self.id} received OK message. Election over.")
    
    def become_coordinator(self):
        # This node becomes the new coordinator and broadcasts COORDINATOR message to all other nodes.
        self.coordinator = self.id
        print(f"Node {self.id} becomes the new coordinator.")
        for node in nodes:
            if node.id != self.id:
                node.handle_coord(self.id)
    
    def handle_coord(self, coord_id):
        # This node receives a COORDINATOR message from a higher node. It updates its coordinator and election is over.
        self.coordinator = coord_id
        print(f"Node {self.id} received COORDINATOR message from node {coord_id}. Election over.")
    
# Create 5 nodes with ids 1-5
nodes = [Node(i) for i in range(1, 6)]

# Select node 3 as initial coordinator
nodes[2].become_coordinator()

# Simulate failure of coordinator (node 3)
nodes[2].coordinator = None

# Node 1 starts an election
nodes[0].start_election()
