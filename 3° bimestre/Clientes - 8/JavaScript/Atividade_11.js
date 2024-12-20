function fetchPokemonList() {
    fetch('https://pokeapi.co/api/v2/pokemon?limit=20')
        .then(response => response.json())
        .then(data => {
            const pokemonList = document.getElementById('pokemon-list');
            data.results.forEach((pokemon, index) => {
                const pokemonItem = document.createElement('div');
                pokemonItem.classList.add('pokemon-item');
                pokemonItem.textContent = pokemon.name;
                pokemonItem.setAttribute('data-url', pokemon.url);

                
                pokemonItem.addEventListener('click', () => {
                    fetchPokemonDetails(pokemon.url);
                });

                pokemonList.appendChild(pokemonItem);
            });
        })
        .catch(error => console.error('Erro ao buscar Pokémon:', error));
}

function fetchPokemonDetails(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const pokemonDetails = document.getElementById('pokemon-details');
            pokemonDetails.innerHTML = `
                <h2>${data.name}</h2>
                <p><strong>Altura:</strong> ${data.height}</p>
                <p><strong>Peso:</strong> ${data.weight}</p>
                <p><strong>Tipos:</strong> ${data.types.map(type => type.type.name).join(', ')}</p>
                <h3>Habilidades</h3>
                <ul>
                    ${data.abilities.map(ability => `<li>${ability.ability.name}</li>`).join('')}
                </ul>
                <h3>Movimentos</h3>
                <ul>
                    ${data.moves.slice(0, 5).map(move => `<li>${move.move.name}</li>`).join('')}
                </ul>
            `;
        })
        .catch(error => console.error('Erro ao buscar detalhes do Pokémon:', error));
}

document.addEventListener('DOMContentLoaded', fetchPokemonList);
