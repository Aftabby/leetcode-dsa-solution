'''
problem_name = Design Browser History
problem_source = https://leetcode.com/problems/design-browser-history/description/

Algo 
    -
'''
class Page:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.home = self.curr = Page(homepage)

    def visit(self, url: str) -> None:
        self.curr = Page(url, self.curr)
        self.curr.prev.next = self.curr

    def back(self, steps: int) -> str:
        while self.curr != self.home and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next != None and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)