import re

class Number:
    """
    数値を表すクラス。
    
    Attributes:
        value (int or float): 数値の値。
    """
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"Number({self.value})"
        
class Token:
    """
    トークンを表すクラス。
    
    Attributes:
        token (str): トークンの値。
        token_type (str): トークンの種類。
    """
    def __init__(self, token, token_type):
        self.token = token
        self.token_type = token_type
    
    def __repr__(self):
        return f"Token({self.token}, {self.token_type})"

class Lexer:
    """
    数式をトークンに分解するクラス。
    Attributes:
        expression (str): 数式の文字列。
    """
    
    def __init__(self, expression):
        self.expression = expression
        
    def __repr__(self):
        return f"Lexer({self.expression})"
    
    def tokenize(self):
        """
        数式をトークンに分解するメソッド。
        Returns:
            list: トークンのリスト。
        """

        raw_token = re.findall(r'\d+\.\d+|\d+|\*{2,}|/{2,}|[()+\-*/]|[^ \d()+\-*/]', self.expression)
        tokens = []
        paren_depth = 0
        
        for token in raw_token:
            if re.match(r'\d+\.\d+', token):
                tokens.append(Token(Number(float(token)), "NUMBER"))
            elif token.isdigit():
                tokens.append(Token(Number(int(token)), "NUMBER"))
            elif token == "+":
                tokens.append(Token(token, "PLUS"))
            elif token == "-":
                tokens.append(Token(token, "MINUS"))
            elif token == "*":
                tokens.append(Token(token, "STAR"))
            elif token == "/":
                tokens.append(Token(token, "SLASH"))
            elif token == "(":
                tokens.append(Token(token, "LPAREN"))
                paren_depth += 1
            elif token == ")":
                tokens.append(Token(token, "RPAREN"))
                paren_depth -= 1
            else:
                raise ValueError(f"Invalid token: {token}")
            
            if paren_depth < 0:
                raise ValueError(f"Error: Too many closing parentheses")
        
        if paren_depth != 0:
            raise ValueError(f"Error: Mismatched parentheses")
                
        return tokens