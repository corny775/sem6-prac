decision_tree = {
    "question": "engine wont start",
    "yes": {
        "question": "battery warning light on",
        "yes": "dead or weak battery",
        "no": "starter motor or ignition problem",
    },
    "no": {
        "question": "high temperature gauge",
        "yes": {
            "question": "coolant level low",
            "yes": "coolant leak or low coolant",
            "no": "engine overheating",
        },
        "no": {
            "question": "vehicle pulling to side",
            "yes": {
                "question": "uneven tire wear",
                "yes": "wheel alignment problem",
                "no": "tire pressure imbalance",
            },
            "no": {
                "question": "warning lights on dashboard",
                "yes": {
                    "question": "check engine light on",
                    "yes": "engine sensor or emission issue",
                    "no": "electrical or system fault",
                },
                "no": {
                    "question": "brakes making noise",
                    "yes": "worn brake pads or brake issue",
                    "no": "No clear issue found",
                },
            },
        },
    },
}

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with y or n.")

def traverse_tree(tree):
    if isinstance(tree, str):
        return tree
    return traverse_tree(tree["yes"] if ask_yes_no(
        f"Do you observe {tree['question']}? [y/n]: ") else tree["no"])

def inference(tree):
    print("\n--- Diagnostic Result ---")
    print("Most likely issue:", traverse_tree(tree) + ".")

def make_decision():
    print("--- Vehicle Diagnostics Expert System ---")
    print("Answer with y/n\n")
    inference(decision_tree)

make_decision()