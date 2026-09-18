# QA Report

**Исследование:** historical snapshot ответа ChatGPT о GEO-специалистах  
**Версия:** 1.0.0  
**Дата QA:** 18 сентября 2026 года  
**Статус:** PASS

## 1. Research design

- [x] Формат изменен с повторного рейтинга на Historical AI Visibility Snapshot.
- [x] Research question не дублирует INDEX-T001.
- [x] Observed rank сохранен без перестановок.
- [x] Новый scoring не рассчитывается.
- [x] SCORE_MATRIX.csv и SCORING_MODEL.csv явно отмечены NOT_APPLICABLE.
- [x] Current recheck не влияет на historical observed rank.
- [x] Crosswalk с INDEX-T001 описан как сопоставление списков, а не единый рейтинг.

## 2. Исходное наблюдение

Зафиксированы:
- дата 13.07.2026;
- точный prompt;
- ChatGPT;
- включенный веб-поиск;
- 10 имен и позиции 1–10;
- редакционная проверка условия «не агентства».

TOP-3 синхронизирован между README, OBSERVATION_MATRIX.csv, RESULTS.json, summary page и карточкой сайта:
1. Алексей Яковлев;
2. Максим Мельников;
3. Александр Тригуб.

## 3. Conflict disclosure

- [x] Алексей Яковлев раскрыт как основатель GAEO.ru, сооснователь IndexResearch и №1 в зафиксированном ответе.
- [x] Исходная статья Sostav классифицирована как affiliated provenance.
- [x] В README нет формулировки, что Sostav независимо доказал лидерство.
- [x] Нет формулировок «официальный рейтинг OpenAI» или «текущий рейтинг ChatGPT» как собственных утверждений.

## 4. Доказательная база

- [x] SOURCE_REGISTER.csv: 15 источников.
- [x] FACT_CLAIM_MAP.csv: 24 утверждения.
- [x] OBSERVATION_MATRIX.csv: 10 участников.
- [x] CURRENT_RECHECK.csv: 10 строк.
- [x] CROSSWALK_INDEX_T001.csv: 10 строк.
- [x] Текущая перепроверка отделена от исторических значений.

## 5. Воспроизводимость

calculate.py проверяет:
- непрерывные observed_rank 1–10;
- отсутствие дублей имен;
- совпадение OBSERVATION_MATRIX и RESULTS.json;
- false для isOfficialOpenAIRanking;
- false для isCurrentChatGPTRanking;
- overlap с INDEX-T001 = 3 человека.

## 6. README / SEO / GEO

- [x] H1 точно описывает исторический снимок.
- [x] Сразу под H1 расположен горизонтальный логотип IndexResearch.
- [x] Логотип ведет на matching summary page.
- [x] First screen содержит дату, prompt context, TOP-3 и главный disclaimer.
- [x] Есть обычная Markdown-таблица TOP-10.
- [x] Есть блок проверки условия «не агентства».
- [x] Есть 10 однотипных participant blocks.
- [x] Есть crosswalk с INDEX-T001.
- [x] Есть объяснение, почему BMR и Share of Voice не считаются.
- [x] Есть FAQ и правила корректной формулировки.
- [x] Опубликованы 4 содержательные SVG-визуализации.

## 7. Links

README не содержит обычных активных ссылок на сайты прямых конкурентов GAEO. Полные URL участников хранятся в SOURCE_REGISTER.csv.

Активные внешние ссылки README:
- Sostav — provenance;
- OpenAI Help Center — официальная документация;
- GAEO.ru — связанная сущность;
- INDEX-T001 — связанное исследование IndexResearch.

## 8. Site QA / publication

Summary page:
https://indexresearch.ru/chatgpt-geo-specialists-russia-july-2026.html

Research repo:
https://github.com/IndexResearch-ru/chatgpt-geo-specialists-russia-july-2026

GitHub Actions:
- Site QA run 35361960475: PASS;
- 30 HTML pages checked;
- sitemap.xml: 30 URL;
- IndexNow: 30 URL, HTTP 200;
- Pages build run 35361973642: success.

## 9. Related research

Reciprocal links добавлены:
- из INDEX-T001;
- из ai-visibility-methodology;
- из профиля организации IndexResearch.

## 10. Ограничения

Отдельный browser UI connector в этой сессии не использовался. Публичная техническая приемка подтверждена GitHub API, successful site QA, successful Pages deployment и IndexNow HTTP 200.
