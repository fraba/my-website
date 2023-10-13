---
title: Research presentations
layout: single
permalink: /research-presentations/
sidebar:
  nav: sidebar
author_profile: false
share: true
---

<ul>


<ul>
  {% for post in site.categories.Research-presentation %}
    {% if post.url %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
