from BatalhaService import BatalhaService
from Pokemon import Pokemon

# Treinador, que depende do serviço de batalha
class Treinador:
    def __init__(self, nome: str, pokemon: Pokemon, batalha_service: BatalhaService):
        self.nome = nome
        self.pokemon = pokemon
        self.batalha_service = batalha_service  # Injeção da dependência

    def desafiar(self, outro_treinador):
        print(f"{self.nome} desafia {outro_treinador.nome} para uma batalha!")
        vencedor = self.batalha_service.comecar_batalha(self.pokemon, outro_treinador.pokemon)
        return vencedor