import streamlit as st
import speedtest

def main():
    st.header("SpeedTest", divider=True)
    st.write("Clique no botão abaixo para iniciar o teste.")
    
    if st.button("Iniciar"):
        with st.spinner("Testando a velocidade da sua internet..."):
            # Inicializando o Speedtest
            s = speedtest.Speedtest()
            s.get_best_server()  # Busca o melhor servidor

            # Testando as velocidades
            download_speed = s.download() / 1_000_000  # Converte para Mbps
            upload_speed = s.upload() / 1_000_000      # Converte para Mbps

            # Obtendo o ping e outros dados do teste
            results = s.results.dict()
            max_speed = 100  # Máxima velocidade esperada (para normalizar a barra de progresso)

            # Exibindo resultados
            st.write(f"Velocidade de Download: {download_speed:.2f} Mbps")
            st.progress(min(download_speed / max_speed, 1.0))  # Barra de progresso limitada a 1.0

            st.write(f"Velocidade de Upload: {upload_speed:.2f} Mbps")
            st.progress(min(upload_speed / max_speed, 1.0))  # Barra de progresso limitada a 1.0

            st.write(f"Ping: {results['ping']} ms")

# Executa o programa principal
if __name__ == "__main__":
    main()
