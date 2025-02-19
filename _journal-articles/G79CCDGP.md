---
layout: single
permalink: "/G79CCDGP/"
title: "Before It's Too Late: A State Space Model for the Early Prediction of Misinformation and Disinformation Engagement"
date: "2025-02-07"
comments: true
published: true
share: true
categories: ["peer-reviewed journal article"]
tags: ["Informations ystems", "Socialnetworks", "Computing methodologies", "Artificial intelligence"]
authors: "Lin Tian, Emily Booth, Francesco Bailo, Julian Droogan, Marian-Andrei Rizoiu"
doi: "10.48550/arXiv.2502.04655"
publication: "WWW '25: Proceedings of the ACM Web Conference 2025"
publication-url: "https://doi.org/10.48550/arXiv.2502.04655"
abstract: "In today’s digital age, conspiracies and information campaigns can emerge rapidly and erode social and democratic cohesion. While recent deep learning approaches have made progress in modeling engagement through language and propagation models, they struggle with irregularly sampled data and early trajectory assessment. We present IC-Mamba , a novel state space model that forecasts social media engagement by modeling intervalcensored data with integrated temporal embeddings. Our model excels at predicting engagement patterns within the crucial first 15-30 minutes of posting (RMSE 0.118-0.143), enabling rapid assessment of content reach. By incorporating interval-censored modeling into the state space framework, IC-Mamba captures finegrained temporal dynamics of engagement growth, achieving a 4.72% improvement over state-of-the-art across multiple engagement metrics (likes, shares, comments, and emojis). Our experiments demonstrate IC-Mamba’s effectiveness in forecasting both post-level dynamics and broader narrative patterns (F1 0.508-0.751 for narrative-level predictions). The model maintains strong predictive performance across extended time horizons, successfully forecasting opinion-level engagement up to 28 days ahead using observation windows of 3-10 days. These capabilities enable earlier identification of potentially problematic content, providing crucial lead time for designing and implementing countermeasures. Code is available at: https://github.com/ltian678/ic-mamba. An interactive dashboard demonstrating our results is available at: https://ic-mamba.behavioral-ds.science/."
excerpt: "The paper introduces IC-Mamba, a novel state space model that forecasts social media engagement by modeling interval-censored data with integrated temporal embeddings, enabling early detection of misinformation and disinformation engagement patterns to facilitate proactive countermeasures"
---

* [Publisher version]()
* [Preprint version](https://arxiv.org/abs/2502.04655)
* [Replication materials](https://github.com/ltian678/ic-mamba)

**Cite** Tian, L., Booth, E., Bailo, F., Droogan, J., & Rizoiu, M.-A. (2025, February 7). Before It’s Too Late: A State Space Model for the Early Prediction of Misinformation and Disinformation Engagement. WWW ’25: Proceedings of the ACM Web Conference 2025. 2025 ACM Web Conference, Sydney. https://doi.org/10.1145/3696410.3714527

In today’s fast-moving digital world, false information can spread like wildfire, influencing public opinion and even destabilising democracies. A new study introduces **IC-Mamba**, an AI-powered model designed to predict how misinformation and disinformation gain traction online—before it’s too late.  

- **Early Detection of Viral Misinformation**  
  IC-Mamba can forecast how misinformation spreads within the first **15-30 minutes** of a post going live, allowing for rapid intervention.  

- **Advanced AI for Social Media Analysis**  
  Unlike traditional models, IC-Mamba processes **irregularly sampled social media data** to better understand engagement trends over time.  

- **Improved Accuracy Over Existing Models**  
  By integrating **interval-censored data** and **state space modeling**, IC-Mamba improves prediction accuracy by **4.72% over state-of-the-art models** across multiple platforms.  

- **A Tool for Proactive Action**  
  This technology enables researchers, platforms, and policymakers to **identify harmful narratives early**, helping to prevent large-scale disinformation campaigns.  

As misinformation becomes more sophisticated, AI-driven solutions like IC-Mamba could play a crucial role in safeguarding online spaces and ensuring the integrity of public debate.
