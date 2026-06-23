---
title: Funding and grants
layout: single
permalink: /research-grants/
sidebar:
  nav: sidebar
author_profile: false
share: true
---

<ul>
{% assign sorted = site.grants | sort: 'start-date' | reverse %}
{% for grant in sorted %}
 <li><p><b>{{ grant.start-date | date: "%Y" }}{% if grant.end-date %}–{{ grant.end-date | date: "%Y" }}{% endif %}</b>. {{ grant.title }}. {{ grant.funder }}{% if grant.scheme %}, {{ grant.scheme }}{% endif %}{% if grant.amount %} ({{ grant.amount }}){% endif %}{% if grant.collaborators %}. With {{ grant.collaborators }}{% endif %}.</p></li>
{% endfor %}
</ul>
