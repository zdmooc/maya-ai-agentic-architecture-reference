# D-099 AA3 — Premier design réel `NOTIFY-01` : réussite JSON, revue de fond réservée

**Source : transcription fidèle de la sortie opérateur HP du 9 octobre 2026**
`evals/observed/aa3_operator_design_notify_2026-10-09.json`, modèle
`qwen3.5:9b-q4_K_M`, fenêtre demandée 8 192 tokens. Ce fichier n'est
**ni** une télémétrie indépendante, **ni** une preuve signée.

## Résultat effectivement obtenu

- `AA3_LOCAL_DESIGN_SLICE_PASS`, `violations=[]` ;
  trois options S1/S2/S3 ; ADR `PROPOSED` orienté vers S2
- 525 tokens de prompt, 530 tokens générés, 296,91 s total,
  chargement 28,01 s ; RAM disponible après 24,15 Gio.
- `ollama ps` vide après la requête ; pas de preuve de
  contexte ou consommation du modèle en charge à cet instant.
- `full_aa0_assessment_schema_validated=false`,
  `source_semantic_entailment_reviewed=false`,
  `human_architecture_score=NOT_SCORED`, `adr_approved=false`.

## Revue préliminaire du contenu — NON indépendante

| Élément | Avis motivé |
|---|---|
| S1 | **Écart majeur** : présente une DLQ proposée « for unbounded retries », contraire à la livraison asynchrone bornée exigée par N2. La section risque reconnaît la violation ; l'option n'est donc pas viable sans reprise. |
| S2 | **Orientation plausible mais à instruire** : déduplication et événements de statut documentés par N2 ; cap de retry et gestion d'échec **à concevoir et tester**, pas déployés. Absence de mesure RTO/performance. |
| S3 | **Écart majeur de différenciation** : ajoute surtout un test de révocation du consentement, validation utile, mais pas une architecture de livraison complète répondant seule à la résilience/traçabilité. |
| ADR | `PROPOSED` et `approval_ref=null` corrects. Choisir S2 automatiquement pour exécuter un build serait prématuré ; arbitrage indépendant nécessaire. |

Le succès technique du schéma **n'équivaut pas** à une revue
sémantique, à la validation de toutes les contraintes par chaque
solution, ou au score humain >=85/100 requis pour AA3.

Le prompt `local_aa3_design_probe.py` précise désormais que
**chacune des trois options** doit répondre aux exigences non
négociables. Pour INVENTORY-02 : expiration/libération de réservation,
idempotence, journal cohérent, aucun mécanisme fictivement déployé.
Ces formulations améliorent la consigne mais ne garantissent pas
la correction du texte libre. Aucune deuxième inférence n'a été
lancée par GitHub ou CI.

**Suite opérateur** : fast-forward vérifié du hub,
puis un seul test `--case inventory_case.json` sur Ollama
8K local ; faire une vraie revue des options et de l'ADR proposé.
D099 et AA3 restent ouverts. D-093 et l'autre session inchangés.
