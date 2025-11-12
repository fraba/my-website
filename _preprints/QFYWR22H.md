---
layout: single
permalink: "/QFYWR22H/"
title: "Mapping violence perceptions through YouTube comments: A new approach to real-time violence monitoring"
date: "[2025-11-10]"
comments: true
published: true
share: true
categories: ["preprint"]
tags: ["computational social science", "conflict monitoring", "social media analysis", "Mexico"]
doi: "10.31235/osf.io/rbfuy_v1"
publication: "SocArXiv"
publication-url: "https://doi.org/10.31235/osf.io/rbfuy_v1"
abstract: "This paper introduces the Violence Perception Index (VPI), a novel methodology for quantifying violence-related discourse through geolocated YouTube comments. Utilizing the YouTube API and natural language processing techniques, the VPI measures public references to violence in 3,398,143 geolocated videos across Mexico (2020–2024). This approach provides spatiotemporally granular data on violence perceptions, extending beyond traditional event-based datasets by capturing not only documented violence but also rumors, fears, and community discourse about violence—dimensions that influence community behavior and social stability independently of official records.
Violence scores are constructed using a weighted Spanish-language dictionary developed through semantic network expansion from violence-related seed terms. The dictionary-based scoring approach demonstrates moderate-to-substantial agreement with large language model classifications across 700 stratified comments (75-81% agreement), validating the method's capacity to systematically identify violence-related discourse at scale while maintaining computational efficiency for processing millions of comments.
The VPI is benchmarked against established violence indicators including ACLED fatalities and official municipal homicide statistics through panel regression specifications incorporating comprehensive spatial and temporal fixed effects. Analysis reveals systematic geographic heterogeneity: the VPI correlates strongly with ACLED data in high-population areas but exhibits stronger correlation with official homicide records in low-population contexts. Rather than constituting a methodological limitation, this pattern demonstrates the VPI's enhanced sensitivity in marginalized and remote regions where news-based datasets suffer from systematic reporting bias. The methodology is immediately scalable across languages and geographies, providing complementary intelligence for conflict monitoring, early warning systems, and policy interventions in precisely those underrepresented areas where traditional event-based monitoring systems provide incomplete coverage."
excerpt: "By analyzing millions of geolocated YouTube comments from Mexico, the Violence Perception Index measures how communities discuss and perceive violence—capturing fears, rumors, and local discourse that traditional monitoring systems miss, particularly in remote and marginalized regions."
---

* [Preprint access](10.31235/osf.io/rbfuy_v1)

Violence monitoring has always faced a fundamental challenge: official records and news reports systematically undercount violence in remote and marginalized areas. When a shooting happens in Mexico City, it makes headlines. When it happens in a rural municipality, it often goes unreported.

Our new paper introduces the **Violence Perception Index (VPI)**, which takes a different approach. Instead of counting documented incidents, we measure what people are actually talking about online. Using 3.4 million geolocated YouTube videos and their 44 million associated comments across Mexico (2020-2024), we track violence-related discourse at unprecedented spatial and temporal granularity.

## Why This Matters

The VPI captures something traditional datasets miss: **perception**. When communities fear violence—whether based on direct experience, news reports, or rumors—that fear shapes behavior, economic activity, and social stability. A rumor about cartel activity can empty streets just as effectively as an actual incident. The VPI quantifies this reality.

We built a Spanish-language violence dictionary using semantic network expansion, scoring each comment for violence-related content. Then we aggregated these scores into monthly measures across 50km grid cells covering Mexico, creating a continuous map of violence perception that updates in near-real-time.

## The Key Finding

When we validated the VPI against established violence measures (ACLED fatalities and official homicide statistics), we discovered something striking: the VPI correlates with ACLED in high-population urban areas, but it correlates with official homicide records in low-population contexts where ACLED shows no relationship.

This isn't a limitation—it's the point. News-based datasets like ACLED systematically miss violence in marginalized areas. The VPI detects it because people in these communities are discussing violence on social media even when journalists aren't covering it.

## What We're Measuring

The VPI doesn't distinguish between different types of violence discourse. A high score might reflect:

- Eyewitness accounts of direct experiences
- Expressions of fear or perceived threats
- Discussion of news reports (local or national)
- Rumors and unverified claims
- Historical references to past violence

Each matters differently, but all shape the perception environment that influences community behavior.

Future iterations could separate these signals, distinguishing local experiences from national news discussion, or genuine threats from rumor-mongering. For now, we've demonstrated that systematic measurement of violence perception at scale is feasible and correlates meaningfully with documented violence patterns.

## Implications

The methodology is immediately scalable across languages and geographies. It provides complementary intelligence for conflict monitoring and early warning systems in precisely those underrepresented areas where traditional event-based monitoring fails.

For researchers and policymakers working in conflict-affected contexts, the VPI offers a new tool: one that captures ground-level discourse in marginalized communities, tracks perceptions that shape behavior independently of official records, and provides near-real-time monitoring at fine spatial resolution.

## Access the Research

The Violence Perception Index dataset and complete replication materials are publicly available, enabling researchers to adapt this approach to other contexts where understanding how violence is *perceived*—not just where it's officially recorded—matters for social stability and policy intervention.

**Paper citation:** Amarasinghe, A., Nanlohy, S., Morgan, T., Hammond, D., Dahiya, Y., & Bailo, F. (2025). Mapping violence perceptions through YouTube comments: A new approach to real-time violence monitoring.

**VPI Dataset:** [https://doi.org/10.17605/OSF.IO/FA493](https://doi.org/10.17605/OSF.IO/FA493)

**Replication package:** [https://doi.org/10.7910/DVN/C6TJ9K](https://doi.org/10.7910/DVN/C6TJ9K)




