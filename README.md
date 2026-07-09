# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/harshagarwalnyu/halal-scout-nyc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                      |    Stmts |     Miss |   Cover |   Missing |
|------------------------------------------ | -------: | -------: | ------: | --------: |
| src/\_\_init\_\_.py                       |        0 |        0 |    100% |           |
| src/api/\_\_init\_\_.py                   |        0 |        0 |    100% |           |
| src/api/deps.py                           |        3 |        0 |    100% |           |
| src/api/main.py                           |       16 |        0 |    100% |           |
| src/api/routers/\_\_init\_\_.py           |        0 |        0 |    100% |           |
| src/api/routers/datasets.py               |        7 |        0 |    100% |           |
| src/api/routers/health.py                 |       23 |        5 |     78% |     22-26 |
| src/api/routers/recommendations.py        |      267 |       58 |     78% |66-67, 79-82, 91-95, 104, 272-276, 288-301, 314, 366-368, 373-374, 590-592, 661, 665-688, 701-705, 738-747 |
| src/config/\_\_init\_\_.py                |        4 |        0 |    100% |           |
| src/config/constants.py                   |        7 |        0 |    100% |           |
| src/config/model\_config.py               |       36 |        0 |    100% |           |
| src/config/settings.py                    |       27 |        0 |    100% |           |
| src/data/\_\_init\_\_.py                  |        3 |        0 |    100% |           |
| src/data/audit.py                         |        5 |        0 |    100% |           |
| src/data/base.py                          |       25 |        0 |    100% |           |
| src/data/enrich\_zone\_features.py        |       58 |        0 |    100% |           |
| src/data/etl\_311.py                      |       31 |        0 |    100% |           |
| src/data/etl\_acs.py                      |       75 |       15 |     80% |60, 106, 130-144 |
| src/data/etl\_airbnb.py                   |       53 |        0 |    100% |           |
| src/data/etl\_citibike.py                 |      114 |       10 |     91% |75, 144-145, 160-161, 210-214 |
| src/data/etl\_inspections.py              |       95 |       12 |     87% |116, 126, 198-217 |
| src/data/etl\_licenses.py                 |       34 |        0 |    100% |           |
| src/data/etl\_permits.py                  |       69 |        3 |     96% |49, 53, 69 |
| src/data/etl\_pluto.py                    |       46 |        0 |    100% |           |
| src/data/etl\_runner.py                   |       61 |        0 |    100% |           |
| src/data/etl\_yelp.py                     |      141 |        0 |    100% |           |
| src/data/quality.py                       |      151 |       32 |     79% |94, 107, 116, 120-123, 127-131, 138-164, 180, 184-186, 190, 286 |
| src/data/registry.py                      |       11 |        0 |    100% |           |
| src/features/\_\_init\_\_.py              |        4 |        0 |    100% |           |
| src/features/competition\_score.py        |        7 |        0 |    100% |           |
| src/features/demand\_signals.py           |       27 |        0 |    100% |           |
| src/features/feature\_matrix.py           |      248 |       14 |     94% |207-218, 313-348 |
| src/features/ground\_truth.py             |      114 |        0 |    100% |           |
| src/features/healthy\_gap.py              |        9 |        0 |    100% |           |
| src/features/license\_velocity.py         |       18 |        0 |    100% |           |
| src/features/merchant\_viability.py       |        8 |        0 |    100% |           |
| src/features/microzones.py                |       10 |        0 |    100% |           |
| src/features/rent\_trajectory.py          |       13 |        0 |    100% |           |
| src/features/zone\_crosswalk.py           |      112 |       12 |     89% |76, 89-96, 150-152 |
| src/halal\_demand.py                      |       96 |        5 |     95% |41, 134-138, 177 |
| src/halal\_forecast.py                    |      120 |       50 |     58% |43, 75-181, 299-357 |
| src/halal\_kmeans.py                      |       98 |        5 |     95% |59, 64-66, 92, 130 |
| src/halal\_opportunity.py                 |       29 |        0 |    100% |           |
| src/halal\_risk.py                        |       83 |       41 |     51% |63, 98-193 |
| src/halal\_similarity.py                  |       23 |       23 |      0% |      1-32 |
| src/halal\_spatial.py                     |       68 |       68 |      0% |     1-134 |
| src/halal\_utils.py                       |       10 |        0 |    100% |           |
| src/models/\_\_init\_\_.py                |        4 |        0 |    100% |           |
| src/models/baselines.py                   |        9 |        0 |    100% |           |
| src/models/cmf\_score.py                  |      110 |        3 |     97% |   247-249 |
| src/models/explainability.py              |       64 |        0 |    100% |           |
| src/models/model\_loader.py               |       87 |        0 |    100% |           |
| src/models/ranking\_model.py              |       67 |       15 |     78% |     54-73 |
| src/models/survival\_model.py             |      262 |        2 |     99% |   530-535 |
| src/models/trajectory\_model.py           |      135 |        0 |    100% |           |
| src/nlp/\_\_init\_\_.py                   |        3 |        0 |    100% |           |
| src/nlp/embeddings.py                     |      123 |        0 |    100% |           |
| src/nlp/gemini\_labels.py                 |      158 |        0 |    100% |           |
| src/nlp/neighborhood\_mentions.py         |        4 |        0 |    100% |           |
| src/nlp/review\_aggregates.py             |       77 |        1 |     99% |       149 |
| src/nlp/sentiment.py                      |        2 |        0 |    100% |           |
| src/nlp/subtype\_classifier.py            |       32 |        0 |    100% |           |
| src/nlp/topic\_model.py                   |       45 |        0 |    100% |           |
| src/nlp/white\_space.py                   |        3 |        0 |    100% |           |
| src/pipeline/\_\_init\_\_.py              |        3 |        3 |      0% |       3-6 |
| src/pipeline/orchestrator.py              |       11 |       11 |      0% |      3-20 |
| src/pipeline/preflight.py                 |      104 |      104 |      0% |     3-344 |
| src/pipeline/stages.py                    |        1 |        1 |      0% |         3 |
| src/schemas/\_\_init\_\_.py               |        4 |        0 |    100% |           |
| src/schemas/datasets.py                   |        6 |        0 |    100% |           |
| src/schemas/requests.py                   |       20 |        0 |    100% |           |
| src/schemas/results.py                    |       38 |        0 |    100% |           |
| src/utils/\_\_init\_\_.py                 |        4 |        0 |    100% |           |
| src/utils/geospatial.py                   |       74 |        7 |     91% |   112-121 |
| src/utils/paths.py                        |        6 |        0 |    100% |           |
| src/utils/taxonomy.py                     |       16 |        0 |    100% |           |
| src/validation/\_\_init\_\_.py            |        3 |        0 |    100% |           |
| src/validation/ablation.py                |       75 |        0 |    100% |           |
| src/validation/backtesting.py             |      149 |        0 |    100% |           |
| src/validation/causal.py                  |      335 |       19 |     94% |326, 339, 418, 436, 599-613, 621-629, 639, 646, 649, 740-751 |
| src/validation/run\_causal\_evaluation.py |       37 |        0 |    100% |           |
| **TOTAL**                                 | **4530** |  **519** | **89%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/harshagarwalnyu/halal-scout-nyc/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/harshagarwalnyu/halal-scout-nyc/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/harshagarwalnyu/halal-scout-nyc/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/harshagarwalnyu/halal-scout-nyc/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fharshagarwalnyu%2Fhalal-scout-nyc%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/harshagarwalnyu/halal-scout-nyc/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.