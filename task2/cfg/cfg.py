import json
import sys


def form_blocks(func):
    label_index = 0
    label_map = {}
    blocks = {}
    current_block = []
    terminators = set(["jmp", "br"])
    for instr in func["instrs"]:
        if 'op' in instr and instr['op'] in terminators:
            current_block.append(instr)
            blocks[label_index] = current_block
            current_block = []
            label_index += 1
        elif "label" in instr:
            if len(current_block) != 0:
                blocks[label_index] = current_block
                label_index += 1
            current_block = [instr]
            label_map[instr["label"]] = label_index
        else:
            current_block.append(instr)
    blocks[label_index] = current_block
    return blocks, label_map


def find_cfg(blocks, label_map):
    cfg = {}
    labels = list(blocks.keys())
    for i, label in enumerate(labels):
        cfg[label] = []
        block = blocks[label]
        if len(block) == 0:
            continue
        last_instr = block[-1]
        op = last_instr.get("op")
        if op == "jmp":
            target = last_instr["labels"][0]
            cfg[label].append(label_map[target])
        elif op == "br":
            true_target = last_instr["labels"][0]
            false_target = last_instr["labels"][1]
            cfg[label].append(label_map[true_target])
            cfg[label].append(label_map[false_target])
        else:
            if i + 1 < len(labels):
                next_label = labels[i + 1]
                cfg[label].append(next_label)
            else:
                cfg[label].append("exit")
    return cfg


def cfg():
    prog = json.load(sys.stdin)
    for func in prog["functions"]:
        blocks, label_map = form_blocks(func)
        for label, instrs in blocks.items():
            print(f"Label {label}: \t{instrs[0]}")
            if len(instrs) > 1:
                for instr in instrs[1:]:
                    print(f"\t\t\t\t\t{instr}")
        print("\n")
        graph = find_cfg(blocks, label_map)
        print(f"Function {func['name']}:")
        for label, successors in graph.items():
            print(f"  Block '{label}' -> {successors}")
    return 0


if __name__ == "__main__":
    cfg()