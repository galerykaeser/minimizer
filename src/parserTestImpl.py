from parserbase import ParserBase


class Parser(ParserBase):
    def parse(self, output):
        cond1 = "caught signal 11 -- exiting" in output
        cond2 = "caught signal 6 -- exiting" in output
        return cond1 or cond2
