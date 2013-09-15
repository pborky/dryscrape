"""
Headless Webkit driver for dryscrape. Wraps the ``webkit_server`` module.
"""

import dryscrape.mixins
try:
    import webkit_server as server
except ImportError:
    import webkit_scraper as server


class Node(server.Node,
           dryscrape.mixins.SelectionMixin,
           dryscrape.mixins.AttributeMixin):
  """ Node implementation wrapping a ``webkit_server`` node. """


class NodeFactory(server.NodeFactory):
  """ overrides the NodeFactory provided by ``webkit_server``. """
  def create(self, node_id):
    return Node(self.client, node_id)


class Driver(server.Client,
             dryscrape.mixins.WaitMixin,
             dryscrape.mixins.HtmlParsingMixin):
  """ Driver implementation wrapping a ``webkit_server`` driver.

  Keyword arguments are passed through to the underlying ``webkit_server.Client``
  constructor. By default, `node_factory_class` is set to use the dryscrape
  node implementation. """
  def __init__(self, **kw):
    kw.setdefault('node_factory_class', NodeFactory)
    super(Driver, self).__init__(**kw)
