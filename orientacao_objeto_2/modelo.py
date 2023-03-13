class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def get_likes(self):
        return self.__likes

    @property
    def get_ano(self):
        return self.__ano

    @property
    def get_duracao(self):
        return self.__duracao

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    @property
    def get_nome(self):
        return self.__nome

    @get_nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def get_likes(self):
        return self.__likes

    @property
    def get_ano(self):
        return self.__ano

    @property
    def get_temporadas(self):
        return self.__temporadas

    def dar_like(self):
        self.__likes += 1


vingadores = Filme("vingadores guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
print(f"Nome: {vingadores.nome.title()} - Ano: {vingadores.get_ano} "
      f"- Duração: {vingadores.get_duracao} min - Likes: {vingadores.get_likes}")
vingadores.dar_like()
vingadores.dar_like()
print(f"Nome: {vingadores.nome.title()} - Ano: {vingadores.get_ano} "
      f"- Duração: {vingadores.get_duracao} min - {vingadores.get_likes}")

atlanta.nome = "Atllanta"
print(f"Nome: {atlanta.nome.title()} - Ano: {atlanta.get_ano} "
      f"- Temporadas: {atlanta.get_temporadas}")
