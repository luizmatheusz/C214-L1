from BatalhaService import BatalhaService
from Pokemon import Pokemon
from Treinador import Treinador

# Instanciando o serviço de batalha
batalha_service = BatalhaService()

# Criando dois pokémon, dois treinadores e injetando o serviço de batalha
pokemon_ash = Pokemon(nome="Pikachu", tipo="Eletrico", nivel=100)
ash = Treinador(nome="Ash", pokemon=pokemon_ash, batalha_service=batalha_service)
pokemon_gary = Pokemon(nome="Blastoise", tipo="Agua", nivel=92)
gary = Treinador(nome="Gary", pokemon=pokemon_gary, batalha_service=batalha_service)

# Iniciando uma batalha entre os treinadores
ash.desafiar(gary)