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

{% for journal-article in site. journal-articles %}
  <h2>
    <a href="{{ journal-article.url }}">
      {{ journal-article.title }}
    </a>
  </h2>
  <p>{{ journal-article. excerpt | markdownify }}</p>
{% endfor %}
