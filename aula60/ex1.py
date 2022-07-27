class A:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
a = A()
a(1, 2, 3, 4, 5, nome = 'Julio', sobrenome = 'César')