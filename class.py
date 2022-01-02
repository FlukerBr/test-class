class user:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomereverso = user.textoreverso(nome)

    def textoreverso(text):
        l = len(text)
        textr = ''
        while l > 0:
            l -= 1 
            a = text[l]
            textr += a
        return textr
usuario1 = user('rodrigo', '18')
usuario2 = user('luiz', '12')
print(usuario1.nome)
usuario2.nome = 'paulo'
print(usuario2.nome)
print(usuario1.nomereverso)
