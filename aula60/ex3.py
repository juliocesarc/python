class A:
    def __init__(self):
        pass
    def __del__(self):
        print('O objeto foi deletado!')

a = A()
print(a)