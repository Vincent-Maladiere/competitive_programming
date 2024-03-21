"""Mobile telephones with keys offer an interesting input mode, sometimes called T9.
The 26 letters of the alphabet are distributed over the keys 2 to 9, as in Figure 2.1.
To input a word, it suffices to input the corresponding sequence of digits. However, as
several words could begin with the same digits, a dictionary must be used to propose
the most probable word. At any moment, the telephone displays the prefix of the most
probable word corresponding to the sequence of digits entered.
"""

# %%
from copy import deepcopy


def t9(x):
    """
    For each T9 combination entered by the user, this solution looks at
    the first letter of each word of the vocabulary at the first key hit,
    then narrows the vocabulary to the valid options.
    
    Since words can be up to 100 characters long, storing them in a tree would
    result in an worst space complexity of 9 ** 100, which is infeasible.

    So, linearly scanning the vocabulary in O(vocab_size) time sounds reasonable
    for the first iteration.

    Was the vocabulary very large, using a max-heap to pop in O(1) the most
    probable word would be more time efficient than using a max() of time complexity
    O(size_word_remaining), at the expense of memory complexity.
    """
    inputs = _parser(x)
    keyboard = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"],
    ]

    out = []

    for idx_scenario, input in enumerate(inputs, 1):
        out.append(f"\nScenario #{idx_scenario}:\n")
        
        vocab_probas, user_typing = input["vocab"], input["user_typing"]
        vocab = list(vocab_probas)

        for typing in user_typing:
            vocab_options = deepcopy(vocab)

            predictions = []
            
            for idx, key in enumerate(typing[:-1]):
                words_to_keep = []
                letters = keyboard[int(key)-2]
                for word in vocab_options:
                    if len(word) > idx and word[idx] in letters:
                        words_to_keep.append((int(vocab_probas[word]), word))

                if words_to_keep:
                    _, prediction = max(words_to_keep)
                    prediction = prediction[:idx+1]
                    _, vocab_options = zip(*words_to_keep)
                else:
                    prediction = "MANUALLY"
                    vocab_options = []
                
                predictions.append(prediction)

            out.append("\n".join(predictions))
            out.append("\n\n")

    return "".join(out)


def _parser(x):
    """Parse a text input into a list of dict.

    Each dict has the keys "vocab" and "user_typing", where:
    * vocab is a dict that maps words to probabilities
    * user_typing is a list of string representing the user entries.
    """
    x = x.split()
    n_inputs = int(x[0])
    inputs = []
    offset = 0

    for _ in range(n_inputs):

        # get vocab
        n_words = int(x[offset + 1])
        idx_word_start = offset + 2
        idx_word_end = idx_word_start + n_words * 2
        word_probas = x[idx_word_start:idx_word_end]
        words = word_probas[:-1:2]
        probas = word_probas[1::2]
        vocab = dict(zip(words, probas))

        # get user typing
        n_typing = int(x[idx_word_end])
        idx_typing_start = idx_word_end + 1
        idx_typing_end = idx_typing_start + n_typing
        user_typing = x[idx_typing_start:idx_typing_end]

        inputs.append(
            dict(
                vocab=vocab,
                user_typing=user_typing,
            )
        )

        offset = idx_typing_end - 1

    return inputs


# %%


def test_parser():
    x = """
        2
        5
        hell 3
        hello 4
        idea 8
        next 8
        super 3
        2
        435561
        43321
        7
        another 5
        contest 6
        follow 3
        give 13
        integer 6
        new 14
        program 4
        5
        77647261
        6391
        4681
        26684371
        77771
    """

    out = _parser(x)

    expected_out = [
        {
            "vocab": {
                "hell": "3",
                "hello": "4",
                "idea": "8",
                "next": "8",
                "super": "3",
            },
            "user_typing": ["435561", "43321"],
        },
        {
            "vocab": {
                "another": "5",
                "contest": "6",
                "follow": "3",
                "give": "13",
                "integer": "6",
                "new": "14",
                "program": "4",
            },
            "user_typing": ["77647261", "6391", "4681", "26684371", "77771"],
        },
    ]
    assert out == expected_out


def test_example():
    """Given in http://poj.org/problem?id=1451."""

    x = """
        2
        5
        hell 3
        hello 4
        idea 8
        next 8
        super 3
        2
        435561
        43321
        7
        another 5
        contest 6
        follow 3
        give 13
        integer 6
        new 14
        program 4
        5
        77647261
        6391
        4681
        26684371
        77771
    """
    out = t9(x)

    expected_out = """
        Scenario #1:
        i
        id
        hel
        hell
        hello

        i
        id
        ide
        idea


        Scenario #2:
        p
        pr
        pro
        prog
        progr
        progra
        program

        n
        ne
        new

        g
        in
        int

        c
        co
        con
        cont
        anoth
        anothe
        another

        p
        pr
        MANUALLY
        MANUALLY

    """

    assert out.replace(" ", "") == expected_out.replace(" ", "")
