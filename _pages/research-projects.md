---
title: Research projects
layout: single
permalink: /research-projects/
sidebar:
  nav: sidebar
author_profile: false
share: true
---

<ul>
{% assign sorted = site.projects | sort: 'start-date' | reverse %}
{% for project in sorted %}
 <li><p><a href="{{ project.url }}"><b>{{ project.title }}</b></a>{% if project.status %} <i>({{ project.status }})</i>{% endif %}</p>
    <ul>
        <li>{{ project.excerpt | markdownify }}</li>
    </ul>
 </li>
{% endfor %}
</ul>
