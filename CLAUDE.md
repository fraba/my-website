# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Francesco Bailo's academic personal site — a Jekyll site built on the remote theme `mmistakes/minimal-mistakes`, hosted on GitHub Pages (custom domain via `CNAME`: francescobailo.net).

## Commands

```bash
bundle install          # install gems (first time / after Gemfile changes)
bundle exec jekyll serve # run local dev server (http://localhost:4000), rebuild on save
bundle exec jekyll build # build the static site into _site/
```

There is no test suite, linter, or CI config in this repo — changes are verified by building/serving locally and checking pages render.

## Architecture

This is a content-only Jekyll repository (no custom plugins/Ruby code). The two things to understand are the **collection system** and the **link-post pattern**.

### Collections hold the actual content

Site content lives in per-type collections declared in `_config.yml`, each with its own directory and `defaults` block: `_peer-reviewed-articles`, `_books`, `_book-sections`, `_research-reports`, `_news-articles`, `_media-appereances`, `_research-presentations`, `_teaching-units`, `_preprint-articles`.

Every item in these collections:
- Is a single Markdown file named with an 8-character alphanumeric key (a Zotero item key, e.g. `5CQTZXZP.md`), not a slug.
- Sets its own `permalink: "/<KEY>/"` in front matter, so the item is reachable at the site root (e.g. `francescobailo.net/5CQTZXZP/`), independent of which collection it lives in.
- Carries citation-style metadata in front matter — `authors`, `date`, `publication`, `doi`, `publication-url`, `abstract`, `excerpt`, plus type-specific fields (e.g. presentations use `presentation-title`, `presenters`, `meeting-name`, `place`; media appearances use `program`).

Listing pages in `_pages/` (e.g. `research-publications.md`, `research-presentations.md`) pull from these collections at build time via Liquid, e.g.:
```liquid
{% assign sorted = site.peer-reviewed-articles | sort: 'date' | reverse %}
{% for article in sorted %} ... {% endfor %}
```
When adding a new collection or renaming front-matter fields, update both the `_config.yml` collection/defaults block and every listing page that loops over `site.<collection>`.

### `_posts` are mostly short "link posts"

Almost all files in `_posts/` (63 of 65) are minimal stub posts whose entire body is a `link:` front-matter field pointing at one of the permalink pages above, e.g.:
```yaml
---
title: "📻  ABC @ Antropic, Mythos and Fable"
permalink: "/2026/06/16/abc-antropic-mythos-fable/"
date: "2026-06-16"
tags:
  - link
link: https://francescobailo.net/6TIP8P66/
---
```
These act as chronological blog/feed entries ("I published X") that reference the canonical collection item rather than duplicating its content. When adding a new publication/presentation/media item, the usual flow is: (1) add the collection item under its 8-char key, (2) add a short dated link-post in `_posts/` pointing to `/​<KEY>/`.

### Front matter defaults

`_config.yml` sets `defaults:` per collection/type (layout, `author_profile`, `share`, sidebar nav). Most collection items use `layout: single` with `author_profile: false` and a `sidebar: nav: sidebar` block; `_posts` and `_pages` use `author_profile: true`. Sidebar navigation itself is defined in `_data/navigation.yml` (`main` = top nav, `sidebar` = the Research/Teaching/Media sidebar tree) — new top-level sections need an entry there.

### Static pages

`_pages/` holds the site's static/listing pages (About, CV links, statements, and the publication/presentation listing pages described above). `_pages` is explicitly included via `include:` in `_config.yml` since Jekyll doesn't process underscore-prefixed dirs by default.
