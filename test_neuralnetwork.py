# test_neuralnetwork.py
"""
Tests for NeuralNetwork module.
"""

import unittest
from neuralnetwork import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):
    """Test cases for NeuralNetwork class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralNetwork()
        self.assertIsInstance(instance, NeuralNetwork)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralNetwork()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
