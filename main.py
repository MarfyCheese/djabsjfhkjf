class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() * self.right.eval()
class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def eval(self):
        return self.left.eval() + self.right.eval()
class NumNode:
    def __init__(self, num):
        self.num = num
    def eval(self):
        return self.num

def parse_prefix(inString):
    """Take a string in prefix notation, e.g. "+ + * 4 5 6 7", and
    produce an Abstract Syntax Tree representing the expression."""

    tokens = inString.split()

    # TODO: Implement the rest.

    def parse_num(token):
        try:
             return float(token)
        except ValueError:
             return token

    tokens = [parse_num(token) for token in tokens]

    def __parse(tokens):
        if len(tokens) > 0:
            head = tokens[0]
            tail = tokens[1:]

            if isinstance(head, float):
                 return NumNode(head), tail
            elif head == "+":
                left, rest = __parse(tail)
                right, rest = __parse(rest)
                return PlusNode(left, right), rest
            elif head == "*":
                left, rest = __parse(tail)
                right, rest = __parse(rest)
                return TimesNode(left, right), rest
        else:
            pass
    tree, _ = __parse(tokens)
    return tree
    

def main():
    ast = parse_prefix("+ + * 4 5 6 7")
    print(ast.eval())
if __name__ == "__main__":
    main()