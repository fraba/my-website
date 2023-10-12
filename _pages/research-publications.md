---
title: Research publication
layout: single
permalink: /research-publications/
sidebar:
  nav: sidebar
author_profile: false
share: true
---

## Journal articles

<ul>

{% assign sorted = site. journal-articles | sort: 'date' | reverse  %}

{% for journal-article in sorted %}

 <li><p><b>{{journal-article.date | date:
     "%Y"}}</b>. {{journal-article.authors}}. <a href="{{
     journal-article.url }}">{{ journal-article.title
     }}</a>. <i>{{journal-article.publication}}</i>. DOI: <a href="{{
     journal-article.publication-url }}">{{ journal-article.doi
     }}</a></p></li>
     <ul>
         <li>{{ journal-article. excerpt | markdownify }}</li>
    </ul>

{% endfor %}

</ul>

## Book

<ul>

{% assign sorted = site. book | sort: 'date' | reverse  %}

{% for book in sorted %}

 <li><p><b>{{book.date | date:
     "%Y"}}</b>. {{book.authors}}. <i><a href="{{
     book.url }}">{{ book.title
     }}</a></i>. {{book.publisher}}. DOI: <a href="{{
     book.publication-url }}">{{ book.doi
     }}</a></p></li>
     <ul>
         <li>{{ book. excerpt | markdownify }}</li>
    </ul>

{% endfor %}

</ul>

## Book sections

<ul>

{% assign sorted = site. book-sections | sort: 'date' | reverse  %}

{% for book-section in sorted %}

 <li><p><b>{{ book-section.date | date:
     "%Y"}}</b>. {{ book-section.authors}}. <a href="{{
     book.url }}">{{  book-section.title
     }}</a>. In  {{book-section.editors}}. <i>{{book-section.book-title}}</i>. {{book-section.publisher}}. DOI: <a href="{{
     book-section.publication-url }}">{{  book-section.doi
     }}</a></p></li>
     <ul>
         <li>{{ book. excerpt | markdownify }}</li>
    </ul>

{% endfor %}

</ul>

