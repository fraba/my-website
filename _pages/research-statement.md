---
permalink: /research-statement/
title: "Research statement"
sidebar:
  nav: sidebar
author_profile: false
share: true
---

I am a political scientist specialising in the study of political participation, digital media, and information disorder. I am Deputy Director of the [Centre for AI, Trust and Governance](https://www.sydney.edu.au/arts/our-research/centres-institutes-and-groups/centre-for-ai-trust-and-governance.html) at the University of Sydney, where I do interdisciplinary research combining political science, computational methods, and digital studies.

My work investigates how digital infrastructures reshape political mobilisation, opinion dynamics, and democratic participation. I use large-scale data analysis, longitudinal experiments, and predictive modeling to understand the early diffusion of misinformation, the changing structures of political engagement, and the emergence of new forms of collective action. 

In addition to empirical research, I contribute to methodological innovation. I am developing approaches for collaborative data collection and ontology building, with a [forthcoming book](https://francescobailo.net/EUWDFHWX/), *How to Use Wikibase for Mixed-Methods Research: An Interdisciplinary and Collaborative Approach* (Edward Elgar Publishing, How To Research Guides series).

## Recent peer-reviewed articles

{% assign six_months_ago = 'now' | date: '%s' | minus: 15778463 %}
{% assign sorted = site.journal-articles | sort: 'date' | reverse %}

<ul>
{% for journal-article in sorted %}
  {% assign article_timestamp = journal-article.date | date: '%s' %}
  {% if article_timestamp >= six_months_ago %}
    <li>
      <p><b>{{ journal-article.date | date: "%Y" }}</b>. {{ journal-article.authors }}. 
      <a href="{{ journal-article.url }}">{{ journal-article.title }}</a>. 
      <i>{{ journal-article.publication }}</i>. 
      DOI: <a href="{{ journal-article.publication-url }}">{{ journal-article.doi }}</a></p>
    </li>
    <ul>
      <li>{{ journal-article.excerpt | markdownify }}</li>
    </ul>
  {% endif %}
{% endfor %}
</ul>



