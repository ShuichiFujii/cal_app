from app.engine import ExpressionEngine

def eval_expr(expr):
    engine = ExpressionEngine(expr)
    return engine.evaluate()

def main():
    while True:
        expr = input("Enter an expression: ")
        
        if expr.lower() in ("exit", "quit"):
            break

        try:
            print(f"Answer >>> {eval_expr(expr)}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()