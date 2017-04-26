"""
For a given string and dictionary, how many sentences can you make from the
string, such that all the words are contained in the dictionary.

eg: for given string -> "appletablet"
"apple", "tablet"
"applet", "able", "t"
"apple", "table", "t"
"app", "let", "able", "t"

"applet", {app, let, apple, t, applet} => 3
"thing", {"thing"} -> 1
"""

class MakeSentence(object):

    def __init__(self, example_string, dictionarys):
        self.count = 0
        self.example_string = example_string
        self.dictionarys = dictionarys

    def run(self):
        self.make_sentence(self.example_string, self.dictionarys)
        print(self.count)

    def make_sentence(self, str_piece, dictionarys):
        if len(str_piece) == 0:
            return True
        for i in range(0, len(str_piece)):
            prefix, suffix = str_piece[0:i], str_piece[i:]
            if ((prefix in dictionarys and suffix in dictionarys)
                    or (prefix in dictionarys and self.make_sentence(suffix, dictionarys))):
                self.count += 1
        return True

if __name__ == "__main__":
    dictionarys = ["", "app", "let", "t", "apple", "applet"]
    make_sentence = MakeSentence("applet", dictionarys)
    make_sentence.run()
