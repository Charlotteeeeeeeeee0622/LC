class BrowserHistory:

    def __init__(self, homepage: str):
        self.stackin = [homepage]
        self.stackout = []

    def visit(self, url: str) -> None:
        self.stackin.append(url)
        self.stackout.clear()

    def back(self, steps: int) -> str:
        if steps < len(self.stackin):
            while steps:
                self.stackout.append(self.stackin.pop())
                steps -= 1
        else:
            slen = len(self.stackin)
            while slen - 1:
                self.stackout.append(self.stackin.pop())
                slen -= 1
        return self.stackin[-1]

    def forward(self, steps: int) -> str:
        if steps <= len(self.stackout):
            while steps:
                self.stackin.append(self.stackout.pop())
                steps -= 1
        else:
            slen = len(self.stackout)
            while slen:
                self.stackin.append(self.stackout.pop())
                slen -= 1

        return self.stackin[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)