class Stack:

 def __init__(self):
    self.stack = []

 def isEmpty(self):
    if len(self.stack) == 0:
         return None
 def Size(self):
     return len(self.stack)
 def push(self, item):
    self.stack.append(item)

 def pop(self):
    removed = self.stack.pop()
    return removed
 def peek(self):
    item = self.stack.pop()
    self.stack.append(item)
    return item

def check(str_in):
     open_mark = [ "(","[", "{"]
     close_mark = [")","]", "}"]
     stack = []
     for i in str_in:
         if i in open_mark:
             stack.append(i)
         elif i in close_mark:
             pos = close_mark.index(i)
             if ((len(stack) > 0) and
                     (open_mark[pos] == stack[len(stack) - 1])):
                 stack.pop()

     if len(stack) == 0:
         return "Строка сбалансирована по скобкам"
     else:
         return "Строка НЕ сбалансирована по скобкам"

if __name__ == '__main__':
    s = Stack()
    s.push("A")
    s.push("N")
    s.push("A")
    s.push("X")
    s.push("O")
    print(f'Длина стека {s.Size()}')
    print(f'Из стека {s.pop()}{s.pop()}{s.pop()}{s.pop()}{s.pop()}')
    if s.isEmpty()==None:
        print('Стек пустой')
    else:
        print('Стек заполнен')

    str="{[]{()}}"
    print(f'Строка {str} {check(str)}')

    str = "(([]{()}})"
    print(f'Строка {str} {check(str)}')



