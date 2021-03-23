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
    # could be a Knight or a Knave
    Or(AKnight, AKnave),
    # if is a knight then can't be a knave and viseversa
    Not(Biconditional(AKnight, AKnave)),

    # A says
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # could be a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # if is a knight then can't be a knave and viseversa
    Not(Biconditional(AKnight, AKnave)),
    Not(Biconditional(BKnight, BKnave)),
    # sencence
    Implication(AKnight, And(BKnave, AKnave)),
    Implication(AKnave, Not(And(BKnave, AKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # could be a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # if is a knight then can't be a knave and viseversa
    Not(Biconditional(AKnight, AKnave)),
    Not(Biconditional(BKnight, BKnave)),
    # sencences
    # A says
    Implication(AKnight,
        Or(
            And(BKnave, AKnave),
            And(BKnight, AKnight)
        )
    ),
    Implication(AKnave,
        Not(Or(
            And(BKnave, AKnave),
            And(BKnight, AKnight)
        ))
    ),
    
    # B says
    Implication(BKnight,
        Or(
            And(BKnave, BKnave),
            And(BKnight, AKnave)
        )
    ),
    Implication(BKnave,
        Not(Or(
            And(BKnave, BKnave),
            And(BKnight, AKnave)
        ))
    ),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # could be a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # if is a knight then can't be a knave and viseversa
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Implication(CKnight, Not(CKnave)),
    Implication(CKnave, Not(CKnight)),
    # A says
    Implication(AKnight, Not(Biconditional(AKnight, AKnave))),
    Implication(AKnave, Biconditional(AKnight, AKnave)),
    # B says that A said
    Implication(BKnight,
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        )
    ),
    Implication(BKnave,
        Not(And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave))
        ))
    ),
    # B says again
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # C says
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
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
