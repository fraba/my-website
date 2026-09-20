---
title: Funding and grants
layout: single
permalink: /research-grants/
sidebar:
  nav: sidebar
author_profile: false
share: true
---

## Internal grants

| Year | Title | Funder | Scheme | Amount | Collaborators |
|---|---|---|---|---|---|
{% assign internal = site.grants | where: 'category', 'Internal' | sort: 'start-date' | reverse %}
{% for grant in internal %}| {{ grant.start-date | date: "%Y" }} | [{{ grant.title }}]({{ grant.url }}) | {{ grant.funder }} | {{ grant.scheme }} | {{ grant.amount }} | {{ grant.collaborators }} |
{% endfor %}

## External grants

| Year | Title | Funder | Scheme | Amount | Collaborators |
|---|---|---|---|---|---|
{% assign external = site.grants | where: 'category', 'External' | sort: 'start-date' | reverse %}
{% for grant in external %}| {{ grant.start-date | date: "%Y" }} | [{{ grant.title }}]({{ grant.url }}) | {{ grant.funder }} | {{ grant.scheme }} | {{ grant.amount }} | {{ grant.collaborators }} |
{% endfor %}
