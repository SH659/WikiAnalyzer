# My task is to build an integration and processing system for Wikipedia / Wikimedia.

My task is to add integration with the Wiki Recent Change API  ([wikimedia endpoint link](https://en.wikipedia.org/w/api.php?action=help&modules=feedrecentchanges)) (alternatively - [WikiMedia Event Stream API](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams)).

As a part of that task, you should design an API that let:
1. Get all Recent Changes as a real-time stream
2. Track in real-time the activity of a particular user or a set of users (this assumes you shall create a user if you have not observed any events from them) 
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


## Моя задача - построить систему интеграции и обработки для Википедии / Викимедиа.

Моя задача - добавить интеграцию с Wiki Recent Change API (ссылка на конечную точку wikimedia) (альтернативно - WikiMedia Event Stream API).

В рамках этой задачи вам следует разработать API, который позволит:
- [x] Получите все недавние изменения в виде потока в реальном времени.
- [x] Отслеживайте в режиме реального времени активность конкретного пользователя или группы пользователей (это предполагает, что вы должны создать пользователя, если вы не наблюдали каких-либо событий от них)
- [x]  Получить статистику конкретного пользователя, которая включает:
- [x]  Информация о вкладе пользователей в виде набора точек с течением времени. (Вклад пользователей Википедии можно собрать в виде точек данных X Y (где X - время, а Y - общее количество вкладов в этот момент времени. В качестве примера может быть взята следующая диаграмма вклада пользователя в проект Github).
- [x]  Обратите внимание, что API должен позволять указывать гранулярность по времени, в которой должна быть возвращена серия.
- [x]  Темы, в которые пользователь внес наибольший вклад
- [x]  Тип вклада (редактирование опечаток | добавление контента). Тип вклада должен быть представлен в виде абсолютных чисел, чтобы можно было догадаться, помогает ли пользователь добавлять новые факты или в основном редактировать.
- [ ]  Получить наиболее активных пользователей за (ГОД | МЕСЯЦ | ДЕНЬ)
- [ ]  Найдите 10 самых популярных тем, в которых было исправлено наибольшее количество опечаток.
- [ ]  Необязательно: найдите слово, в котором пользователи чаще всего ошибаются.


# Критерии приемки

1. В проекте реализован подход функционального реактивного программирования.
2. Разработайте архитектуру проекта и представьте ее. Объясните причины, по которым был выбран конкретный подход.
3. Объясните поток данных на диаграмме последовательности.
4. Реализуйте основную логику и убедитесь, что она соответствует критериям качества (охват тестированием, ручная проверка).
5. Объясните причины, по которым был выбран конкретный подход к реализации.


# Run tests:
```
docker-compose exec backend ./test.sh
```