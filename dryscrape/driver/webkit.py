"""
Headless Webkit driver for dryscrape. Wraps the ``webkit_server`` module.
"""

import dryscrape.mixins
import webkit_server

class Node(webkit_server.Node, dryscrape.mixins.SelectionMixin,
                               dryscrape.mixins.AttributeMixin):
  """ node implementation wrapping a ``webkit_server``
  node. """
  def __init__(self, *args):
    super(Node, self).__init__(*args)

  def _create_node(self, id):
    return Node(self.driver, id)

class Driver(webkit_server.Driver, dryscrape.mixins.DriverMixin):
  """ driver implementation wrapping a ``webkit_server``
  driver. """
  def __init__(self):
    super(Driver, self).__init__()

  def _create_node(self, id):
    return Node(self, id)