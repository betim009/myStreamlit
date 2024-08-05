import streamlit as st
from data import pokemons


# Função principal do aplicativo Streamlit
# Função principal do aplicativo Streamlit
def main():
    st.title("Pokédex Streamlit")
    st.write("Bem-vindo à Pokédex!")

    # Definindo o número de colunas
    num_columns = 3
    columns = st.columns(num_columns)

    # Adicionando os pokémons nas colunas
    for index, pokemon in enumerate(pokemons):
        col = columns[index % num_columns]
        with col:
            st.image(pokemon["url"], caption=pokemon["name"])
            st.write(f"**Número:** {pokemon['number']}")
            st.write(f"**Nome:** {pokemon['name']}")
            st.write(f"**Tipos:** {', '.join(pokemon['type'])}")


if __name__ == "__main__":
    main()