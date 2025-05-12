from app.lexer import Lexer
from app.parser import Parser
from app.evaluator import Evaluator

class ExpressionEngine:
    """
    数式を評価するためのゲートウェイクラス。
    数式を文字列として受け取り、構文解析を行い、評価結果を返す。
    
    Attributes:
        expression (str): 数式の文字列
        ast (ASTNode): 構文木のルートノード    
    """
    def __init__(self, expression=""):
        self.expression = str(expression).strip()
        self.ast = self._build_ast()
        
    def _build_ast(self):
        lexer = Lexer(self.expression)
        tokens = lexer.tokenize()
        parser = Parser(tokens)        
        ast = parser.parse_expression()
        
        if parser.current_token is not None:
            raise ValueError(f"Unexpected token: {parser.current_token}")

        # print("Tokens:", tokens)
        # print("AST:", ast)
        # print("Result:", ast)
        
        return ast

    def evaluate(self):
        evaluator = Evaluator()
        # print("評価対象トークン列:", self.expression)
        return evaluator.evaluate(self.ast)