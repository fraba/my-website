---
title: "2018 Italian general election: Details on my simulation"
date: "2018-02-28"
categories: 
  - "italian-general-election-2018"
tags: 
  - "gis"
  - "rstat"
  - "simulation"
---

_This article describes the simulation behind the app that you find [here](http://www.francescobailo.net/apps/2018-italian-general-elections-app-en/)_

This simulation of the results for the 2018 general election is based on the results from the last two national elections (the Italian parliament election in 2013 and the European Parliament election 2014) and national polls conducted until 16 February 2018. The simulation is based on one assumption, which is reasonable but not necessarily realistic: the relative territorial strength of parties is stable. From this assumption derives that if the national support for a party (as measured by national voting intention polls) varies, it varies consistently and proportionally _everywhere_. A rising tide lifts all boats and vice versa. The assumption has some empirical justification. If we compare the difference from the national support (in percentage) for each district in 2013 and 2014 we see a significant correlation, especially in the major parties.

\[caption id="attachment\_809" align="aligncenter" width="450"\][![](images/unnamed-chunk-1-1-300x214.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2018/02/unnamed-chunk-1-1.png) Votes to party in the 2018 Chamber districts\[/caption\]

# Pooling polls

To summarise the information provided by a number of opinion polls conducted after January 2018, I used [all polls](https://en.wikipedia.org/wiki/Opinion_polling_for_the_Italian_general_election,_2018#2018) that indicated a sample size. To model each party trend, I used a local regression model with a span of 4 days and weighted based on the sample size (Cleveland, Grosse, and Shyu 1992).

\[caption id="attachment\_810" align="aligncenter" width="450"\][![](images/unnamed-chunk-3-1-1024x731.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2018/02/unnamed-chunk-3-1.png) Polls and local regression model for each party\[/caption\]

For any given party, the last value predicted by the local regression model (that is, the closest to the election day) was used to compute the party percentage vote for each district based on the baseline voting behaviour for the same district.

|  | National vote (%) |
| --- | --- |
| [M5S](https://www.wikidata.org/entity/Q47817) | 27.83 |
| [PD](https://www.wikidata.org/entity/Q47729) | 22.50 |
| [FI](https://www.wikidata.org/entity/Q14924303) | 15.72 |
| [LN](https://www.wikidata.org/entity/Q47750) | 14.41 |
| [LeU](https://www.wikidata.org/entity/Q44929224) | 5.37 |
| [FdI](https://www.wikidata.org/entity/Q1757843) | 4.70 |
| [+E](https://www.wikidata.org/entity/Q47090559) | 2.76 |
| [NcI](https://www.wikidata.org/entity/Q46997473) | 1.53 |
| [CP](https://www.wikidata.org/entity/Q47389793) | 0.79 |
| [I](https://www.wikidata.org/entity/Q46624077) | 0.71 |
| [SVP](https://www.wikidata.org/entity/Q606620) | 0.05 |

# Baseline voting behaviour

The electoral results for the elections of 2013 and 2014 were downloaded from the website of the [Ministry of Interior](http://elezionistorico.interno.gov.it/). Most of the 2018 electoral districts neatly aggregate the territory of Italian communes. Only a few cut through commune borders or are integrally within commune borders. Because I did not have 2013 and 2014 electoral results for these sub communal districts (in the metropolitan areas of Turin, Milan, Genoa, Bologna, Florence, Rome, Bari, Naples and Palermo) I proportionally distributed votes for each party in these districts based on what predicted for each census geographic units contained in the districts by a linear model.

\[caption id="attachment\_815" align="aligncenter" width="450"\][![](images/genova_districts-1024x724.jpg)](http://www.francescobailo.net/wordpress/wp-content/uploads/2018/02/genova_districts.jpg) The Chamber districts intersecting the commune of Genoa\[/caption\]

The linear model used as independent variables the demographics (as collected in the 2011 census) such as the percentage of residents over 65, the percentage of people with a college degree, the unemployment rate, the percentage of people out of the workforce, the percentage of people working as housewives, the percentage of foreigners from different regions of the world and the population density.

\[caption id="attachment\_814" align="aligncenter" width="450"\][![](images/model_genova_area-1024x724.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2018/02/model_genova_area.png) Predicted 2013 results for the M5S at the level of census units (above) and actual 2013 resuls at the level of communes (below). White census units within the districts of Sarra Riccó, Bargagli and Rapallo are not populated.\[/caption\]

# Simulation based on baseline voting behaviour

In each district, the result of a party was simulated sampling a number from an interval determined by the difference from the national result the same party obtained in the district in 2013 and 2014. For example, the M5S obtained 25.62% nationally and 31.86% (Δ = +6.24) in the district of Catania (Sicily) in 2013 and 21.15% nationally and 27.58% locally (Δ = +6.43) in the same district in 2014. The interval from which to draw the random number that will simulate the results for 2018 is defined from 6.24 to 6.43 minus and plus the standard deviation of the same two values (0.1343). That is, For the district of Catania, in each of the 20,000 simulations a random number was drawn from the interval 6.1057 - 6.2957 and then added to what estimated to be the national support for the M5S in February 2018 (based on the opinion polls).

# How votes for parties from the 2013 and 2014 elections are distributed to parties running in 2018

The votes to the parties that do not run in 2018 but where present in previous elections are proportionally distributed based on the following tables.

| Party running in 2013 | Party running in 2018 | Proportion |
| --- | --- | --- |
| MOVIMENTO 5 STELLE BEPPEGRILLO.IT | [M5S](https://www.wikidata.org/entity/Q47817) | 100% |
| PARTITO DEMOCRATICO | [PD](https://www.wikidata.org/entity/Q47729) | 100% |
| IL POPOLO DELLA LIBERTA’ | [FI](https://www.wikidata.org/entity/Q14924303) | 100% |
| SCELTA CIVICA CON MONTI PER L’ITALIA | [NcI](https://www.wikidata.org/entity/Q46997473) | 30% |
| SCELTA CIVICA CON MONTI PER L’ITALIA | [CP](https://www.wikidata.org/entity/Q47389793) | 20% |
| SCELTA CIVICA CON MONTI PER L’ITALIA | [PD](https://www.wikidata.org/entity/Q47729) | 40% |
| SCELTA CIVICA CON MONTI PER L’ITALIA | [+E](https://www.wikidata.org/entity/Q47090559) | 10% |
| LEGA NORD | [LN](https://www.wikidata.org/entity/Q47750) | 100% |
| SINISTRA ECOLOGIA LIBERTA’ | [PD](https://www.wikidata.org/entity/Q47729) | 20% |
| SINISTRA ECOLOGIA LIBERTA’ | [LeU](https://www.wikidata.org/entity/Q44929224) | 80% |
| RIVOLUZIONE CIVILE | [LeU](https://www.wikidata.org/entity/Q44929224) | 100% |
| FRATELLI D’ITALIA | [FdI](https://www.wikidata.org/entity/Q1757843) | 100% |
| UNIONE DI CENTRO | [NcI](https://www.wikidata.org/entity/Q46997473) | 100% |
| FARE PER FERMARE IL DECLINO | [PD](https://www.wikidata.org/entity/Q47729) | 50% |
| FARE PER FERMARE IL DECLINO | [FI](https://www.wikidata.org/entity/Q14924303) | 50% |
| LA DESTRA | [FdI](https://www.wikidata.org/entity/Q1757843) | 100% |
| CENTRO DEMOCRATICO | [+E](https://www.wikidata.org/entity/Q47090559) | 100% |
| FUTURO E LIBERTA’ | [I](https://www.wikidata.org/entity/Q46624077) | 10% |
| FUTURO E LIBERTA’ | [FI](https://www.wikidata.org/entity/Q14924303) | 90% |
| GRANDE SUD - MPA | [FI](https://www.wikidata.org/entity/Q14924303) | 50% |
| GRANDE SUD - MPA | [NcI](https://www.wikidata.org/entity/Q46997473) | 50% |
| SVP | [SVP](https://www.wikidata.org/entity/Q606620) | 100% |
| AUTONOMIE LIBERTE’ DEMOCRATIE | [PD](https://www.wikidata.org/entity/Q47729) | 100% |
| UNION VALDOTAINE PROGRESSISTE | [PD](https://www.wikidata.org/entity/Q47729) | 100% |
| VALLEE D’AOSTE | [PD](https://www.wikidata.org/entity/Q47729) | 20% |
| VALLEE D’AOSTE | [LN](https://www.wikidata.org/entity/Q47750) | 40% |
| VALLEE D’AOSTE | [FI](https://www.wikidata.org/entity/Q14924303) | 40% |

| Party running in 2014 | Party running in 2018 | Proportion |
| --- | --- | --- |
| FORZA ITALIA | [FI](https://www.wikidata.org/entity/Q14924303) | 100% |
| FRATELLI D’ITALIA - ALLEANZA NAZIONALE | [FdI](https://www.wikidata.org/entity/Q1757843) | 100% |
| PARTITO DEMOCRATICO | [PD](https://www.wikidata.org/entity/Q47729) | 100% |
| MOVIMENTO 5 STELLE BEPPEGRILLO.IT | [M5S](https://www.wikidata.org/entity/Q47817) | 100% |
| LEGA NORD-DIE FREIHEITLICHEN-BASTA EURO | [LN](https://www.wikidata.org/entity/Q47750) | 100% |
| NUOVO CENTRO DESTRA - UDC | [FI](https://www.wikidata.org/entity/Q14924303) | 40% |
| NUOVO CENTRO DESTRA - UDC | [NcI](https://www.wikidata.org/entity/Q46997473) | 40% |
| NUOVO CENTRO DESTRA - UDC | [CP](https://www.wikidata.org/entity/Q47389793) | 20% |
| L’ALTRA EUROPA CON TSIPRAS | [LeU](https://www.wikidata.org/entity/Q44929224) | 100% |
| VERDI EUROPEI-GREEN ITALIA | [I](https://www.wikidata.org/entity/Q46624077) | 100% |
| SCELTA EUROPEA | [NcI](https://www.wikidata.org/entity/Q46997473) | 30% |
| SCELTA EUROPEA | [CP](https://www.wikidata.org/entity/Q47389793) | 20% |
| SCELTA EUROPEA | [PD](https://www.wikidata.org/entity/Q47729) | 40% |
| SCELTA EUROPEA | [+E](https://www.wikidata.org/entity/Q47090559) | 10% |
| ITALIA DEI VALORI | [LeU](https://www.wikidata.org/entity/Q44929224) | 100% |
| SVP | [SVP](https://www.wikidata.org/entity/Q606620) | 100% |

# Results

In total I run 20,000 simulations and calculated the distribution of seats for each simulation. The distribution of seats at the level of coalitions are presented in the following figures.

\[caption id="attachment\_811" align="aligncenter" width="450"\][![](images/unnamed-chunk-8-1-1024x731.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2018/02/unnamed-chunk-8-1.png) Density of the distribution of seats based on the simulation (Chamber)\[/caption\]

\[caption id="attachment\_812" align="aligncenter" width="450"\][![](images/unnamed-chunk-8-2-1024x731.png)](http://www.francescobailo.net/wordpress/wp-content/uploads/2018/02/unnamed-chunk-8-2.png) Density of the distribution of seats based on the simulation (Senate)\[/caption\]

# References

Cleveland, William S., E. Grosse, and W. M. Shyu. 1992. “Local Regression Models. Chapter 8.” In _Statistical Models in S_, edited by John M Chambers and Trevor Hastie. Pacific Grove, CA: Wadsworth & Brooks.
