---
title: "Posts by Tag"
permalink: /tags/
layout: single
author_profile: true
toc: true
toc_label: "All Tags"
excerpt: "Explore all topics covered on this site, organised by tags with descriptions and post counts."
---

Discover content organized by topic. Each tag represents a collection of related posts that dive deep into specific areas of interest.

{% assign tag_data = site.data.tag-descriptions %}
{% assign sorted_tags = site.tags | sort %}

<div class="tag-summary-grid">
{% for tag in sorted_tags %}
  {% assign tag_name = tag[0] %}
  {% assign tag_posts = tag[1] %}
  {% assign tag_info = tag_data[tag_name] %}
  
  <div class="tag-card" style="margin-bottom: 2em; padding: 1.5em; border: 1px solid #e9ecef; border-radius: 8px; background: {% if tag_info.color %}{{ tag_info.color }}10{% else %}#f8f9fa{% endif %};">
    <div class="tag-header" style="display: flex; align-items: center; margin-bottom: 1em;">
      {% if tag_info.icon %}
        <i class="{{ tag_info.icon }}" style="color: {{ tag_info.color | default: '#6c757d' }}; font-size: 1.8em; margin-right: 0.75em;"></i>
      {% else %}
        <i class="fas fa-tag" style="color: #6c757d; font-size: 1.8em; margin-right: 0.75em;"></i>
      {% endif %}
      <div>
        <h3 style="margin: 0; color: {{ tag_info.color | default: '#333' }};">
          {% if tag_info %}
            <a href="/tags/{{ tag_name | slugify }}/" style="text-decoration: none; color: inherit;">
              {{ tag_name | capitalize }}
            </a>
          {% else %}
            <a href="/tags/#{{ tag_name | slugify }}" style="text-decoration: none; color: inherit;">
              {{ tag_name | capitalize }}
            </a>
          {% endif %}
        </h3>
        <small style="color: #6c757d;">{{ tag_posts.size }} post{% if tag_posts.size != 1 %}s{% endif %}</small>
      </div>
    </div>
    
    {% if tag_info.description %}
      <p style="margin-bottom: 1em; color: #495057;">{{ tag_info.description }}</p>
    {% else %}
      <p style="margin-bottom: 1em; color: #6c757d; font-style: italic;">Posts tagged with "{{ tag_name }}"</p>
    {% endif %}
    
    <div class="tag-posts" style="margin-top: 1em;">
      <strong>Recent posts:</strong>
      <ul style="margin-top: 0.5em;">
        {% for post in tag_posts limit: 3 %}
          <li>
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            <small style="color: #6c757d;">({{ post.date | date: "%b %Y" }})</small>
          </li>
        {% endfor %}
        {% if tag_posts.size > 3 %}
          <li>
            {% if tag_info %}
              <a href="/tags/{{ tag_name | slugify }}/">View all {{ tag_posts.size }} posts →</a>
            {% else %}
              <a href="/tags/#{{ tag_name | slugify }}">View all {{ tag_posts.size }} posts →</a>
            {% endif %}
          </li>
        {% endif %}
      </ul>
    </div>
  </div>
{% endfor %}
</div>

## All Posts by Tag

{% for tag in sorted_tags %}
  {% assign tag_name = tag[0] %}
  {% assign tag_posts = tag[1] %}
  
  <h3 id="{{ tag_name | slugify }}">{{ tag_name | capitalize }}</h3>
  {% for post in tag_posts %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}

<style>
.tag-summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5em;
  margin-top: 2em;
  margin-bottom: 3em;
}

.tag-card:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transform: translateY(-2px);
  transition: all 0.3s ease;
}

.tag-card a {
  color: inherit;
}

.tag-card a:hover {
  text-decoration: none;
}

@media (max-width: 768px) {
  .tag-summary-grid {
    grid-template-columns: 1fr;
  }
}
</style>
