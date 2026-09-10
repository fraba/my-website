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
      <td><a href="{{ u.url }}"><strong>{{ u.unit-code }}</strong> {{ u.unit-name }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>
        {% if u.outline-url %}<a href="{{ u.outline-url }}">Outline</a>{% endif %}
        {% if u.slides-url %}{% if u.outline-url %} · {% endif %}<a href="{{ u.slides-url }}">Slides</a>{% endif %}
        {% if u.materials-url %} · <a href="{{ u.materials-url }}">Materials</a>{% endif %}
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
      <td><a href="{{ u.url }}"><strong>{{ u.unit-code }}</strong> {{ u.unit-name }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>
        {% if u.outline-url %}<a href="{{ u.outline-url }}">Outline</a>{% endif %}
        {% if u.slides-url %}{% if u.outline-url %} · {% endif %}<a href="{{ u.slides-url }}">Slides</a>{% endif %}
        {% if u.materials-url %} · <a href="{{ u.materials-url }}">Materials</a>{% endif %}
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
      <td><a href="{{ u.url }}"><strong>{{ u.unit-code }}</strong> {{ u.unit-name }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>
        {% if u.outline-url %}<a href="{{ u.outline-url }}">Outline</a>{% endif %}
        {% if u.slides-url %}{% if u.outline-url %} · {% endif %}<a href="{{ u.slides-url }}">Slides</a>{% endif %}
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
      <td><a href="{{ u.url }}"><strong>{{ u.unit-code }}</strong> {{ u.unit-name }}</a></td>
      <td>{{ u.school }}, {{ u.institution }}</td>
      <td>{% if u.outline-url %}<a href="{{ u.outline-url }}">Outline</a>{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

## Workshops

<table class="teaching-table">
  <thead><tr><th>Date</th><th>Workshop</th><th>Host</th><th>Links</th></tr></thead>
  <tbody>
    <tr><td>Jul 2026</td><td><strong>AI Winter School</strong> — led the design of the inaugural School</td><td>Centre for AI, Trust and Governance, University of Sydney</td><td><a href="https://www.sydney.edu.au/arts/our-research/centres-institutes-and-groups/centre-for-ai-trust-and-governance/caitg-ai-winter-school-2026.html">Program</a></td></tr>
    <tr><td>Jul 2022</td><td><strong>(The art of) text mining and analysis</strong></td><td>Winter School Training Session – ANZCA, University of Canberra</td><td><a href="https://fraba.github.io/2022-ANZCA-workshop-The-art-of-text-analysis/">Materials</a></td></tr>
    <tr><td>Jul 2021</td><td><strong>How to do social media data analysis using Tableau</strong></td><td>School of Communication, University of Technology Sydney</td><td></td></tr>
    <tr><td>Dec 2018</td><td><strong>Topic Models in R</strong></td><td>DH Downunder 2018 Summer School, Western Sydney University and the University of Sydney</td><td><a href="https://digital-methods-sydney.github.io/ws-201812/">Materials</a></td></tr>
    <tr><td>Jun 2018</td><td><strong>Digital methods workshop: social network analysis, Twitter data collection, text analysis and the R software</strong></td><td>Department of Media and Communications, the University of Sydney</td><td><a href="https://digital-methods-sydney.github.io/ws-201806/">Materials</a></td></tr>
    <tr><td>Nov–Dec 2016</td><td><strong>Digital media methods: applications of R software and RStudio to social research</strong></td><td>Department of Media and Communications, the University of Sydney</td><td><a href="https://fraba.github.io/digital_media_methods_sydney/">Materials</a></td></tr>
  </tbody>
</table>

<style>
.teaching-table { width: 100%; border-collapse: collapse; margin-bottom: 2em; font-size: 0.85em; }
.teaching-table th, .teaching-table td { text-align: left; vertical-align: top; padding: 0.4em 0.6em; border-bottom: 1px solid #e0e0e0; }
.teaching-table thead th { border-bottom: 2px solid #bbb; white-space: nowrap; }
.teaching-table td:first-child, .teaching-table th:first-child { white-space: nowrap; }
.teaching-table td:last-child, .teaching-table th:last-child { white-space: nowrap; }
</style>
