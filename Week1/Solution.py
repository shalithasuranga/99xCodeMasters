class Stack:
    A = []
    def push(self, x):
        self.A.append(x)
    def pop(self):
        if(len(self.A) == 0):
            return False
        else:
            return self.A.pop(self.size() - 1)
    def size(self):
        return len(self.A)

def run():
    S = list(input().strip())
    stack = Stack()
    for i in S:
        if(i == '[' or i == '('):
            stack.push(i)
        elif(i == ']'):
            if(stack.pop() != '['):
                return "INVALID"
        elif(i == ')'):
            if(stack.pop() != '('):
                return "INVALID"
            
    if(stack.size() == 0):
        return "VALID"
    else:
        return "INVALID"

print(run())
