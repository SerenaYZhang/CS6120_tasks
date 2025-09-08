import json
import sys


def print_operation():
    prog = json.load(sys.stdin)
    arith_ops = {"add", "sub", "mul", "div"}
    for func in prog["functions"]:
        for instr in func["instrs"]:
            if "op" in instr and instr["op"] in arith_ops:
                if instr["op"] == "add":
                    print("adding")
                elif instr["op"] == "sub":
                    print("subtracting")
                elif instr["op"] == "mul":
                    print("multiplying")
                elif instr["op"] == "div":
                    print("dividing")
    return 0


if __name__ == "__main__":
    print_operation()