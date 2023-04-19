class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {

    }

    addEdge(edge) {

    }

    removeEdge(edge) {

    }

    removeVertex(vertex) {

    }
}

let graph = new Graph();
graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");
graph.addVertex("F");

graph.addEdge("A", "B");
graph.addEdge("A", "C");
graph.addEdge("B", "D");
graph.addEdge("C", "E");
graph.addEdge("D", "E");
graph.addEdge("D", "F");
graph.addEdge("E", "F");

/*
    Implement (Iterative and Recursive) "Depth First Search"
    Starts with "A"
    visitedFlow = [ A, B, D, E, C, F ]

    Implement (Iterative and Recursive) "Breadth First Search"
    Starts with "A"
    visitedFlow = [ A, B, C, D, E, F ]

       A
     /  \
    B    C
    |    |
    D----E
     \  /
      F

*/