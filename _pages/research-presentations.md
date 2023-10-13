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
  {% for post in site.posts %}
    {% if post.category == "Research presentation" %}
         <li><p><b>{{post.date | date:
     "%Y, %d %b"}}</b>. {{post.authors}}. <i><a href="{{
     post.url }}">{{ post.title
     }}</a>[{{post.type}}]</i>. {{post. meeting-name}}, {{post. place}}. {{post.meeting-webpage-url}}</p></li>
     <ul>
         <li>{{ post. excerpt | markdownify }}</li>
    </ul>
    {% endif %}
  {% endfor %}
</ul>
