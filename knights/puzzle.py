from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),

    # Info from the given statements
    Biconditional(And(AKnight, AKnave), AKnight) # A says "I am both a knight and a knave."
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Or(BKnight, BKnave),
    Not(And(AKnave, AKnight)),
    Not(And(BKnight, BKnave)),

    # Info from the given statements
    Biconditional(And(AKnave, BKnave), AKnight), # A says "We are both knaves."
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Or(BKnight, BKnave),
    Not(And(AKnave, AKnight)),
    Not(And(BKnight, BKnave)),

    # Info from the given statements
    Biconditional(Or(And(AKnight, BKnight),     # A says "We are the same kind."
        And(AKnave, BKnave)), AKnight), 
    Biconditional(Or(And(AKnight, BKnave),      # B says "We are of different kinds."
        And(AKnave, BKnight)), BKnight), 
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Or(BKnight, BKnave),
    Or(CKnave, CKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Info from the given statements

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Biconditional(And(Or(AKnight, AKnave), 
        Not(And(AKnave, AKnight))), AKnight),
    
    # B says "A said 'I am a knave'."
    Biconditional(Biconditional(AKnave, AKnight), BKnight),
    
    Biconditional(CKnave, BKnight),     # B says "C is a knave."
    Biconditional(AKnight, CKnight),    # C says "A is a knight."
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
