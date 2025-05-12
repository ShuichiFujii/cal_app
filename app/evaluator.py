from app.lexer import Number
from app.parser import BinaryOp, UnaryOp


class Evaluator:
    """
    数式を評価するクラス。
    数式の構文木を受け取り、評価結果を返す。

    Attributes:
        None
    """
    def evaluate(self, node):
        if isinstance(node, Number):
            return node.value
        
        elif isinstance(node, UnaryOp):
            op = self.evaluate(node.expr)
            if node.op.token_type == "MINUS":
                return -op
            
            elif node.op.token_type == "PLUS":
                return +op
            
            else:
                raise ValueError(f"Unknown unary operator: {node.op.token_type}")
            
        elif isinstance(node, BinaryOp):
            left = self.evaluate(node.left)
            op = node.op.token_type
            right = self.evaluate(node.right)
            
            if op == "PLUS":
                return left + right
            
            elif op == "MINUS":
                return left - right
            
            elif op == "STAR":
                return left * right
            
            elif op == "SLASH":
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                
                answer = left / right
                return int(answer) if answer.is_integer() else answer
            
        else:
            raise TypeError(f"Unknown node type: {node}")
        
        
