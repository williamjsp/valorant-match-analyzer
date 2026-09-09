<div align="center">

<img src="assets/banner.png" width="100%" alt="Valorant Match Analyzer Banner"/>

# 🎯 valorant-match-analyzer

**Aplicação para análise de performance em partidas competitivas**

Transformando dados de partidas em métricas, análises e insights de desempenho através de uma aplicação backend estruturada com boas práticas de Engenharia de Software.

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square)](https://github.com/williamjsp/valorant-match-analyzer)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 📌 Sobre o projeto

O `valorant-match-analyzer` é uma aplicação desenvolvida para registrar, organizar e analisar dados de desempenho de jogadores em partidas competitivas.

O projeto tem como objetivo transformar dados de partidas em métricas e insights de performance, permitindo identificar padrões relacionados a mapas, agentes, desempenho individual e evolução ao longo do tempo.

A aplicação está sendo desenvolvida aplicando conceitos de Engenharia de Software, como arquitetura em camadas, desenvolvimento de APIs REST, persistência de dados e observabilidade.

---
## 💡 Motivação

Durante minha trajetória competitiva no Valorant, percebi que muitas decisões eram tomadas com base em percepção, e não em dados.

Surgiram questionamentos como:

- Em quais mapas tenho melhor desempenho?
- Quais agentes apresentam melhores resultados?
- Como minha performance evolui ao longo do tempo?
- Quais pontos preciso melhorar?

A partir dessa necessidade surgiu a ideia de desenvolver uma ferramenta capaz de transformar dados de partidas em informações úteis para análise e tomada de decisão.

> "Performance sem contexto é só número."

---
## ✨ Funcionalidades

### ✅ Implementadas

- API REST para gerenciamento de performances;
- Criação de registros de performance;
- Consulta de performances;
- Busca por identificador;
- Atualização de performances;
- Remoção de performances;
- Validação de dados com Pydantic;
- Persistência utilizando SQLAlchemy + SQLite;
- Tratamento de exceções;
- Controle de transações no acesso ao banco;
- Instrumentação da aplicação com métricas utilizando Prometheus.
- Dashboard de acompanhamento utilizando Grafana

### 🚧 Planejadas

- Análise de K/D por partida, agente e mapa;
- Identificação de padrões de desempenho;
- Comparação entre sessões de treino;
- Geração de insights;
- Modelos de Machine Learning.

---

## 🛠️ Tecnologias

| Tecnologia | Uso no projeto | Status |
|---|---|---|
| Python 3.11+ | Linguagem principal | ✅ Em uso |
| FastAPI | Construção da API e dos endpoints da aplicação | ✅ Em uso |
| Pydantic | Validação e definição dos schemas de entrada e saída | ✅ Em uso |
| SQLAlchemy | ORM e camada de persistência da aplicação | ✅ Em uso |
| SQLite | Banco de dados utilizado na fase inicial de desenvolvimento | ✅ Em uso |
| Prometheus | Coleta, armazenamento e consulta de métricas da aplicação | ✅ Em uso |
| Grafana | Construção de dashboards para visualização das métricas | ✅ Em uso |
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

```bash
# Clone o repositório
git clone https://github.com/williamjsp/valorant-match-analyzer.git

# Entre no diretório
cd valorant-match-analyzer

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
uvicorn app.main:app --reload

# Documentação Swagger:
http://localhost:8000/docs

# Métricas Prometheus:
http://localhost:8000/metrics
```
---
## 🏗️ Arquitetura

A aplicação segue uma arquitetura organizada em camadas, buscando separar responsabilidades e facilitar a evolução do sistema.

Fluxo da aplicação:

```text
Cliente
  |
  | Requisição HTTP
  ↓
Router
  |
  | Encaminha a operação
  ↓
Service
  |
  | Aplica regras de negócio
  ↓
Repository
  |
  | Acesso aos dados
  ↓
Database
```

### Camadas

**Router**
- Responsável pelos endpoints HTTP;
- Recebe requisições e retorna respostas.

**Service**
- Contém regras de negócio;
- Coordena o fluxo da aplicação.

**Repository**
- Responsável pela comunicação com o banco de dados.

**Schemas**
- Validação dos dados utilizando Pydantic.

**Models**
- Representação das entidades persistidas utilizando SQLAlchemy.

**Mappers**
- Conversão entre diferentes formatos de dados.

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

## 📊 Visão do resultado esperado

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

⚠️ Pontos de atenção
   - Queda de desempenho em Haven nas últimas partidas
   - Taxa de vitória inferior à média ao jogar de Omen
   - Maior número de mortes nas primeiras rodadas das partidas
```

---

## 🗺️ Roadmap

### Core da aplicação
- [x] Definição da proposta do projeto
- [x] Planejamento da arquitetura inicial
- [x] Estrutura inicial com FastAPI
- [x] Endpoint de health check
- [x] Schemas de entrada e saída com Pydantic
- [x] CRUD de performances
- [x] Camada de serviços
- [x] Repository pattern
- [x] Persistência com SQLAlchemy
- [x] Banco de dados SQLite
- [x] Tratamento de exceções
- [x] Controle de transações 

### Observabilidade
- [x] Instrumentação da aplicação
- [x] Exposição de métricas
- [x] Integração com Prometheus
- [x] Métricas de requisição, erros e tempo de resposta
- [x] Métrica customizada de performances criadas
- [x] Integração com Grafana
- [x] Dashboard de monitoramento da aplicação
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

O projeto nasce da minha experiência como jogador competitivo de VALORANT e da necessidade de transformar dados de partidas em informações mais úteis para tomada de decisão e evolução de performance.

Já conquistei dois vice-campeonatos em competições locais em Maceió e sigo me preparando para novos campeonatos, utilizando o desenvolvimento do `valorant-match-analyzer` também como uma forma de conectar tecnologia, análise de dados e cenário competitivo.

---

## 👨‍💻 Autor

**William Johnson**  
Back-end Developer | Python | Dados & IA | Competidor de Valorant

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
