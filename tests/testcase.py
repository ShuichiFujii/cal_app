from unittest import TestCase
from app.engine import ExpressionEngine

class TestEvaluator(TestCase):
    def eval_expr(self, expr):
        engine = ExpressionEngine(expr)
        return engine.evaluate()
    
    def test_basic_operation(self):
        self.assertEqual(self.eval_expr("1 + 2"), 3)
        self.assertEqual(self.eval_expr("4 - 2"), 2)
        self.assertEqual(self.eval_expr("3 * 2"), 6)
        self.assertEqual(self.eval_expr("8 / 2"), 4)
        self.assertEqual(self.eval_expr(124 - 3), 121)
        
    def test_multiple_operations(self):
        self.assertEqual(self.eval_expr("1 ++++++++++ 2"), 3)
        self.assertEqual(self.eval_expr("1 + 2 -- 3"), 6)
        self.assertEqual(self.eval_expr("--- 3"), -3)
        self.assertEqual(self.eval_expr("2 +++ 3 -- 1"), 6)
        
    def test_unary_operation(self):
        self.assertEqual(self.eval_expr("-5"), -5)
        self.assertEqual(self.eval_expr("+3"), 3)
        self.assertEqual(self.eval_expr("-(3 + 2)"), -5)
        self.assertEqual(self.eval_expr("-(2 * 3)"), -6)
        
    def test_parentheses(self):
        self.assertEqual(self.eval_expr("(1 + 2) * 3"), 9)
        self.assertEqual(self.eval_expr("3 * (2 + 1)"), 9)
        self.assertEqual(self.eval_expr("(4 - 2) / 2"), 1)
        self.assertEqual(self.eval_expr("2 * (3 + 4) - 5"), 9)
        
    def test_division_and_float(self):
        self.assertEqual(self.eval_expr("4 / 2"), 2)
        self.assertEqual(self.eval_expr("5 / 2"), 2.5)
        self.assertEqual(self.eval_expr("7 / 3"), 2.3333333333333335)
        self.assertEqual(self.eval_expr("1.5 * 2"), 3)
        
    def test_complex_expression(self):
        self.assertEqual(self.eval_expr("1 + 2 * (-3) + 4 - (-5) / 2"), 1.5)
        self.assertEqual(self.eval_expr("3 * (2 + 1) - ((-4) / 2) * (-1)"), 7)
        
    def test_one_number(self):
        self.assertEqual(self.eval_expr("5"), 5)
        self.assertEqual(self.eval_expr("0"), 0)
        self.assertEqual(self.eval_expr("-3"), -3)
        self.assertEqual(self.eval_expr("1.5"), 1.5)
        
    def test_empty_expression(self):
        with self.assertRaises(Exception):
            self.eval_expr("")
        with self.assertRaises(Exception):
            self.eval_expr("     ")
        with self.assertRaises(Exception):
            self.eval_expr("()")
        
    def test_invalid_symbols(self):
        with self.assertRaises(Exception):
            self.eval_expr("1 %")
        with self.assertRaises(Exception):
            self.eval_expr("((1 # 2)")
        with self.assertRaises(Exception):
            self.eval_expr("1 @ 0")
        with self.assertRaises(Exception):
            self.eval_expr("1 | 2")
        with self.assertRaises(Exception):
            self.eval_expr("==1  2-1  fs93")
            
    
    def test_invalid_expressions(self):
        with self.assertRaises(Exception):
            self.eval_expr("1 +")
        with self.assertRaises(Exception):
            self.eval_expr("((1 + 2)")
        with self.assertRaises(Exception):
            self.eval_expr("1 / 0")
        with self.assertRaises(Exception):
            self.eval_expr("1 ** 2")
        with self.assertRaises(Exception):
            self.eval_expr("1                   2")
        with self.assertRaises(Exception):
            self.eval_expr()