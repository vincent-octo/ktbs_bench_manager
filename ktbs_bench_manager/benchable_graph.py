from rdflib import Graph


__all__ = ['BenchableGraph']


class BenchableGraph(object):
    """
    Provides a convenient way to use a graph for benchmarks.

    """
    def __init__(self, store, graph_id, store_config, graph_create=False):
        """
        :param str store: Type of store to use.
        :param str graph_id: The graph identifier.
        :param store_config: Configuration to open the store.
        :type store_config: str or tuple
        :param bool graph_create: True to create the graph upon connecting.
        """
        self.graph = Graph(store=store, identifier=graph_id)
        self._graph_id = graph_id
        self._store_config = store_config
        self._graph_create = graph_create

    def connect(self):
        """Connect to the store.

        .. note::

            For some configurations, RDFlib will postpone the actual connection to
            the store until needed (when doing a graph.query() or graph.add()).

            This behaviour comes from RDFbib implementation of graph.open().
        """
        return self.graph.open(configuration=self._store_config, create=self._graph_create)

    def close(self, commit_pending_transaction=True):
        """Close a connection to a store.

        :param bool commit_pending_transaction: True if to commit pending transaction before closing, False otherwise.

        .. note::
            The graph.close() method is not implemented for SPARQL Store in RDFLib
        """
        self.graph.close(commit_pending_transaction=commit_pending_transaction)
