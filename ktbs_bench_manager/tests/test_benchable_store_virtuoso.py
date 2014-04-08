import pytest
from ktbs_bench_manager import BenchableGraph
import rdflib


# This store should be running when running the tests
EMPTY_STORE = {'store_id': 'http://localhost/bs/virtuoso/test/empty_store/',
               'config': ("http://localhost:8890/sparql/", "http://localhost:8890/sparql/")}


class TestVirtuoso(object):
    def test_fail_connect_query(self):
        """Test that the store should not connect if the query endpoint is wrong."""
        bad_query_endpoint = 'http://should_fail/'
        virtuoso = BenchableGraph("SPARQLUpdateStore",
                                  EMPTY_STORE['store_id'],
                                  (bad_query_endpoint, EMPTY_STORE['config'][1]),
                                  graph_create=False)
        fail = False
        try:
            virtuoso.connect()
            # Doing a query forces RDFLib to actually connect to the query endpoint
            virtuoso.graph.query('select * where {?s ?p ?o}')
        except:
            fail = True
        assert fail

    def test_fail_connect_update(self):
        """Test that the store should not connect if the update endpoint is wrong."""
        bad_update_endpoint = 'http://should_fail'
        virtuoso = BenchableGraph('SPARQLUpdateStore',
                                  EMPTY_STORE['store_id'],
                                  (EMPTY_STORE['config'][0], bad_update_endpoint),
                                  graph_create=False)
        fail = False
        triple = (rdflib.URIRef('s'), rdflib.URIRef('p'), rdflib.URIRef('o'))
        try:
            virtuoso.connect()
            # Doing an add forces RDFLib to actually connect to the update endpoint
            virtuoso.graph.add(triple)
        except:
            fail = True
        else:
            virtuoso.graph.remove(triple)
        assert fail

    def test_succeed_connect(self):
        """Test if the server is up."""
        virtuoso = BenchableGraph('SPARQLUpdateStore',
                                  EMPTY_STORE['store_id'],
                                  EMPTY_STORE['config'],
                                  graph_create=False)
        succeed = True
        try:
            virtuoso.connect()
            virtuoso.graph.query('select * where {?s ?p ?o}')
        except:
            succeed = False
        assert succeed
