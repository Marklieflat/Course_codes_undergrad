/*
 * File: graph.h
 * -------------
 * This file is the interface for a flexible graph package that exports
 * a parameterized Graph class.
 */

#ifndef _graph_h
#define _graph_h

#include <string>
#include "map.h"
#include "set.h"

/*
 * Class: Graph<NodeType,ArcType>
 * ------------------------------
 * This class represents a graph with the specified node and arc types.
 * The NodeType and ArcType parameters indicate the record or object types
 * used for nodes and arcs, respectively.  These types can contain any
 * fields or methods required by the client, but must contain the following
 * fields required by the Graph package itself:
 *
 * The NodeType definition must include:
 *   - A string field called name
 *   - A Set<ArcType *> field called arcs
 *
 * The ArcType definition must include:
 *   - A NodeType * field called start
 *   - A NodeType * field called finish
 */

template <typename NodeType,typename ArcType>
class Graph {

public:

/*
 * Constructor: Graph
 * Usage: Graph<NodeType,ArcType> g;
 * ---------------------------------
 * Creates an empty Graph object.
 */

   Graph();

/*
 * Destructor: ~Graph
 * ------------------
 * Frees the internal storage allocated to represent the graph.
 */

   ~Graph();

/*
 * Method: size
 * Usage: int size = g.size();
 * ---------------------------
 * Returns the number of nodes in the graph.
 */

   int size() const;

/*
 * Method: isEmpty
 * Usage: if (g.isEmpty()) . . .
 * -----------------------------
 * Returns true if the graph is empty.
 */

   bool isEmpty() const;

/*
 * Method: clear
 * Usage: g.clear();
 * -----------------
 * Reinitializes the graph to be empty, freeing any heap storage.
 */

   void clear();

/*
 * Method: addNode
 * Usage: g.addNode(name);
 *        g.addNode(node);
 * -----------------------
 * Adds a node to the graph.  The first form creates the node from
 * the name.  The second form takes a node pointer created by the client.
 * Both forms return a pointer to the added node, although that value is
 * typically ignored.
 */

   NodeType *addNode(std::string name);
   NodeType *addNode(NodeType *node);

/*
 * Method: removeNode
 * Usage: g.removeNode(name);
 *        g.removeNode(node);
 * --------------------------
 * Removes a node from the graph, where the node can be specified
 * either by its name or as a pointer value.  Removing a node also
 * removes all arcs that contain that node.
 */

   void removeNode(std::string name);
   void removeNode(NodeType *node);

/*
 * Method: getNode
 * Usage: NodeType *node = g.getNode(name);
 * ----------------------------------------
 * Looks up a node in the name table attached to the graph and
 * returns a pointer to that node.  If no node with the specified
 * name exists, getNode returns NULL.
 */

   NodeType *getNode(std::string name) const;

/*
 * Method: addArc
 * Usage: g.addArc(s1, s2);
 *        g.addArc(n1, n2);
 *        g.addArc(arc);
 * ---------------------
 * Adds an arc to the graph.  The endpoints of the arc can be specified
 * either as strings indicating the names of the nodes or as pointers to
 * the node structures.  All versions return a pointer to the added arc,
 * although that value is typically ignored.
 */

   ArcType *addArc(std::string s1, std::string s2);
   ArcType *addArc(NodeType *n1, NodeType *n2);
   ArcType *addArc(ArcType *arc);

/*
 * Method: removeArc
 * Usage: g.removeArc(s1, s2);
 *        g.removeArc(n1, n2);
 *        g.removeArc(arc);
 * ------------------------
 * Removes an arc from the graph, where the arc can be specified in any
 * of three ways: by the names of its endpoints, by the node pointers
 * at its endpoints, or as an arc pointer.  If more than one arc
 * connects the specified endpoints, all of them are removed.
 */

   void removeArc(std::string s1, std::string s2);
   void removeArc(NodeType *n1, NodeType *n2);
   void removeArc(ArcType *arc);

/*
 * Method: isConnected
 * Usage: if (g.isConnected(s1, s2)) . . .
 *        if (g.isConnected(n1, n2)) . . .
 * ---------------------------------------
 * Returns true if the graph contains an arc between the specified nodes.
 * Nodes can be specified either by name or as pointers to node objects.
 */

   bool isConnected(std::string s1, std::string s2) const;
   bool isConnected(NodeType *n1, NodeType *n2) const;

/*
 * Method: getNodeSet
 * Usage: for (NodeType *node : g.getNodeSet()) . . .
 * --------------------------------------------------
 * Returns the set of all nodes in the graph.
 */

   Set<NodeType *> & getNodeSet();

/*
 * Method: getArcSet
 * Usage: for (ArcType *arc : g.getArcSet()) . . .
 *        for (ArcType *arc : g.getArcSet(node)) . . .
 *        for (ArcType *arc : g.getArcSet(name)) . . .
 * ---------------------------------------------------
 * Returns the set of all arcs in the graph or, in the second and
 * third forms, the arcs that start at the specified node, which
 * can be indicated either as a pointer or by name.
 */

   Set<ArcType *> & getArcSet();
   Set<ArcType *> & getArcSet(NodeType *node);
   Set<ArcType *> & getArcSet(std::string name);

/*
 * Method: getNeighbors
 * Usage: for (NodeType *node : g.getNeighbors(node)) . . .
 *        for (NodeType *node : g.getNeighbors(name)) . . .
 * --------------------------------------------------------
 * Returns the set of nodes that are neighbors of the specified
 * node, which can be indicated either as a pointer or by name.
 */

   Set<NodeType *> getNeighbors(NodeType *node);
   Set<NodeType *> getNeighbors(std::string node);

/*
 * Methods: copy constructor and assignment operator
 * -------------------------------------------------
 * These methods implement deep copying for graphs.
 */

   Graph(const Graph & src);
   const Graph & operator=(const Graph & src);

/* Private section */

/*
 * Notes on the representation
 * ---------------------------
 * The Graph class is built as a layered abstraction on top of the Set
 * and Map classes.  Most of the complexity appears in the underlying
 * implementations.
 */

private:

/* Instance variables */

   Set<NodeType *> nodes;                /* The set of nodes in the graph */
   Set<ArcType *> arcs;                  /* The set of arcs in the graph  */
   Map<std::string,NodeType *> nodeMap;  /* A map from names and nodes    */

/* Private methods */

   void deepCopy(const Graph & src);
   NodeType *getExistingNode(std::string name) const;

};

/*
 * Implementation notes: Graph constructor and destructor
 * ------------------------------------------------------
 * The only initialization required at this level is creating empty data
 * structures, which is performed automatically by the underlying classes.
 * The destructor, however, must free the individual arc and node
 * structures as well.  Calling clear is sufficient to accomplish this task.
 */

template <typename NodeType,typename ArcType>
Graph<NodeType,ArcType>::Graph() {
   /* Empty */
}

template <typename NodeType,typename ArcType>
Graph<NodeType,ArcType>::~Graph() {
   clear();
}

/*
 * Implementation notes: size, isEmpty
 * -----------------------------------
 * These methods are defined in terms of the node set, so the Graph
 * class simply forwards the requests to the Set class.
 */

template <typename NodeType,typename ArcType>
int Graph<NodeType,ArcType>::size() const {
   return nodes.size();
}

template <typename NodeType,typename ArcType>
bool Graph<NodeType,ArcType>::isEmpty() const {
   return nodes.isEmpty();
}

/*
 * Implementation notes: clear
 * ---------------------------
 * The implementation of clear frees all nodes and arcs.
 */

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::clear() {
   for (NodeType *node : nodes) {
      delete node;
   }
   for (ArcType *arc : arcs) {
      delete arc;
   }
   arcs.clear();
   nodes.clear();
   nodeMap.clear();
}

/*
 * Implementation notes: addNode
 * -----------------------------
 * The addNode method adds the node to the set of nodes for the graph and
 * to the map from names to nodes.
 */

template <typename NodeType,typename ArcType>
NodeType *Graph<NodeType,ArcType>::addNode(std::string name) {
   if (nodeMap.containsKey(name)) {
      error("addNode: Node " + name + " already exists");
   }
   NodeType *node = new NodeType();
   node->name = name;
   return addNode(node);
}

template <typename NodeType,typename ArcType>
NodeType *Graph<NodeType,ArcType>::addNode(NodeType *node) {
   nodes.add(node);
   nodeMap[node->name] = node;
   return node;
}

/*
 * Implementation notes: removeNode
 * --------------------------------
 * The removeNode method removes the specified node but must also
 * remove any arcs in the graph containing the node.  To avoid
 * changing the node set during iteration, this implementation
 * creates a vector of arcs that require deletion.
 */

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::removeNode(std::string name) {
   removeNode(getExistingNode(name));
}

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::removeNode(NodeType *node) {
   Vector<ArcType *> toRemove;
   for (ArcType *arc : arcs) {
      if (arc->start == node || arc->finish == node) {
         toRemove.add(arc);
      }
   }
   for (ArcType *arc : toRemove) {
      removeArc(arc);
   }
   nodes.remove(node);
}

/*
 * Implementation notes: getNode, getExistingNode
 * ----------------------------------------------
 * The getNode method simply looks up the name in the map, which correctly
 * returns NULL if the name is not found.  Other methods in the
 * implementation call the private method getExistingNode instead,
 * which checks for a NULL value and signals an error.
 */

template <typename NodeType,typename ArcType>
NodeType *Graph<NodeType,ArcType>::getNode(std::string name) const {
   return nodeMap.get(name);
}

template <typename NodeType,typename ArcType>
NodeType *Graph<NodeType,ArcType>::getExistingNode(std::string name) const {
   NodeType *node = nodeMap.get(name);
   if (node == NULL) error("No node named " + name);
   return node;
}

/*
 * Implementation notes: addArc
 * ----------------------------
 * The addArc method appears in three forms, as described in the interface.
 */

template <typename NodeType,typename ArcType>
ArcType *Graph<NodeType,ArcType>::addArc(std::string s1, std::string s2) {
   return addArc(getExistingNode(s1), getExistingNode(s2));
}

template <typename NodeType,typename ArcType>
ArcType *Graph<NodeType,ArcType>::addArc(NodeType *n1, NodeType *n2) {
   ArcType *arc = new ArcType();
   arc->start = n1;
   arc->finish = n2;
   return addArc(arc);
}

template <typename NodeType,typename ArcType>
ArcType *Graph<NodeType,ArcType>::addArc(ArcType *arc) {
   arc->start->arcs.add(arc);
   arcs.add(arc);
   return arc;
}

/*
 * Implementation notes: removeArc
 * -------------------------------
 * These methods remove arcs from the graph, which is ordinarily a simple
 * matter of removing the arc from two sets: the set of arcs in the graph
 * as a whole and the set of arcs in the starting node.  The methods that
 * remove an arc specified by its endpoints, however, must take account of
 * the possibility that there is more than one arc and remove all of them.
 */

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::removeArc(std::string s1, std::string s2) {
   removeArc(getExistingNode(s1), getExistingNode(s2));
}

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::removeArc(NodeType *n1, NodeType *n2) {
   Vector<ArcType *> toRemove;
   for (ArcType *arc : arcs) {
      if (arc->start == n1 && arc->finish == n2) {
         toRemove.add(arc);
      }
   }
   for (ArcType *arc : toRemove) {
      removeArc(arc);
   }
}

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::removeArc(ArcType *arc) {
   arc->start->arcs.remove(arc);
   arcs.remove(arc);
}

/*
 * Implementation notes: isConnected
 * ---------------------------------
 * Node n1 is connected to n2 if any of the arcs leaving n1 finish at n2.
 */

template <typename NodeType,typename ArcType>
bool Graph<NodeType,ArcType>::isConnected(std::string s1,
                                          std::string s2) const {
   return isConnected(getExistingNode(s1), getExistingNode(s2));
}

template <typename NodeType,typename ArcType>
bool Graph<NodeType,ArcType>::isConnected(NodeType *n1, NodeType *n2) const {
   for (ArcType *arc : n1->arcs) {
      if (arc->finish == n2) return true;
   }
   return false;
}

/*
 * Implementation notes: getNodeSet, getArcSet
 * -------------------------------------------
 * These methods simply return the set requested by the client.  For
 * efficiency, the sets are returned by reference, because doing so
 * eliminates the need to copy the set.
 */

template <typename NodeType,typename ArcType>
Set<NodeType *> & Graph<NodeType,ArcType>::getNodeSet() {
   return nodes;
}

template <typename NodeType,typename ArcType>
Set<ArcType *> & Graph<NodeType,ArcType>::getArcSet() {
   return arcs;
}

template <typename NodeType,typename ArcType>
Set<ArcType *> & Graph<NodeType,ArcType>::getArcSet(NodeType *node) {
   return node->arcs;
}

template <typename NodeType,typename ArcType>
Set<ArcType *> & Graph<NodeType,ArcType>::getArcSet(std::string name) {
   return getArcSet(getExistingNode(name));
}

/*
 * Implementation notes: getNeighbors
 * ----------------------------------
 * This implementation recomputes the set each time, which is reasonably
 * efficient if the degree of the node is small.
 */

template <typename NodeType,typename ArcType>
Set<NodeType *> Graph<NodeType,ArcType>::getNeighbors(NodeType *node) {
   Set<NodeType *> nodes;
   for (ArcType *arc : node->arcs) {
      nodes.add(arc->finish);
   }
   return nodes;
}

template <typename NodeType,typename ArcType>
Set<NodeType *> Graph<NodeType,ArcType>::getNeighbors(std::string name) {
   return getNeighbors(getExistingNode(name));
}

/*
 * Implementation notes: copy constructor and assignment operator
 * --------------------------------------------------------------
 * These methods ensure that copying a graph creates an entirely new
 * parallel structure of nodes and arcs.
 */

template <typename NodeType,typename ArcType>
const Graph<NodeType,ArcType> &
      Graph<NodeType,ArcType>::operator=(const Graph & src) {
   if (this != &src) {
      clear();
      deepCopy(src);
   }
   return *this;
}

template <typename NodeType,typename ArcType>
Graph<NodeType,ArcType>::Graph(const Graph & src) {
   deepCopy(src);
}

/*
 * Private method: deepCopy
 * ------------------------
 * This method reallocates all the nodes and arcs to ensure that the
 * structures are disjoint.
 */

template <typename NodeType,typename ArcType>
void Graph<NodeType,ArcType>::deepCopy(const Graph & other) {
   for (NodeType *oldNode : other.nodes) {
      NodeType *newNode = new NodeType();
      *newNode = *oldNode;
      newNode->arcs.clear();
      addNode(newNode);
   }
   for (ArcType *oldArc : other.arcs) {
      ArcType *newArc = new ArcType();
      *newArc = *oldArc;
      newArc->start = getExistingNode(oldArc->start->name);
      newArc->finish = getExistingNode(oldArc->finish->name);
      addArc(newArc);
   }
}

#endif
