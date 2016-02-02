# htmlcleaner
<h1>Тестовое задание для компании Tensor</h1>

<h2>Установка</h2>

<pre>
<code>git clone https://github.com/stilnar92/htmlcleaner.git
virtualenv /path/to/envs/directory
pip install -r requirements.txt
</code>
</pre>

<h2><a id="user-content-Запуск" class="anchor" href="#Запуск" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" role="img" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Запуск</h2>

<pre><code>python main.py &lt;url&gt;
</code></pre>

<p>Результат в каталоге results. Тестовые запуски проводились на следующих адресах:</p>

<pre><code>python main.py http://66.ru/news/internet/172721/
python main.py http://www.f1news.ru/news/f1-103942.html
python main.py http://lenta.ru/news/2015/06/01/ukraune/
</code></pre>

<h2><a id="user-content-Задание" class="anchor" href="#Задание" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" role="img" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Задание</h2>

<p>«Вытащить» из веб-страницы только полезную информацию, отбросив весь «мусор» (навигацию, рекламу и тд).</p>

<h2><a id="user-content-Концепция-решения" class="anchor" href="#Концепция-решения" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" role="img" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Концепция решения</h2>

<p>Т.е. условия выполнения задания запрещают использование синтаксических анализаторов, решено было разбирать html 
и по косвенным признакам понять, какой контент важен, а какой - нет
Принята была следующая концепция:
При посещении нескольких сайтов было замечено, что весь значимый контент хранится либо в нескольких последовательных тегах,
например:</p>

<pre><code>&lt;p&gt;Paragraph first&lt;/p&gt;
&lt;p&gt;Paragraph second&lt;/p&gt;
&lt;p&gt;Paragraph third&lt;/p&gt;
</code></pre>

<p>Либо в одном теге, но с разделением, например таким:</p>

<pre><code>&lt;div id="content"&gt;
    Paragraph first
    &lt;br&gt;
    Paragraph second
    &lt;br&gt;
    Paragraph third
&lt;/div&gt;
</code></pre>

<p>Т.е. задача сводится к тому, что бы между списком тегов с параграфами или одним контейнером с большим текстом внутри
выбрать то, что мы считаем приоритетным. Выбор основывается на гипотетической системе оценок.
Два главных параметра для оценки "важности" - количество повторяющихся тегов и кол-во знаков внутри отдельного тега.
Для гибкости эти параметры вынесены в настройки (подробнее чуть ниже).</p>

<p>Так-же подразумевается, что важный контент не может быть разбросан на разных уровнях html дерева, по этому так-же введен 
параметр который определяет минимальное отношение баллов для контента на разных уровнях. Например, есть следующий html:</p>

<pre><code>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Some title&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;div&gt;
            &lt;p&gt;Paragraph first&lt;/p&gt;
            &lt;p&gt;Paragraph second&lt;/p&gt;
            &lt;p&gt;Paragraph third&lt;/p&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;div&gt;
                &lt;p&gt;Some very very long text&lt;/p&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;
&lt;/html&gt;
</code></pre>

<p>Имеют место два гипотетических места сосредоточения контента:
1. Три параграфа (уровень вложенности = 4)
2. Большой параграф (уровень вложенности = 5)</p>

<p>Используя коэфициенты <code>content_level_score</code> (множитель баллов за несколько параграфов-соседей на одном уровне) и 
<code>content_char_score</code> (множитель баллов за каждый отдельный символ внутри отдельно взятого параграфа) 
будут оценены эти два места.
Допустим, место (1) получило 100 условных баллов, место (2) получило 59 условных баллов. 
В <code>config.ini</code> имеется параметр <code>min_group_score_percents=60</code>, который говорит о том, что в выдачу попадут только те места,
кол-во баллов которых &gt;=60% от кол-ва баллов места, которому выдано максимальное кол-во баллов. 
Таким образом при текущем коэфициенте==60 место (2) не попадет в выдачу.</p>

<p>Так-же, имеется параметр <code>content_tags</code>, который регламентирует список тегов, в которых может быть искомый контент</p>

<p>В условиях ограниченного кол-ва времени на выполнение тестового задания мусора всё-же получается не мало, 
но я и не заявляю, что утилита закончена и полностью работаю.</p>

<h2><a id="user-content-Стратегия-развития-утилиты" class="anchor" href="#Стратегия-развития-утилиты" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" role="img" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Стратегия развития утилиты</h2>

<p>Во первых, для более "точного" попадания в контент необходимо точнее детализировать селекторы, тут я вижу 2 стратегии:</p>

<p>Попроще: при каждом запуске уточнять селектор, возможно с использованием class и id (css selectors), возможно так:
<code>python main.py &lt;url&gt; --selector=p.some-class&gt;div#content</code></p>

<p>Посложней: Вести базу данных (возможно, удалённо) по каждому используемому порталу. При запуске парсинга 
утилита смотрит в базу и для этого сайта получает "best practice" селекторы для текущего сайта и в первую очередь ищет
контент там, где его рекомендует искать наша база с рекомендуемыми коэфициентами.</p>

<p>Во вторых, необходимо вырезать javascript, для более чистого прасинга</p>

<p>В третьих (если нужна производительность), "починить" сложные места: во первых, разбивка строк по длине, 
во вторых - html сейчас разбирается не как xml, а как html, что дольше</p>
</article>
