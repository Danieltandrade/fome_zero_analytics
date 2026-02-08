# 🍽️ Fome Zero Analytics

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://daniel-fome-zero-analytics.streamlit.app/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Data_Science-blue)](https://github.com/DanielTorresAndrade)

Este é um projeto end-to-end de Ciência de Dados desenvolvido para auxiliar o CEO da **Fome Zero** na tomada de decisões estratégicas baseadas em dados.

---

## 1. Problema de Negócio

A **Fome Zero** é uma marketplace de restaurantes que conecta clientes a estabelecimentos gastronômicos. A empresa captura dados diversos, como localização, tipos de culinária, avaliações, reservas e entregas.

O recém-contratado CEO, **Kleiton Guerra**, precisa entender profundamente o ecossistema da empresa para alavancar o crescimento. O objetivo deste projeto é entregar um **Painel Gerencial (Dashboard)** que responda às principais perguntas de negócio e permita a exploração interativa dos dados.

<details>
  <summary><strong>📋 Clique aqui para ver as Perguntas de Negócio respondidas neste projeto</strong></summary>

  ### Geral
  1. Quantos restaurantes únicos estão registrados?
  2. Quantos países únicos estão registrados?
  3. Quantas cidades únicas estão registradas?
  4. Qual o total de avaliações feitas?
  5. Qual o total de tipos de culinária registrados?

  ### Países
  1. Qual o nome do país que possui mais cidades registradas?
  2. Qual o nome do país que possui mais restaurantes registrados?
  3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
  4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
  5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
  6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
  7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
  8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
  9. Qual o nome do país que possui, na média, a maior nota média registrada?
  10. Qual o nome do país que possui, na média, a menor nota média registrada?
  11. Qual a média de preço de um prato para dois por país?

  ### Cidades
  1. Qual o nome da cidade que possui mais restaurantes registrados?
  2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
  3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
  4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
  5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
  6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
  7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
  8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

  ### Restaurantes
  1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
  2. Qual o nome do restaurante com a maior nota média?
  3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
  4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
  5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
  6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
  7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
  8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

  ### Culinárias
  1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
  2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
  3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
  4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
  5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
  6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
  7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
  8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
  9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
  10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
  11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
  12. Qual o tipo de culinária que possui a maior nota média?
  13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?
</details>

## 2. Premissas do Negócio

- **Fonte de Dados:** Dataset público [Zomato Restaurants](https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?select=zomato.csv) (Kaggle).
- **Modelo de Negócio:** Marketplace (Intermediação entre clientes e restaurantes).
- **Estrutura de Análise:** O painel foi dividido em 4 visões estratégicas para facilitar a navegação e o foco da análise.

## 3. Estratégia da Solução

O painel foi desenvolvido utilizando a metodologia cíclica de desenvolvimento de software, focando em entregar valor rápido para o usuário final. As métricas foram organizadas nas seguintes visões:

| Visão | Descrição das Métricas Principais |
| :--- | :--- |
| **🌎 Geral** | Visão macro: Total de restaurantes, países, cidades, avaliações e mapa de geolocalização. |
| **🇺🇳 Países** | Comparativo entre nações: Quantidade de restaurantes, média de avaliações e custo médio prato para dois. |
| **🏙️ Cidades** | Top Cidades com mais restaurantes, melhores/piores notas médias e diversidade culinária. |
| **🥘 Culinárias** | Análise de nicho: Melhores restaurantes por tipo de cozinha e rankings de categorias. |

## 4. Top 3 Insights de Dados

Durante a análise exploratória, destacaram-se os seguintes pontos:

1.  **Dominância e Custo na Índia:** A Índia possui a maior quantidade de restaurantes cadastrados, mas também apresenta o 3º maior custo médio para dois (ajustado pela moeda), indicando um mercado volumoso e de alto valor agregado.
2.  **Performance Brasileira:** As três únicas cidades brasileiras presentes (Brasília, São Paulo e Rio de Janeiro) figuram no Top 10 cidades com **piores médias de avaliação**. Isso sugere uma oportunidade de melhoria na qualidade do serviço ou na gestão de expectativas dos clientes locais.
3.  **Paradoxo das Culinárias:** Culinárias tradicionais orientais (Japonesa, etc.) tendem a ter notas consistentemente altas, enquanto categorias de nicho específico (apenas bebidas, culinária mineira, afegan) apresentam médias inferiores.

## 5. O Produto Final

O resultado é um painel interativo hospedado na nuvem, acessível de qualquer dispositivo.

[![Acessar Dashboard](https://img.shields.io/badge/Acessar_Dashboard-Fome_Zero-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://daniel-fome-zero-analytics.streamlit.app/)

## 6. Conclusão

O projeto atingiu seu objetivo de transformar dados brutos em informação acionável. Através dos filtros de países e tipos de culinárias, o CEO agora possui uma ferramenta para segmentar o mercado e identificar micro-tendências que antes estavam ocultas nos dados.

Com este dados, o CEO pode tomar melhores decisões de investir em restaurantes com potencial de crescimento, aumentando assim a eficiência financeira e o crescimento do negócio.

## 7. Próximos Passos

1.  **Novos Filtros:** Adicionar filtros por faixa de preço e disponibilidade de reserva online.
2.  **Análise Temporal:** Se houver dados históricos, implementar análise de tendências ao longo do tempo.
3.  **Otimização do Mapa:** Implementar clusterização mais eficiente para melhorar a performance de renderização em dispositivos móveis.
4.  **UX/UI:** Refinar o layout para uma experiência de usuário ainda mais fluida.
5.  **Melhoria da Documentação:** Melhorar a documentação para tornar o processo de desenvolvimento mais claro e intuitivo.

---

## 8. 🛠️ Documentação Técnica & Instalação

Para detalhes técnicos sobre a estrutura de arquivos, instalação de dependências, como executar o projeto na sua máquina local ou informações sobre as tecnologias utilizadas (Python, Streamlit, Plotly, UV), consulte o arquivo de documentação dedicado:

[![Ver Documentação Técnica](https://img.shields.io/badge/📖_Ler-PROJECT.md-1f425f?style=for-the-badge)](./PROJECT.md)

---