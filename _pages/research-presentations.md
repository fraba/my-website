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


{% capture presentions %}
{{ site.posts where: 'category','Research presentations' %}
{%endcapture%}
{% assign sorted = presentions | sort: 'date' | reverse  %}
{% for post in sorted %}

 <li><p><b>{{post.date | date:"%Y"}}</b>. {{post.authors}}. <a href="{{post.url }}">{{ post.title}}</a></li>

{% endfor %}

</ul>
