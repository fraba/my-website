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

<ul>

{% assign sorted = site. journal-articles | sort: 'date' | reverse  %}

{% for journal-article in sorted %}

 <li><p><b>{{journal-article.date | date: "%Y"}}</b>. {{
     journal-article. authors | markdownify }}. <i>{{journal-article. publication | markdownify}}</i>. <a href="{{ journal-article.url }}">{{ journal-article.title }}</a></li>
     <ul>
         <li>{{ journal-article. excerpt | markdownify }}</li>
    </ul>

{% endfor %}

</ul>
