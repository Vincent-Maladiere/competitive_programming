"""
Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line.

Pad extra spaces ' ' when necessary so that each line has exactly maxWidth
characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is
inserted between words.
"""
import pytest
# %%
def justify_line(
    line,
    space_left,
    n_words_line,
    last_line=False,
):
    n_spaces = n_words_line - 1

    if n_words_line == 1 or last_line:
        # left justify
        for jdx in range(n_spaces):
            line[jdx] += " "
        line[-1] += space_left * " "

    else:
        # full justify
        space_length = space_left // n_spaces + 1
        space_length_extra = space_left % n_spaces

        for jdx in range(n_spaces):
            if jdx < space_length_extra:
                space_length_ = space_length + 1
            else:
                space_length_ = space_length
            line[jdx] += " " * space_length_

    return line


def justify(words, maxWidth):

    out = []
    line = []
    n_words_line = 0
    len_no_space = 0

    for idx, word in enumerate(words):

        len_word = len(word)
        space_left = maxWidth - (len_no_space + len_word + n_words_line)
        print(line, word, space_left)
        
        if space_left < 0:
            previous_space_left = space_left + len_word + 1
            line = justify_line(
                line,
                previous_space_left,
                n_words_line,
            )
            out.append("".join(line))

            line = []
            len_no_space = 0
            n_words_line = 0

        line.append(word)
        len_no_space += len_word
        n_words_line += 1

        if idx == len(words) - 1:
            space_left = maxWidth - (len_no_space + n_words_line - 1)
            line = justify_line(
                line,
                space_left,
                n_words_line,
                last_line=True,
            )
            out.append("".join(line))

    return out

words = ["Science", "is", "what", "we", "understand", "well", "enough",
         "to", "explain", "to", "a", "computer.",
         "Art", "is", "everything", "else", "we", "do",
        ]
maxWidth = 20
justify(words, maxWidth)



# %%

@pytest.mark.parametrize("words, maxWidth, expected", [
    (
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        ['This    is    an', 'example  of text', "justification.  "],
    ),
    (
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16,
        ["What   must   be", "acknowledgment  ", "shall be        "],
    ),
    (
        ["Science", "is", "what", "we", "understand", "well", "enough",
         "to", "explain", "to", "a", "computer.",
         "Art", "is", "everything", "else", "we", "do",
        ],
        20,
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
    )
])
def test_suite(words, maxWidth, expected):
    assert justify(words, maxWidth) == expected