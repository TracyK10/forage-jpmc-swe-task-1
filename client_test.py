import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_results = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]

    for quote, expected in zip(quotes, expected_results):
      self.assertEqual(getDataPoint(quote), expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_results = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]

    for quote, expected in zip(quotes, expected_results):
      self.assertEqual(getDataPoint(quote), expected)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
        # Test when price_b is zero
        self.assertIsNone(getRatio(120.48, 0))

        # Test when both prices are positive
        self.assertEqual(getRatio(120.48, 121.2), 120.48 / 121.2)

        # Test when price_a is zero
        self.assertEqual(getRatio(0, 121.2), 0 / 121.2)

        # Test when both prices are zero (should handle division by zero)
        self.assertIsNone(getRatio(0, 0))


if __name__ == '__main__':
    unittest.main()
