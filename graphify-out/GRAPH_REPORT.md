# Graph Report - cs473-fml  (2026-05-01)

## Corpus Check
- 144 files · ~220,334 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1661 nodes · 2998 edges · 55 communities detected
- Extraction: 62% EXTRACTED · 38% INFERRED · 0% AMBIGUOUS · INFERRED: 1128 edges (avg confidence: 0.74)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]

## God Nodes (most connected - your core abstractions)
1. `SurvivalModelBundle` - 66 edges
2. `DatasetSpec` - 59 edges
3. `TrajectoryClusteringModel` - 49 edges
4. `LearnedScoringModel` - 42 edges
5. `build_zone_year_matrix()` - 31 edges
6. `transform()` - 29 edges
7. `run_etl()` - 26 edges
8. `Halal pipeline package.` - 25 edges
9. `TemporalSplit` - 25 edges
10. `RecommendationRequest` - 22 edges

## Surprising Connections (you probably didn't know these)
- `build_zone_year_matrix()` --calls--> `test_build_zone_year_matrix_accepts_311_for_social_buzz()`  [INFERRED]
  src/features/feature_matrix.py → tests/test_nlp.py
- `build_demand()` --calls--> `test_mn22_latent_gt_revealed()`  [INFERRED]
  src/halal_demand.py → tests/test_halal_demand.py
- `build_demand()` --calls--> `main()`  [INFERRED]
  src/halal_demand.py → scripts/run_phase1.py
- `build_entry_forecast()` --calls--> `test_build_entry_forecast_logic()`  [INFERRED]
  src/halal_forecast.py → tests/test_halal_forecast.py
- `build_viability()` --calls--> `test_build_viability_columns()`  [INFERRED]
  src/halal_risk.py → tests/test_halal_risk.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (259): build_default_audit_rows(), Default audit rows for the active data sources., Return one audit row per registered dataset., BaseDatasetPipeline, build_empty_frame(), DatasetSpec, Shared base classes for dataset placeholders., Minimal source metadata for dataset-specific workstreams. (+251 more)

### Community 1 - "Community 1"
Cohesion: 0.02
Nodes (192): BaselineRun, build_baseline_runs(), Shared baseline bundles for placeholder experimentation., A lightweight record describing an experiment slot., Return the initial model workstreams for the team., LearnedScoringModel, XGBoost-based zone attractiveness scorer., Train XGBoost regressor on feature matrix with composite outcome.          Param (+184 more)

### Community 2 - "Community 2"
Cohesion: 0.01
Nodes (203): compute_competition_score(), Competition scoring for healthy-food concepts., Score competitive pressure in a zone (higher = more competition).      Weights:, build_demand_features(), compute_healthy_review_share(), Demand-feature builders from reviews and social signals., Merge review and social signals into demand features.      Parameters     ------, Compute the fraction of reviews that mention any healthy keyword.      Parameter (+195 more)

### Community 3 - "Community 3"
Cohesion: 0.02
Nodes (160): cluster_embeddings(), cluster_stability(), compute_zone_embedding_features(), embed_reviews(), EmbeddingConfig, optimal_k_search(), Sentence-transformer embeddings for review text., Find optimal k for K-means via silhouette score.      Returns (best_k, {k: silho (+152 more)

### Community 4 - "Community 4"
Cohesion: 0.03
Nodes (109): baseline_comparison(), feature_ablation(), _heuristic_scores(), _learned_predict(), permutation_importance(), _popularity_scores(), Feature ablation and baseline comparison studies., Fit and predict with the learned model. (+101 more)

### Community 5 - "Community 5"
Cohesion: 0.03
Nodes (80): BaseModel, list_datasets(), Schemas for dataset metadata and audits., Expose the dataset audit inventory for frontend and QA work., health_check(), Health endpoints for local development., Return an enriched health payload with data and model stats., lifespan() (+72 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (74): A blocked train/test split over ordered time periods., TemporalSplit, _as_numeric_frame(), CausalMLConfig, compute_qini_coefficient(), compute_standardized_mean_differences(), compute_uplift_at_fraction(), compute_uplift_curve() (+66 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (42): Shared constants for the project., get_app_settings(), Shared API dependencies., Expose cached settings via FastAPI dependency injection., Halal pipeline package., ProjectPipeline, A lightweight orchestrator that documents the intended workflow., Track the ordered stages of the current scaffold. (+34 more)

### Community 8 - "Community 8"
Cohesion: 0.05
Nodes (55): filter_recommendations(), load_recommendations(), load_review_evidence_pool(), main(), Streamlit entrypoint — NYC Halal Restaurant Opportunity Finder., Yelp reviews with Gemini halal labels — used for qualitative evidence per NTA., _generate_narrative(), Comparison view — side-by-side neighborhood analysis. (+47 more)

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (34): build_entry_forecast(), build_forecast(), _load_yearly_nta_signals(), HalalKMeans, run_kmeans(), build_gap(), build_supply(), build_gmm_risk() (+26 more)

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (38): _cuisine_diversity_features(), main(), Enrich zone_features.parquet with NTA cuisine diversity and Yelp rating signals., Aggregate cuisine_type from inspections to NTA level.      Returns DataFrame wit, Aggregate Yelp ratings from already-zoned review data to NTA level.      yelp_re, _yelp_nta_features(), _load_phase1_results(), _load_phase2_results() (+30 more)

### Community 11 - "Community 11"
Cohesion: 0.09
Nodes (33): data/output/ — Derived CSVs powering Streamlit dashboards, data/processed/inspections.parquet — Per-inspection parquet with grades + nta_id, frontend/app.py — Primary Streamlit recommender UX, frontend/methodology_content.py — Narrative + metrics for investor slides, scripts/run_phase1.py — Elbow analysis, clustering exports, centroid tables, scripts/run_phase2.py — Risk viability merge, final_score + similarity rankings, scripts/run_phase3.py — Ridge forecasts, GMM risk, final CSV outputs, src/halal_forecast.py — Temporal ridge models for halal chatter + entry dynamics (+25 more)

### Community 12 - "Community 12"
Cohesion: 0.11
Nodes (20): test_resolve_nta_multi_zone_no_primary_falls_back_to_sorted(), Tests for NTA → micro-zone resolution., test_load_all_nta_codes_fallback(), test_resolve_ambiguous_nta_uses_primary(), test_resolve_single_nta_maps_to_one_zone(), test_resolve_unknown_nta_returns_none(), assign_yelp_business_zones(), Assign Yelp businesses to micro-zones (NYC NTA → zone_id). (+12 more)

### Community 13 - "Community 13"
Cohesion: 0.26
Nodes (12): build_census_features(), build_citibike_features(), build_hygiene_features(), build_yelp_features(), load_manhattan_ntas(), _load_ntas(), main(), Build NTA-level feature tables for Yelp, hygiene, census, and Citi Bike. (+4 more)

### Community 14 - "Community 14"
Cohesion: 0.17
Nodes (11): Shared fixtures for the test suite., Compact feature dict using current (2020-NTA) feature matrix column names., 20 rows of license events with required columns., 20 rows of PLUTO-style assessed-value data., 20 rows of Gemini-style labeled reviews with zone/time keys., 50 rows of test restaurant survival data., sample_license_events(), sample_pluto_frame() (+3 more)

### Community 15 - "Community 15"
Cohesion: 0.38
Nodes (8): build_demand(), build_latent_demand(), _load_raw_data(), _labels(), _reviews(), test_latent_demand_columns(), test_latent_demand_range(), test_mn22_latent_gt_revealed()

### Community 16 - "Community 16"
Cohesion: 0.39
Nodes (8): assess_columns(), build_log(), choose_sheet(), download_zip_bytes(), ensure_parent(), extract_member(), main(), Download and convert the selected NYC DCP ACS NTA dataset to CSV.

### Community 17 - "Community 17"
Cohesion: 0.52
Nodes (6): _api_key(), _business_ids(), _fetch_one(), fetch_reviews(), _load_repo_env(), main()

### Community 18 - "Community 18"
Cohesion: 0.29
Nodes (7): NYC Halal Opportunity Finder (Design Doc), NYC DOHMH CAMIS hygiene extracts — restaurant supply + cuisine source, data/processed/inspections.parquet — inspection-grade history aggregated to NTAs, Yelp review text + Gemini labels — demand signal source, NTA (Neighborhood Tabulation Area) — unit of analysis, Problem: halal restaurant location selection for NYC operators — information gap, Environment setup — Python 3.10+, venv, pip install -r requirements.txt

### Community 19 - "Community 19"
Cohesion: 0.33
Nodes (2): ModelConfig, test_custom_override()

### Community 20 - "Community 20"
Cohesion: 0.4
Nodes (1): Tests for frontend query resolution logic.

### Community 21 - "Community 21"
Cohesion: 0.6
Nodes (5): data/raw/gemini_labels_full.csv — Gemini halal relevance labels, data/raw/yelp_reviews_with_zones.csv — Review text with NTA + Gemini join keys, src/halal_demand.py — Gemini-labeled Yelp text → NTA demand_score features, Siqi Zhu (sz3950) — Gemini/Yelp ingestion + demand-signal QA, pandas>=2.0.0

### Community 22 - "Community 22"
Cohesion: 0.5
Nodes (3): minmax(), Shared utilities — math helpers and domain constants for the halal pipeline., Min-max normalize a Series to [0, 1]. Returns 0.0 if constant or all-null.

### Community 23 - "Community 23"
Cohesion: 0.67
Nodes (3): load_frame(), main(), Build the Phase 1 neighborhood finding dataset.

### Community 24 - "Community 24"
Cohesion: 0.5
Nodes (3): load_nyc_ntas_for_zones(), Load NTA boundary layers for spatial joins (Yelp → NTA → micro-zone_id)., Load **2020** NYC NTA polygons with ACS ``nta2020`` codes (MN0202, BK0202, …).

### Community 25 - "Community 25"
Cohesion: 0.5
Nodes (3): Integration tests for full pipeline., Verify build_feature_matrix_stage produces null-free output., test_build_feature_matrix_stage_returns_null_free_dataframe()

### Community 27 - "Community 27"
Cohesion: 0.83
Nodes (3): main(), _summary(), _validate()

### Community 28 - "Community 28"
Cohesion: 0.5
Nodes (3): Data freshness helpers for the frontend., Render per-source freshness with live availability status., render_data_freshness()

### Community 29 - "Community 29"
Cohesion: 0.67
Nodes (4): data/raw/restaurant_hygiene.csv — CAMIS universe with cuisine descriptors, scripts/check_camis_time.py — CAMIS timeline QA vs Yelp and parquet, src/halal_opportunity.py — CAMIS cuisines → halal supply rates, gaps, diversification, Harsh Agarwal (ha2957) — CAMIS supply metrics + reproducibility

### Community 30 - "Community 30"
Cohesion: 0.67
Nodes (1): Methodology content for the main Streamlit app.

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (1): Single source of truth for sidebar control keys and defaults.

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (1): Compute the overall weighted opening score.

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (1): Load model from joblib.

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (1): Load model from joblib.

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (1): Sanitize and validate concept_subtype.

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (1): Shared utilities — math helpers and domain constants for the halal pipeline.

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (1): Min-max normalize a Series to [0, 1]. Returns 0.0 if constant or all-null.

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (1): Radar chart: 5 opportunity dimensions, all on [0, 1].

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (1): Generate plain-English 2-sentence opportunity summary from signal values.

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (1): Return an HTML inline pill badge for the given market type.

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (1): Injects premium CSS for a standalone app feel with Islamic green + gold palette.

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (1): Render concept, price, and risk controls.  Supports any cuisine type.

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (1): Injects premium CSS for a standalone app feel with Islamic green + gold palette.

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (1): Rich analytics for Tab 3.

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (1): Rich analytics for Tab 3.

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (1): Compute Local Moran's I (LISA) for gap_score.          Args:         gap_df: Dat

### Community 59 - "Community 59"
Cohesion: 1.0
Nodes (1): Yelp reviews with Gemini halal labels — used for qualitative evidence per NTA.

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (1): Min-max normalize a Series to [0, 1]. Returns 0.0 if constant or all-null.

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (1): A K-Means implementation built from scratch using NumPy.     Supports K-Means++

### Community 62 - "Community 62"
Cohesion: 1.0
Nodes (1): K-Means++ initialization.

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (1): Assign each sample to the nearest centroid.

### Community 64 - "Community 64"
Cohesion: 1.0
Nodes (1): Transform X to a cluster-distance space.

### Community 65 - "Community 65"
Cohesion: 1.0
Nodes (1): Engine for computing composite demand scores.     Integrates Revealed Demand (Ye

### Community 66 - "Community 66"
Cohesion: 1.0
Nodes (1): build_halal_scores.py — Planned merge façade (currently dormant)

### Community 67 - "Community 67"
Cohesion: 1.0
Nodes (1): scipy>=1.10.0

## Knowledge Gaps
- **290 isolated node(s):** `Shared utilities — math helpers and domain constants for the halal pipeline.`, `Min-max normalize a Series to [0, 1]. Returns 0.0 if constant or all-null.`, `Parse NTA centroids from NTA boundaries CSV.          Parses WKT MULTIPOLYGON st`, `Compute Local Moran's I (LISA) for gap_score.          Args:         gap_df: Dat`, `Orchestrator that runs all ETL modules and returns their outputs.` (+285 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 19`** (6 nodes): `ModelConfig`, `config.py`, `test_custom_override()`, `test_defaults_sane()`, `test_immutable()`, `test_config.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (5 nodes): `Tests for frontend query resolution logic.`, `test_resolve_effective_search_settings_falls_back_without_description()`, `test_resolve_effective_search_settings_uses_nlp_values_when_enabled()`, `test_resolve_effective_search_settings_uses_selected_values_when_structured()`, `test_frontend_search_state.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (3 nodes): `methodology_content.py`, `Methodology content for the main Streamlit app.`, `render_methodology_page()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `Single source of truth for sidebar control keys and defaults.`, `_form_keys.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Compute the overall weighted opening score.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `Load model from joblib.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `Load model from joblib.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `Sanitize and validate concept_subtype.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `Shared utilities — math helpers and domain constants for the halal pipeline.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `Min-max normalize a Series to [0, 1]. Returns 0.0 if constant or all-null.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `Radar chart: 5 opportunity dimensions, all on [0, 1].`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `Generate plain-English 2-sentence opportunity summary from signal values.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `Return an HTML inline pill badge for the given market type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `Injects premium CSS for a standalone app feel with Islamic green + gold palette.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `Render concept, price, and risk controls.  Supports any cuisine type.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `Injects premium CSS for a standalone app feel with Islamic green + gold palette.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `Rich analytics for Tab 3.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `Rich analytics for Tab 3.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `Compute Local Moran's I (LISA) for gap_score.          Args:         gap_df: Dat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (1 nodes): `Yelp reviews with Gemini halal labels — used for qualitative evidence per NTA.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `Min-max normalize a Series to [0, 1]. Returns 0.0 if constant or all-null.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `A K-Means implementation built from scratch using NumPy.     Supports K-Means++`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `K-Means++ initialization.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `Assign each sample to the nearest centroid.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (1 nodes): `Transform X to a cluster-distance space.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (1 nodes): `Engine for computing composite demand scores.     Integrates Revealed Demand (Ye`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (1 nodes): `build_halal_scores.py — Planned merge façade (currently dormant)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (1 nodes): `scipy>=1.10.0`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Halal pipeline package.` connect `Community 7` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Why does `transform()` connect `Community 0` to `Community 1`, `Community 2`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `TrajectoryClusteringModel` connect `Community 1` to `Community 4`, `Community 5`, `Community 7`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `SurvivalModelBundle` (e.g. with `ProductionScoringAdapter` and `Standalone evaluation script for the NYC Healthy-Food White-Space Finder.  Run w`) actually correct?**
  _`SurvivalModelBundle` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 57 inferred relationships involving `DatasetSpec` (e.g. with `ETL for NYC building permit activity (DOB Permit Issuance).` and `Normalize community-district / NTA-like ids into a stable string code.`) actually correct?**
  _`DatasetSpec` has 57 INFERRED edges - model-reasoned connections that need verification._
- **Are the 39 inferred relationships involving `TrajectoryClusteringModel` (e.g. with `Halal pipeline package.` and `Recommendation endpoints — fully data-driven, works for any NYC area / cuisine.`) actually correct?**
  _`TrajectoryClusteringModel` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `LearnedScoringModel` (e.g. with `ProductionScoringAdapter` and `Standalone evaluation script for the NYC Healthy-Food White-Space Finder.  Run w`) actually correct?**
  _`LearnedScoringModel` has 34 INFERRED edges - model-reasoned connections that need verification._