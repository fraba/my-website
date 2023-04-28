---
permalink: /publications/
title: "Publications"
author_profile: true
---

## Peer-reviewed articles

{% include_relative publications-peer-reviewed-articles.html %}

### Posts about my articles

<script type="text/javascript">
  function filterUsingCategory(selectedCategory) {
    var id = 0;
    {% for post in site.posts %}
      var cats = {{ post.categories | jsonify }}

      var postDiv = document.getElementById(++id);
      postDiv.style.display =
        (selectedCategory == 'Peer-reviewed articles' || cats.includes(selectedCategory)) 
          ? 'unset' 
          : 'none';
    {% endfor %}
  }
</script>


## Book

{% include_relative publications-books.html %}

## Reports

{% include_relative publications-reports.html %}

## News articles

{% include_relative publications-news-articles.html %}


