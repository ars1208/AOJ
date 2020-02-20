class Queue:
    def __init__(self, Q = []):
        self.Q = Q

    def enqueue(self, data):
        self.Q.append(data)
        return self.Q

    def dequeue(self):
        if len(self.Q) == 0:
            return 0
        else:
            cell = self.Q[0]
            del self.Q[0]
            return self.Q


if __name__ == '__main__':
    n, q = map(int, input().split())
    p_dict = dict()
    for i in range(n):
        p, p_value = input().split()
        p_dict[p] = int(p_value)

    Q = Queue()
    
