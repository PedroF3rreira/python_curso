class RevelaAcesso:
    def __init__(self, valor_inicial=None, name="my_var"):
        self.valor = valor_inicial
        self.name = name

        def __get__(self, instance, woner):
            print("recuperando valor de ", self.name)
            return self.val

        def __set__(self, instance, value):
            print("atualizando valor de ", self.name)
            self.name = value
