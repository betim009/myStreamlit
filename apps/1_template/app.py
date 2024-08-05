import streamlit as st  # Importa a biblioteca Streamlit

# Configurações iniciais do Streamlit
# Define o título da página e o layout como "wide" (amplo)
st.set_page_config(page_title='Meu Aplicativo Streamlit', layout='wide')


def main():
    # Título do aplicativo
    st.title('Meu Aplicativo Streamlit')
    st.write('Bem-vindo ao meu aplicativo Streamlit!')  # Mensagem de boas-vindas

    # Barra lateral para navegação
    st.sidebar.title('Navegação')  # Título da barra lateral
    # Cria um selectbox na barra lateral com as opções "Home", "Página 1" e "Página 2"
    option = st.sidebar.selectbox(
        'Selecione a página', ['Home', 'Página 1', 'Página 2']
    )

    # Página Home
    if option == 'Home':
        st.header('Home')  # Cabeçalho da página
        st.write(
            'Esta é a página inicial do seu aplicativo.'
        )  # Conteúdo da página Home

    # Página 1
    elif option == 'Página 1':
        st.header('Página 1')  # Cabeçalho da página
        st.write('Conteúdo da Página 1.')  # Conteúdo da Página 1

    # Página 2
    elif option == 'Página 2':
        st.header('Página 2')  # Cabeçalho da página
        st.write('Conteúdo da Página 2.')  # Conteúdo da Página 2


# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    main()  # Chama a função principal para executar o aplicativo
