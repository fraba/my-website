---
permalink: /media/
title: "Media appereances"
sidebar:
  nav: sidebar
author_profile: false
share: true
---


<ul>
{% assign sorted = site.media-appereances | sort: 'date' | reverse %}
{% for article in sorted %}
 <li><p><b>{{article.date | date:
     "%Y"}}</b>. {{article.authors}}. <a href="{{
    preprint.url }}">{{ article.title
     }}</a>. <i>{{article.publication}}</i>. <a href="{{
     article.publication-url }}">{{ article.publication-url
     }}</a></p></li>
{% endfor %}
</ul>
