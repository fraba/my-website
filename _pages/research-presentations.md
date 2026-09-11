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
{% assign sorted = site.research-presentations | sort: 'date' | reverse %}
{% for post in sorted %}
  <li><p><b>{{ post.date | date: "%Y, %d %b" }}</b>. <i><a href="{{ post.url }}">{{ post.presentation-title | default: post.title }}</a> [{{ post.type }}]</i>. {{ post.meeting-name }}, {{ post.place }}.{% if post.meeting-webpage-url %} <a href="{{ post.meeting-webpage-url }}">{{ post.meeting-webpage-url }}</a>{% endif %}</p>
    {% if post.excerpt %}<ul><li>{{ post.excerpt | markdownify }}</li></ul>{% endif %}
  </li>
{% endfor %}
</ul>
