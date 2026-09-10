---
permalink: /teaching-courses/
title: "Courses and workshops"
sidebar:
  nav: sidebar
author_profile: false
share: true
toc: true
toc_label: "On this page"
---

{% assign units = site.teaching-units | sort: "year" | reverse %}
{% assign coordinated = units | where: "role", "coordinator" %}
{% assign pg = coordinated | where: "level", "postgraduate" %}
{% assign ug = coordinated | where: "level", "undergraduate" %}
{% assign guest = units | where: "role", "guest lecturer" %}
{% assign ta = units | where: "role", "teaching assistant" %}

## Course coordination

### Postgraduate

<table class="teaching-table">
  <thead><tr><th>Year</th><th>Unit</th><th>School</th><th>Links</th></tr></thead>
  <tbody>
  {% for u in pg %}
    <tr>
      <td>{{ u.year }}</td>
      <td><a href="{{ u.url }}"><strong>{{ u["unit-code"] }}</strong> {{ u["unit-name"] }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>
        {% if u["outline-url"] %}<a href="{{ u['outline-url'] }}">Outline</a>{% endif %}
        {% if u["slides-url"] %}{% if u["outline-url"] %} · {% endif %}<a href="{{ u['slides-url'] }}">Slides</a>{% endif %}
        {% if u["materials-url"] %} · <a href="{{ u['materials-url'] }}">Materials</a>{% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

### Undergraduate

<table class="teaching-table">
  <thead><tr><th>Year</th><th>Unit</th><th>School</th><th>Links</th></tr></thead>
  <tbody>
  {% for u in ug %}
    <tr>
      <td>{{ u.year }}</td>
      <td><a href="{{ u.url }}"><strong>{{ u["unit-code"] }}</strong> {{ u["unit-name"] }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>
        {% if u["outline-url"] %}<a href="{{ u['outline-url'] }}">Outline</a>{% endif %}
        {% if u["slides-url"] %}{% if u["outline-url"] %} · {% endif %}<a href="{{ u['slides-url'] }}">Slides</a>{% endif %}
        {% if u["materials-url"] %} · <a href="{{ u['materials-url'] }}">Materials</a>{% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

## Guest lecturing

<table class="teaching-table">
  <thead><tr><th>Year</th><th>Unit</th><th>School</th><th>Links</th></tr></thead>
  <tbody>
  {% for u in guest %}
    <tr>
      <td>{{ u.year }}</td>
      <td><a href="{{ u.url }}"><strong>{{ u["unit-code"] }}</strong> {{ u["unit-name"] }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>
        {% if u["outline-url"] %}<a href="{{ u['outline-url'] }}">Outline</a>{% endif %}
        {% if u["slides-url"] %}{% if u["outline-url"] %} · {% endif %}<a href="{{ u['slides-url'] }}">Slides</a>{% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

## Teaching assistant

<table class="teaching-table">
  <thead><tr><th>Year</th><th>Unit</th><th>School</th><th>Links</th></tr></thead>
  <tbody>
  {% for u in ta %}
    <tr>
      <td>{{ u.year }}</td>
      <td><a href="{{ u.url }}"><strong>{{ u["unit-code"] }}</strong> {{ u["unit-name"] }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>{% if u["outline-url"] %}<a href="{{ u['outline-url'] }}">Outline</a>{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

## Workshops

{% assign workshops = site.workshops | sort: "date" | reverse %}

<table class="teaching-table">
  <thead><tr><th>Date</th><th>Workshop</th><th>Host</th><th>Links</th></tr></thead>
  <tbody>
  {% for w in workshops %}
    <tr>
      <td>{{ w["date-display"] | default: w.date }}</td>
      <td><a href="{{ w.url }}"><strong>{{ w.title }}</strong></a>{% if w.role %} <span class="workshop-role">— {{ w.role | downcase }}</span>{% endif %}</td>
      <td>{{ w.host }}</td>
      <td>
        {% if w["event-url"] %}<a href="{{ w['event-url'] }}">Program</a>{% endif %}
        {% if w["materials-url"] %}{% if w["event-url"] %} · {% endif %}<a href="{{ w['materials-url'] }}">Materials</a>{% endif %}
        {% if w["slides-url"] %} · <a href="{{ w['slides-url'] }}">Slides</a>{% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<style>
.teaching-table { width: 100%; border-collapse: collapse; margin-bottom: 2em; font-size: 0.85em; }
.teaching-table th, .teaching-table td { text-align: left; vertical-align: top; padding: 0.4em 0.6em; border-bottom: 1px solid #e0e0e0; }
.teaching-table thead th { border-bottom: 2px solid #bbb; white-space: nowrap; }
.teaching-table td:first-child, .teaching-table th:first-child { white-space: nowrap; }
.teaching-table td:last-child, .teaching-table th:last-child { white-space: nowrap; }
.workshop-role { color: #888; font-style: italic; }
</style>
