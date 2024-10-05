from Pokemon import Pokemon

# Serviço, que gerencia Batalhas de Pokémon
class BatalhaService:
    def comecar_batalha(self, pokemon1: Pokemon, pokemon2: Pokemon):
        print(f"{pokemon1.nome} está batalhando contra {pokemon2.nome}!")
        
        # Simulação simples de batalha
        pokemon_vencedor = pokemon1 if pokemon1.nivel >= pokemon2.nivel else pokemon2
        print(f"O vencedor é {pokemon_vencedor.nome}!")