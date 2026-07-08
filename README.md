# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/harshagarwalnyu/halal-scout-nyc/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                      |    Stmts |     Miss |   Cover |   Missing |
|------------------------------------------ | -------: | -------: | ------: | --------: |
| src/\_\_init\_\_.py                       |        0 |        0 |    100% |           |
| src/api/\_\_init\_\_.py                   |        0 |        0 |    100% |           |
| src/api/deps.py                           |        3 |        3 |      0% |       3-9 |
| src/api/main.py                           |       16 |        1 |     94% |        19 |
| src/api/routers/\_\_init\_\_.py           |        0 |        0 |    100% |           |
| src/api/routers/datasets.py               |        7 |        1 |     86% |        16 |
| src/api/routers/health.py                 |       23 |        7 |     70% |22-26, 36-38 |
| src/api/routers/recommendations.py        |      267 |      207 |     22% |36-42, 63-67, 79-82, 91-95, 104, 272-276, 280-301, 305-314, 324-343, 358-389, 408-412, 419-446, 457-474, 510-541, 557-614, 645-720, 735-747, 753-754, 763-790 |
| src/config/\_\_init\_\_.py                |        4 |        0 |    100% |           |
| src/config/constants.py                   |        7 |        0 |    100% |           |
| src/config/model\_config.py               |       36 |        0 |    100% |           |
| src/config/settings.py                    |       27 |        5 |     81% |23, 27, 31, 35, 42 |
| src/data/\_\_init\_\_.py                  |        3 |        0 |    100% |           |
| src/data/audit.py                         |        5 |        1 |     80% |        13 |
| src/data/base.py                          |       25 |        4 |     84% |27, 38, 41, 44 |
| src/data/enrich\_zone\_features.py        |       58 |       50 |     14% |19-57, 68-86, 90-138 |
| src/data/etl\_311.py                      |       31 |       17 |     45% |27, 48-56, 60-79, 84-85 |
| src/data/etl\_acs.py                      |       75 |       61 |     19% |33-34, 38, 48-70, 80-115, 120-147 |
| src/data/etl\_airbnb.py                   |       53 |       38 |     28% |39, 44-77, 82-89, 97-114 |
| src/data/etl\_citibike.py                 |      114 |       92 |     19% |41, 46-85, 90-97, 101-104, 113-219 |
| src/data/etl\_inspections.py              |       95 |       78 |     18% |35, 54-80, 89-127, 131-179, 184-219 |
| src/data/etl\_licenses.py                 |       34 |       22 |     35% |34, 51-63, 67-88, 93-94 |
| src/data/etl\_permits.py                  |       69 |       52 |     25% |26, 47-69, 73-77, 81-150, 155-156 |
| src/data/etl\_pluto.py                    |       46 |       34 |     26% |25, 37-45, 49-110, 115-116 |
| src/data/etl\_runner.py                   |       61 |       49 |     20% |46-56, 79-127 |
| src/data/etl\_yelp.py                     |      141 |       90 |     36% |40-43, 50-53, 81, 86-104, 112-127, 132-142, 172, 178, 194-215, 219-280 |
| src/data/quality.py                       |      151 |      131 |     13% |30-35, 48-202, 213-243, 260-315, 332-352 |
| src/data/registry.py                      |       11 |        0 |    100% |           |
| src/features/\_\_init\_\_.py              |        4 |        0 |    100% |           |
| src/features/competition\_score.py        |        7 |        7 |      0% |      3-18 |
| src/features/demand\_signals.py           |       27 |       27 |      0% |      3-92 |
| src/features/feature\_matrix.py           |      248 |      226 |      9% |43-57, 63-75, 106-396, 401-425, 437-483, 510-543, 550-580 |
| src/features/ground\_truth.py             |      114 |      114 |      0% |     3-256 |
| src/features/healthy\_gap.py              |        9 |        6 |     33% |     11-26 |
| src/features/license\_velocity.py         |       18 |       18 |      0% |      3-60 |
| src/features/merchant\_viability.py       |        8 |        8 |      0% |      3-17 |
| src/features/microzones.py                |       10 |        1 |     90% |        21 |
| src/features/rent\_trajectory.py          |       13 |       13 |      0% |      3-48 |
| src/features/zone\_crosswalk.py           |      112 |       86 |     23% |76, 85-96, 150-152, 180-190, 220-305 |
| src/halal\_demand.py                      |       94 |       94 |      0% |     1-200 |
| src/halal\_forecast.py                    |      120 |       99 |     18% |34-71, 75-181, 185-357 |
| src/halal\_kmeans.py                      |       98 |       89 |      9% |11-18, 21-22, 25-56, 59, 63-144 |
| src/halal\_opportunity.py                 |       29 |       29 |      0% |      1-85 |
| src/halal\_risk.py                        |       83 |       66 |     20% |28-55, 59-65, 69-85, 98-193 |
| src/halal\_similarity.py                  |       23 |       23 |      0% |      1-32 |
| src/halal\_spatial.py                     |       68 |       68 |      0% |     1-134 |
| src/halal\_utils.py                       |       10 |        5 |     50% |     13-17 |
| src/models/\_\_init\_\_.py                |        4 |        0 |    100% |           |
| src/models/baselines.py                   |        9 |        9 |      0% |      3-20 |
| src/models/cmf\_score.py                  |      110 |       70 |     36% |64, 85-97, 114-144, 167-169, 192-201, 214-233, 237-239, 243-249, 253-256, 268-274 |
| src/models/explainability.py              |       64 |       57 |     11% |12-60, 65-105, 145-159 |
| src/models/model\_loader.py               |       87 |       50 |     43% |29, 39-61, 66-69, 74-79, 90-104, 115-120, 131-140 |
| src/models/ranking\_model.py              |       67 |       47 |     30% |39-75, 87-89, 101-111, 115-117, 121-124, 136-142 |
| src/models/survival\_model.py             |      262 |      262 |      0% |     3-677 |
| src/models/trajectory\_model.py           |      135 |      106 |     21% |37-38, 41-93, 97-120, 123-132, 136, 140-143, 153-171, 180-211 |
| src/nlp/\_\_init\_\_.py                   |        3 |        0 |    100% |           |
| src/nlp/embeddings.py                     |      123 |      107 |     13% |31-100, 111-130, 137-149, 159-172, 181-224 |
| src/nlp/gemini\_labels.py                 |      158 |      127 |     20% |39-40, 67-103, 108-115, 120-148, 153-171, 176-183, 188-225, 230-238, 243-257, 280-346 |
| src/nlp/neighborhood\_mentions.py         |        4 |        4 |      0% |      3-10 |
| src/nlp/review\_aggregates.py             |       77 |       77 |      0% |     3-349 |
| src/nlp/sentiment.py                      |        2 |        2 |      0% |       4-7 |
| src/nlp/subtype\_classifier.py            |       32 |       24 |     25% |24, 30-34, 61-82 |
| src/nlp/topic\_model.py                   |       45 |       45 |      0% |     3-111 |
| src/nlp/white\_space.py                   |        3 |        1 |     67% |         9 |
| src/pipeline/\_\_init\_\_.py              |        3 |        3 |      0% |       3-6 |
| src/pipeline/orchestrator.py              |       11 |       11 |      0% |      3-20 |
| src/pipeline/preflight.py                 |      104 |      104 |      0% |     3-344 |
| src/pipeline/stages.py                    |        1 |        1 |      0% |         3 |
| src/schemas/\_\_init\_\_.py               |        4 |        0 |    100% |           |
| src/schemas/datasets.py                   |        6 |        0 |    100% |           |
| src/schemas/requests.py                   |       20 |        7 |     65% |     24-31 |
| src/schemas/results.py                    |       38 |        2 |     95% |     68-90 |
| src/utils/\_\_init\_\_.py                 |        4 |        0 |    100% |           |
| src/utils/geospatial.py                   |       74 |       60 |     19% |28-66, 71-77, 88-125 |
| src/utils/paths.py                        |        6 |        2 |     67% |     13-14 |
| src/utils/taxonomy.py                     |       16 |       10 |     38% |92, 101-110, 115 |
| src/validation/\_\_init\_\_.py            |        3 |        0 |    100% |           |
| src/validation/ablation.py                |       75 |       75 |      0% |     3-211 |
| src/validation/backtesting.py             |      149 |      129 |     13% |27-29, 40-48, 58-60, 66-72, 91-108, 137-155, 187-200, 212-222, 231-243, 247-250, 255-263, 283-378 |
| src/validation/causal.py                  |      335 |      262 |     22% |23-26, 30, 39, 47-51, 94-98, 101-125, 131-136, 141-146, 158-169, 181-194, 204-238, 252-272, 290-313, 319-326, 338-346, 358-372, 387-392, 404-412, 416-418, 428-532, 542-556, 564-586, 594-613, 621-629, 633-649, 658-816, 825-839, 848-854 |
| src/validation/run\_causal\_evaluation.py |       37 |       30 |     19% |18-62, 66-100 |
| **TOTAL**                                 | **4528** | **3606** | **20%** |           |


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