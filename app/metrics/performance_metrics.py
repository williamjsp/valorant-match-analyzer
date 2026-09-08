from prometheus_client import Counter

performances_creations_total = Counter(
    "valorant_performances_creations_total",
    "Total de Performances Criadas",
)
