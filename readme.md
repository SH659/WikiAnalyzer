

<a href="https://docs.python.org/3/library/index.html">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
</a>
<a href="https://fastapi.tiangolo.com/">
<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" /> 
</a>
<a href="https://www.docker.com/">
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>
</a>
<a href="https://docs.pytest.org/en/6.2.x/contents.html/">
<img src="https://img.shields.io/badge/coverage-72%25-green.svg"/>
</a>

# Our task is to build an integration and processing system for Wikipedia / Wikimedia.

Our task is to add integration with the Wiki Recent Change API  ([wikimedia endpoint link](https://en.wikipedia.org/w/api.php?action=help&modules=feedrecentchanges)) (alternatively - [WikiMedia Event Stream API](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams)).

As a part of that task, we should design an API that let:
1. Get all Recent Changes as a real-time stream
2. Track in real-time the activity of a particular user or a set of users (this assumes we shall create a user if we have not observed any events from them) 
3. Retrieve a statistic of a particular user which include:
- Information about user contribution as a series of points over time. (Wikipedia User Contribution can be gathered as X Y data points (where X is time and Y is a total number of contributions at that point in time. As an example of such may be taken the following graphic of a user contribution for a Github project
- Note, the API should allow one to specify the time granularity in which the series should be returned 
- Topics to which user has contributed most
- Type of contribution (typos editing | content addition). The type of contribution should be exposed as absolute numbers so one can guess whether the user helps with adding new facts or mostly with copyediting.
4. Retrieve most active user during the (YEAR|MONTH|DAY)
5. Retrieve the top 10 topics which have the most number of typo editings
6. Optional: Retrieve the word in which users do mistake most of the time


## Acceptance Criteria 

1. The project is implemented used functional reactive programming approach
2. Design Project Architecture and present it. Explain the reasons why the specific approach was selected.
3. Explain data flow on the sequence diagram
4. Implement core logic and makes sure that it meets quality criteria (test coverage, manual verification)
5. Explain the reasons, why a specific implementation approach was selected

# Run tests:
```
docker-compose exec backend ./test.sh
```

# Test coverage
```
python -m pytest --cov
```

# Interesting links
- [watchlist](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bwatchlist)
- [usercontribs](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Busercontribs)
- [users](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Busers)
- [mostviewed](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bmostviewed)

