---
title: "Using r/exams in SSPS4102 Data Analytics in the Social Sciences"
excerpt_separator: "To support the coupling of both statistical concepts and R in the learning experience, I designed a series of short, hands-on exercises with the R package R/exams to practice statistical concepts that students encounter in the unit, applying them to real-world problems. "
date: 2023-10-23
categories:
  - Blog
  - Teaching
  - R
tags:
  - Rexams
  - "Data Analytics in the Social Sciences"
  - SSPS4102
  - Canvas
---

> In October 2023, I was one of the recipients of  the *Teaching Innovation Awards* of the the Faculty of Arts and Social Sciences of the University of Sydney (for "recognising and encouraging the creative and experimental ideas and practices that educators implement to meet current teaching and learning challenges"). Below is the description of the innovation I implemented in 2023 in [SSPS4102: Data Analytics in the Social Sciences](https://www.sydney.edu.au/units/SSPS4102).  

The unit SSPS4102 introduces undergraduate students with different disciplinary backgrounds to statistical concepts critical to consuming and producing quantitative research in the social sciences. The unit exposes students, mostly for the first time, to the R programming language and the RStudio software. The **reflective engagement** with the statistical software R and RStudio points to giving students practice-based data analysis skills to apply the knowledge acquired during the unit to self-directed research projects. The unit includes a weekly 3-hour seminar, and generative feedback is provided to students throughout the session. 

This unit is challenging for two reasons. First, by engaging with data analytics concepts and processes, social science students often find themself out of their disciplinary comfort zone. Second, students must simultaneously engage in two independent dimensions: statistical and programming. I address these two challenges in the unit's design by developing two streams of continuous in-class assessments. According to **active learning** principles, in class, students are 1) **exposed** to statistical and programming concepts and 2) **asked to apply **the concepts creatively and independently through practical individual and collective hands-on live programming tasks. The first assessment stream involves data-based problem sets to be completed in groups. The second assessment stream involves interactive statistical exercises to be completed individually using R. In the next section, I discuss the innovative aspects of this second assessment stream.

To support the coupling of both statistical concepts and R in the learning experience, I designed a series of short, hands-on exercises to practice statistical concepts that students encounter in the unit, applying them to real-world problems. The exercises have two goals: 1) allowing students to **self-assess** their understanding of the statistical concepts covered and 2) allowing students to **apply the concepts to real data** using R and practice across authentic scenarios. A further innovative aspect of these exercises is using the open-source R package ‘exams’ ([https://www.r-exams.org/](https://www.r-exams.org/)).

The use of this package has many advantages. Once developed, each exercise can be seamlessly imported to Canvas using the _Question and Test Interoperability_ (QTI) format, recognised by Learning Management Systems (LMS). The type of answers to be included in the exercises (i.e. multiple-choice answers, numeric answers, or text answers), as well as the criteria to assess them automatically (e.g. perfect match, match across different options), can be set offline in the exercise document, and then **imported into Canvas**. This makes creating and maintaining a stock of exercises - potentially to be used across a range of units - much more streamlined and effective. In addition, across this package, exercises are generated **dynamically** The exercise document is a template that can dynamically generate **random variations** of the same exercise by varying values or the questions’ selection. In this case, meaningful use of technology supports both students and instructors in scaffolding learning experiences. 

The advantages of the R package ‘exam’ include the opportunity **to integrate into Canvas a relatively large number of practice-based exercises** (e.g. 22 concept-based exercises in 2023), which students can take multiple times - including during self-study - and with variations, thanks to the randomised design. Also, because exercises are integrated with Canvas’ Markbook and new ones are published every week as new concepts are introduced, the assessment stream produces important weekly data points about the pace of students’ learning, allowing instructors to provide prompt generative feedback. It is then possible to identify students struggling with learning outcomes and **act immediately with personalised support**. 

This model and the use of R was first adopted in this unit in 2023, under my coordination. **Students responded very positively** to the innovations introduced. The Unit of Study Survey was completed by 74% of the cohort, an important indicator of engagement with the unit. To the USS question on whether “the assessment tasks challenged me to learn”, **71.4%** of students responded to “strongly agree” (with a mean rating of **4.64**), while to the question on whether students felt to “have been guided by helpful feedback on my learning” **51.1%** of students responded to “strongly agree” (with a mean rating of **4.5**).