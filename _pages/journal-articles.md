---
title: Journal articles
layout: collection
permalink: /journal-articles/
entries_layout: grid
classes: wide
sidebar:
  nav: sidebar
author_profile: false
share: true
---

{% assign sorted = site. journal-articles | sort: 'date' | reverse  %}

{% for journal-article in sorted %}
   <p><b>{{journal-article.date | date: "%Y"}}</b></p> 
  <h2>
    <a href="{{ journal-article.url }}">
      {{ journal-article.title }}
    </a>
  </h2>
  <p>{{ journal-article. authors | markdownify }}. <i>{{ journal-article. publication | markdownify }}</i><p/>
  <p>{{ journal-article. excerpt | markdownify }}</p>
{% endfor %}
