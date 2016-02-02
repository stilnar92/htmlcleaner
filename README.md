# htmlcleaner

<p> Утилита позволяющая «вытащить» из веб-страницы только полезную информацию, отбросив весь «мусор» (навигацию, рекламу и тд).</p>

<h2>Установка</h2>

<pre>
<code>git clone https://github.com/stilnar92/htmlcleaner.git
pip install -r requirements.txt
</code>
</pre>

<h2>Запуск</h2>

<pre><code>python htmlcleaner.py &lt;url&gt;
</code></pre>

<p>Тестовые запуски проводились на следующих адресах:</p>

<pre><code>
    https://medium.com/life-tips/multitasking-is-killing-your-brain-79104e62e930#.cctxppb58
    http://www.bbc.com/russian/blogs/2016/01/160127_blog_strana_russia_border_control
    http://lenta.ru/news/2016/02/02/alphabet/
    http://www.machinalis.com/blog/full-text-search-on-django-with-database-back-ends/
    http://ufa.rbc.ru/ufa/freenews/56af038d9a79472cf43b7b0a?from=main
    http://pythondigest.ru/issue/110/
</code></pre>



<h2>Алгоритм</h2>
<p>1. Получаем содержимое страницы.</p>
<p>2. Находим все блочные элементы. </p>
<p>3. В каждом блочном элементе считаем количество тегов. Таких как p,h1,h2. </p>
<p>4. Находим блочный элемент с найбольшим количеством тегов. </p>
<p>4. Записываем в список. </p>
<p>5. Выполняем выше описанные действия до тех пор пока не найдем блочный элемент который  не содержит блочных элементов. </p>
<p>6. Берем последний элемент в списке. Находим количество тегов. Запомним это значеник как минимальное количество тегов.
<p>7.Проходим по списку с конца считая количество тегов в каждом элементе. Выбираем тот который удовлетворяет условию: Количество тегов в элементе меньше минимального количества тегов + EPS. EPS - погрешность.










<h2> Стратегия развития утилиты</h2>

<p></p>

<p></p>

<p></p>

<p></p>

<p></p>
</article>
