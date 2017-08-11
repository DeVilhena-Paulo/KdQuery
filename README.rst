=======
KdQuery
=======

KdQuery is a python package that defines one possible implementation of kd-trees using list to avoid recursion, but most importantly it defines a general method to find the nearest node for any kd-tree implementation.

Getting Started
===============

Prerequisites
-------------

* Python version 3.6 installed locally
* Pip installed locally

Installing
----------

The package can easily be installed via pip::

  pip install KdQuery

Usage
=====

The Tree class with the default settings:

.. code-block:: python

    from kdquery import Tree

    # Create a kd-tree (k = 2 and capacity = 10000 by default)
    tree = Tree()

    # Insert points with some attached data (or not)
    # The method returns the identifier of the internal
    # representation of the node.
    node_id = tree.insert((0, 3), 'Important data')
    tree.insert((9, 1), {'description': 'point in the plane', 'label': 6})
    tree.insert((1, -8))
    tree.insert((-3, 3), data=None)
    tree.insert((0.2, 3.89), ["blue", "yellow", "python"])

    # Recover the data attached to (0, 3)
    # The get_node mehtod returns an object
    node = tree.get_node(node_id)
    print(node.data)  # prints: 'Important data'

    # Find the node in the tree that is nearest to a given point
    query = (7.2, 1.2)
    node_id, dist = tree.find_nearest_point(query)
    print(dist)  # 1.8110770276274832

The Tree class with the optional arguments:

.. code-block:: python

    from kdquery import Tree

    # Create a 3d-tree with capacity of 3000000 nodes and delimited by a well
    # definied region
    x_limits = [-100, 100]
    y_limits = [-10000, 250]
    z_limits = [-1500, 10]

    region = [x_limits, y_limits, z_limits]
    capacity = 3000000

    tree = Tree(3, capacity, region)

The nearest_point method:

    # Let's say that in your application you have some positions over the
    # superface of the Earth and that you implement a kd-tree where each
    # node is stored as an element of a array with these specifications:
    #
    # node_dtype = np.dtype([
    #    ('longitude', 'float64'),
    #    ('latitude', 'float64'),
    #    ('limit_left', 'float64'),
    #    ('limit_right', 'float64'),
    #    ('limit_bottom', 'float64'),
    #    ('limit_top', 'float64'),
    #    ('dimension', 'float64'),
    #    ('left', 'int32'),
    #    ('right', 'int32')
    # ])
    #
    # If you need to find the node in this kd-tree implementation that is
    # nearest to a given point for the spherical distance, you can use
    # the nearest_point method from this package by simply definig a method
    # that receives the index of a node in this representation and returns
    # the coordinates of the node, the region where it is, the index for
    # the left child and the index for the right child. For this implementation
    # it could be something like:

    def get_properties(node_id):
        node = data['kdtree'][node_id]

        horizontal_limits = [node['limit_left'], node['limit_right']]
        vertical_limits = [node['limit_bottom'], node['limit_top']]

        region = [horizontal_limits, vertical_limits]
        coordinates = (node['longitude']), node['latitude']))
        dimension = node['dimension']
        left, right = node['left'], node['right']

        return coordinates, region, dimension, True, left, right

    # The syntax:
    import kdquery

    def spherical_dist(point1, point2):
        theta = point1[0] - point2[0]
        phi = point1[1] - point2[1]
        return math.acos(math.cos(theta) * math.cos(phi))

    query = (2.21, 48.65)
    root_id  # index of the root
    node_id, dist = kdquery.nearest_point(query, root_id, get_properties,
                                          spherical_dist)

