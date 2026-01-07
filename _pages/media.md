---
permalink: /media/
title: "Media appereances"
sidebar:
  nav: sidebar
author_profile: false
share: true
---


<ol>
{% assign sorted = site.media-appereances | sort: 'date' | reverse %}
{% for article in sorted %}
 <li><p><b>{{article.date | date:
     "%Y"}}</b>. {{article.authors}}. <a href="{{
    article.url }}">{{ article.title
     }}</a>. <i>{{article.publication}}</i>.</p></li>
{% endfor %}
</ol>
