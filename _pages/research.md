---
permalink: /research/
redirect_from:
  - /research-statement/
title: "Research"
sidebar:
  nav: sidebar
author_profile: false
share: true
cutoff_date: "2023-10-01"
---

I am a political scientist specialising in the study of political participation, digital media, and information disorder. I am Deputy Director of the [Centre for AI, Trust and Governance](https://www.sydney.edu.au/arts/our-research/centres-institutes-and-groups/centre-for-ai-trust-and-governance.html) at the University of Sydney, where I do interdisciplinary research combining political science, computational methods, and digital studies.

My work investigates how digital infrastructures reshape political mobilisation, opinion dynamics, and democratic participation. I use large-scale data analysis, longitudinal experiments, and predictive modeling to understand the early diffusion of misinformation, the changing structures of political engagement, and the emergence of new forms of collective action. 

In addition to empirical research, I contribute to methodological innovation. I am developing approaches for collaborative data collection and ontology building, with a [forthcoming book](https://francescobailo.net/EUWDFHWX/), *How to Use Wikibase for Mixed-Methods Research: An Interdisciplinary and Collaborative Approach* (Edward Elgar Publishing, How To Research Guides series).

## Current research

{% assign latest_project = site.projects | sort: 'start-date' | reverse | first %}
{% assign latest_grant = site.grants | sort: 'start-date' | reverse | first %}

<p><b>Latest project</b> — <a href="{{ latest_project.url }}">{{ latest_project.title }}</a>{% if latest_project.status %} <i>({{ latest_project.status }})</i>{% endif %}. {{ latest_project.excerpt }}</p>

<p><b>Latest grant</b> — {{ latest_grant.start-date | date: "%Y" }}{% if latest_grant.end-date %}–{{ latest_grant.end-date | date: "%Y" }}{% endif %}. {{ latest_grant.title }}. {{ latest_grant.funder }}{% if latest_grant.amount %} ({{ latest_grant.amount }}){% endif %}.</p>

See all [projects](/research-projects/) and [funding](/research-grants/).

## Recent peer-reviewed articles

For a list a complete list of publications, [click here](/research-publications/).

{% assign cutoff_date_parsed = page.cutoff_date | date: "%s" %}
{% assign sorted = site.peer-reviewed-articles | sort: 'date' | reverse %}

<ul>
{% for article in sorted %}
  {% assign article_date_parsed = article.date | date: "%s" %}
  {% if article_date_parsed >= cutoff_date_parsed %}
    <li>
      <p><b>{{ article.date | date: "%Y" }}</b>. {{ article.authors }}. 
      <a href="{{ article.url }}">{{ article.title }}</a>. 
      <i>{{article.publication }}</i>. 
      DOI: <a href="{{ article.publication-url }}">{{ article.doi }}</a></p>
    </li>
  {% endif %}
{% endfor %}
</ul>




