class BinaryOp:
    """ 
    二項の演算子を表すクラス。
    例: x + y, x - y, x * y, x / y
    
    Attributes:
        left: 演算子の左側の式
        op: 演算子トークン
        right: 演算子の右側の式
    """
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def __repr__(self):
        return f"BinaryOp({self.left}, {self.op}, {self.right})"

class UnaryOp:
    """ 
    単項の演算子を表すクラス。
    例: -x, +x 
    
    Attributes:
        op: 演算子トークン
        expr: 演算子の右側の式
    """
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr
        
    def __repr__(self):
        return f"UnaryOp({self.op}, {self.expr})"
        
class Parser:
    """ 
    数式を解析するクラス。
    トークン列を受け取り、AST（抽象構文木）を生成する。
    
    Attributes:
        tokens: トークン列
        pos: 現在のトークンの位置
        current_token: 現在のトークン    
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None
        
    def advance(self):
        """ 
        トークン列の次のトークンに移動する。
        トークン列の終端に達した場合は、Noneを設定する。
        """
        
        self.pos += 1
        
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None
            
    def parse_expression(self):
        """
        数式を解析するメソッド。
        """
        
        if self.current_token is None:
            raise ValueError("Empty expression")
        
        left = self.parse_term()
        
        while self.current_token is not None and self.current_token.token_type in ("PLUS", "MINUS"):
            op = self.current_token
            self.advance()
            right = self.parse_term()
            left = BinaryOp(left, op, right)
            
        return left
    
    def parse_term(self):
        """
        数式の項を解析するメソッド。
        """
        
        left = self.parse_factor()
        
        while self.current_token is not None and self.current_token.token_type in ("STAR", "SLASH"):
            op = self.current_token
            self.advance()
            right = self.parse_factor()
            left = BinaryOp(left, op, right)
            
        return left

    def parse_factor(self):
        """
        数式の因子を解析するメソッド。
        """

        token = self.current_token

        if token.token_type in ("PLUS", "MINUS"):
            self.advance()
            factor = self.parse_factor()  # 再帰呼び出しで中身を取る
            return UnaryOp(token, factor)

        return self.parse_atom()

    def parse_atom(self):
        """
        数式の原子を解析するメソッド。
        原子は数値または括弧で囲まれた式を表す。
        """

        token = self.current_token

        if token.token_type == "NUMBER":
            self.advance()
            return token.token
        elif token.token_type == "LPAREN":
            self.advance()
            node = self.parse_expression()
            
            if self.current_token is None or self.current_token.token_type != "RPAREN":
                raise ValueError("Expected ')'")
            
            self.advance()
            return node
        
        else:
            raise ValueError(f"Unexpected token: {token}")
        