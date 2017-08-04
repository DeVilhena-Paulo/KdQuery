import numpy.random as npr
import unittest

from KdQuery import Tree


class TestKdtree(unittest.TestCase):

    def test_kdtree_consistency(self):
        tree = Tree(k, capacity)

        points = (npr.rand(capacity, k) - 0.5) * size
        for point in points:
            tree.insert(point)

        for node in tree:
            point = node.point
            axis = node.axis

            left_id = node.left
            if left_id is not None:
                left_child = tree.get_node(left_id).point
                self.assertLess(left_child[axis], point[axis])

            right_id = node.right
            if right_id is not None:
                right_child = tree.get_node(right_id).point
                self.assertGreaterEqual(right_child[axis], point[axis])

    def test_find_nearest_point(self):
        tree = Tree(k, capacity)
        points = (npr.rand(capacity, k) - 0.5) * size
        for point in points:
            tree.insert(point)

        radius = 10 ** -3
        n_tests = 5
        for node in tree:
            point = node.point
            perturbation = (npr.rand(n_tests, k) - 0.5) * radius

            for epsilon in perturbation:
                query = point + epsilon
                ind, dist, cnt = tree.find_nearest_point(query)
                self.assertEqual(list(tree.node_list[ind].point), list(point))


if __name__ == '__main__':
    size = 1000
    capacity = 3000
    k = 4
    unittest.main()
