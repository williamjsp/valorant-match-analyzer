<div align="center">
<img src="https://media.valorant-api.com/agents/eb93336a-449b-9c1e-0ac7-dfe9992400c5/displayicon.png" width="80" alt="Valorant Agent Icon"/>
🎯 valorant-match-analyzer
Ferramenta de análise de performance para jogadores de Valorant  
Dados reais de partidas. Insights que o jogo não te mostra.
![Status](https://github.com/williamjohnsonsz/valorant-match-analyzer)
![Python](https://python.org)
![API](https://docs.henrikdev.xyz)
![License](LICENSE)
</div>
---
📌 Sobre o projeto
Jogo Valorant competitivamente — já fui 2x vice-campeão em Maceió e estou me preparando para o Campeonato da FCN.
Durante os treinos, percebi que tomava decisões baseadas em feeling, não em dados. Quais mapas eu perco mais? Em quais agentes meu K/D cai? Quando eu erro mais headshots?
O `valorant-match-analyzer` responde essas perguntas automaticamente, buscando seus dados reais via API e gerando um relatório completo de performance.
> "O que não é medido, não pode ser melhorado." — aplicado ao Valorant.
---
✨ Funcionalidades
📊 K/D ratio por partida, agente e mapa
🎯 Headshot % — onde você está errando a mira
🗺️ Mapas mais fortes e mais fracos com taxa de vitória
🧑‍🤝‍🧑 Agentes mais jogados e performance por agente
📈 Evolução de performance ao longo do tempo
🔍 Comparativo entre sessões de treino
---
🛠️ Stack
Tecnologia	Uso
Python 3.11+	Linguagem principal
Henrik Dev API	Dados de partidas do Valorant
Pandas	Manipulação e análise de dados
Matplotlib / Plotly	Visualização dos resultados
Requests	Consumo da API REST
---
🚀 Como rodar
> ⚠️ Em desenvolvimento — instruções serão atualizadas conforme o projeto avança.
```bash
# Clone o repositório
git clone https://github.com/williamjohnsonsz/valorant-match-analyzer.git
cd valorant-match-analyzer

# Instale as dependências
pip install -r requirements.txt

# Configure sua API key
cp .env.example .env
# Edite o .env com seu HENRIK\_API\_KEY

# Execute a análise
python main.py --player "williamjohnsonsz#BR1"
```
---
📂 Estrutura do projeto
```
valorant-match-analyzer/
├── src/
│   ├── api/          # Integração com Henrik API
│   ├── analysis/     # Lógica de análise de dados
│   └── reports/      # Geração de relatórios e gráficos
├── data/             # Dados brutos e processados
├── tests/            # Testes unitários
├── main.py           # Ponto de entrada
├── requirements.txt
└── README.md
```
---
📊 Exemplo de output
```
📋 RELATÓRIO DE PERFORMANCE — williamjohnsonsz
══════════════════════════════════════════════

🏆 Últimas 20 partidas
   K/D Ratio:       1.42
   Headshot %:      28.3%
   Taxa de vitória: 55%

🗺️  Melhores mapas
   1. Ascent    →  70% vitória  |  K/D 1.8
   2. Bind      →  60% vitória  |  K/D 1.5
   3. Haven     →  55% vitória  |  K/D 1.3

🎭 Agentes mais jogados
   1. Reyna   →  12 partidas  |  K/D 1.9
   2. Phoenix →   5 partidas  |  K/D 1.2
   3. Breach  →   3 partidas  |  K/D 0.9

⚠️  Pontos de atenção
   - Headshot % abaixo de 30% — trabalhe mira em aim trainer
   - Haven com K/D < 1.0 nos últimos 7 dias
```
---
🗺️ Roadmap
[x] Estrutura inicial do projeto
[x] README e documentação base
[ ] Integração com Henrik API
[ ] Parser de dados de partidas
[ ] Geração de relatório no terminal
[ ] Dashboard visual com Plotly
[ ] Comparativo entre sessões de treino
[ ] Export para PDF / HTML
[ ] Suporte a múltiplos jogadores (análise de time)
---
🤝 Contexto competitivo
Este projeto nasce de uma necessidade real: usar dados para melhorar performance no Valorant competitivo.
Atualmente estou em preparação para o Campeonato FCN 2025 — patrocinado pela Riot Games, representando Maceió, AL. O analisador é uma das ferramentas que pretendo usar durante a preparação do time.
---
👨‍💻 Autor
William Johnson  
Back-end Developer | Dados & IA | Competidor de Valorant
![LinkedIn](https://linkedin.com/in/williamjohnsonsz)
![Instagram](https://instagram.com/williamjohnsonsz)
![GitHub](https://github.com/williamjohnsonsz)
---
📄 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
---
<div align="center">
  <sub>Feito com dados, café e muitas partidas de Valorant ☕🎮</sub>
</div>
