<div align="center">

<img src="assets/banner.png" width="100%" alt="Valorant Match Analyzer Banner"/>

# 🎯 valorant-match-analyzer

**Ferramenta de análise de performance para jogadores de Valorant**  
Transformando dados de partidas em métricas, análises e insights de performance.

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square)](https://github.com/williamjsp/valorant-match-analyzer)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 📌 Sobre o projeto

Jogo Valorant competitivamente — já fui **2x vice-campeão em Maceió** e estou me preparando para o **Campeonato FCN**.

Durante os treinos, percebi que tomava decisões baseadas em feeling, não em dados. Quais mapas eu perco mais? Em quais agentes meu K/D cai? Quando eu erro mais headshots?

O `valorant-match-analyzer` está sendo desenvolvido para transformar dados de partidas em métricas e insights de performance, permitindo identificar padrões relacionados a mapas, agentes, desempenho individual e evolução ao longo do tempo.

Neste estágio inicial, o projeto utiliza dados simulados de partidas (`fixtures`) para desenvolver e testar a arquitetura sem depender de integrações externas. A integração com a API oficial de VALORANT está planejada para uma etapa futura.

> "O que não é medido, não pode ser melhorado." — aplicado ao Valorant.

---

## ✨ Funcionalidades

- 📊 **K/D ratio** por partida, agente e mapa
- 🎯 **Headshot %** — onde você está errando a mira
- 🗺️ **Mapas mais fortes e mais fracos** com taxa de vitória
- 🧑‍🤝‍🧑 **Agentes mais jogados** e performance por agente
- 📈 **Evolução de performance** ao longo do tempo
- 🔍 **Comparativo entre sessões** de treino

---

## 🛠️ Tecnologias

| Tecnologia | Uso no projeto | Status |
|---|---|---|
| Python 3.11+ | Linguagem principal | ✅ Em uso |
| FastAPI | Construção da API e dos endpoints da aplicação | 🚧 Em implementação |
| Pydantic | Validação e definição dos schemas de entrada e saída | 🗺️ Planejado |
| SQLAlchemy | ORM e camada de persistência da aplicação | 🗺️ Planejado |
| SQLite | Banco de dados utilizado na fase inicial de desenvolvimento | 🗺️ Planejado |
| Prometheus | Coleta e exposição de métricas da aplicação | 🗺️ Planejado |
| Grafana | Visualização e monitoramento das métricas | 🗺️ Planejado |
| Docker / Docker Compose | Execução e organização dos serviços da aplicação | 🗺️ Planejado |
| pytest | Testes automatizados da aplicação | 🗺️ Planejado |
| pandas | Processamento e transformação de dados de partidas | 🗺️ Evolução futura |
| PostgreSQL | Banco de dados para evolução da persistência e deploy | 🗺️ Evolução futura |
| scikit-learn | Modelos de Machine Learning e previsão de performance | 🗺️ Evolução futura |

---

### 📡 Fonte de dados

Atualmente, o projeto utiliza dados simulados de partidas (`fixtures`) durante o desenvolvimento.

A arquitetura está sendo preparada para permitir a substituição dessa fonte de dados pela API oficial de VALORANT em uma etapa futura, sem exigir alterações significativas nas demais camadas da aplicação.

---
## 🚀 Como rodar

> ⚠️ O projeto está em estágio inicial de desenvolvimento. As instruções de execução serão atualizadas conforme as primeiras funcionalidades forem implementadas.

```bash
# Clone o repositório
git clone https://github.com/williamjsp/valorant-match-analyzer.git

# Entre no diretório
cd valorant-match-analyzer
```
---
## 📂 Estrutura do projeto

```
valorant-match-analyzer/
│
├── app/
│   ├── main.py
│   ├── routers/          # Endpoints e rotas da API
│   ├── services/         # Regras e lógica da aplicação
│   ├── repositories/     # Acesso e persistência de dados
│   ├── schemas/          # Schemas de entrada e saída com Pydantic
│   ├── models/           # Modelos de persistência com SQLAlchemy
│   └── mappers/          # Transformação entre diferentes formatos de dados
│
├── data/
│   └── fixtures/         # Dados simulados de partidas para desenvolvimento
│
├── tests/                # Testes automatizados
├── requirements.txt      # Dependências do projeto
└── README.md
```

---

## 📊 Exemplo de output

```
📋 RELATÓRIO DE PERFORMANCE — williamjohnson
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

## 🗺️ Roadmap

### Core da aplicação
- [x] Definição da proposta do projeto
- [x] Planejamento da arquitetura inicial
- [x] Documentação base
- [ ] Estrutura inicial com FastAPI
- [ ] Endpoint de health check
- [ ] Schemas de entrada e saída com Pydantic
- [ ] CRUD de partidas
- [ ] Camada de serviços
- [ ] Repository pattern
- [ ] Persistência com SQLAlchemy
- [ ] Banco de dados SQLite
- [ ] Tratamento de exceções

### Observabilidade
- [ ] Instrumentação da aplicação
- [ ] Exposição de métricas
- [ ] Integração com Prometheus
- [ ] Métricas de requisição, erros e tempo de resposta
- [ ] Métricas customizadas relacionadas ao processamento de partidas
- [ ] Integração com Grafana
- [ ] Dashboard de monitoramento da aplicação
- [ ] Containerização dos serviços com Docker Compose

### Pipeline de dados
- [ ] Estrutura de ingestão de partidas
- [ ] Transformação e limpeza de dados com pandas
- [ ] Mapeamento dos dados para o modelo interno da aplicação
- [ ] Validação e qualidade dos dados
- [ ] Armazenamento de histórico de partidas
- [ ] Migração da persistência para PostgreSQL

### Machine Learning
- [ ] Construção do dataset
- [ ] Feature engineering
- [ ] Criação de modelo baseline
- [ ] Treinamento com scikit-learn
- [ ] Avaliação e comparação de modelos
- [ ] Endpoint para previsões
- [ ] Registro de previsão versus resultado real
- [ ] Monitoramento das métricas do modelo

### Integração com VALORANT
- [ ] Adapter para fontes externas de dados
- [ ] Integração com a API oficial de VALORANT
- [ ] Autorização do jogador
- [ ] Coleta automática de partidas
- [ ] Substituição das fixtures por dados reais

### Evolução do produto
- [ ] Análise de performance por mapa
- [ ] Análise de performance por agente
- [ ] Evolução de desempenho ao longo do tempo
- [ ] Comparação entre sessões
- [ ] Geração de insights de performance
- [ ] Análise de múltiplos jogadores
- [ ] Análise de equipes

---

## 🤝 Contexto competitivo

Este projeto nasce de uma necessidade real: **usar dados para melhorar performance no Valorant competitivo**.

Atualmente estou em preparação para o **Campeonato FCN 2026**. O analisador é uma das ferramentas que pretendo usar durante a preparação do time.

---

## 👨‍💻 Autor

**William Johnson**  
Back-end Developer | Dados & IA | Competidor de Valorant

[![LinkedIn](https://img.shields.io/badge/LinkedIn-williamjohnson--dev-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/williamjohnson-dev)
[![Instagram](https://img.shields.io/badge/Instagram-@williamjohnsonsz-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com/williamjohnsonsz)
[![GitHub](https://img.shields.io/badge/GitHub-williamjsp-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/williamjsp)

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.

---

<div align="center">
  <sub>Feito com dados, café e muitas partidas de Valorant ☕🎮</sub>
</div>
