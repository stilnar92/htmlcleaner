# htmlcleaner

<p> Утилита позволяющая «вытащить» из веб-страницы только полезную информацию, отбросив весь «мусор» (навигацию, рекламу и тд).</p>

<h2>Язык программирования</h2>
<p>Python 3.4.3</p>
<h2>Установка</h2>

<pre>
<code>
git clone https://github.com/stilnar92/htmlcleaner.git
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv htmlcleaner
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
<ul>
<li>Находим все  div элементы. </li>
<li>В каждом div элементе считаем количество тегов. Такие как p,h1,h2. </li>
<li>Находим div  элемент с найбольшим количеством тегов. </li>
<li>Записываем в список. </li>
<li>Выполняем выше описанные действия до тех пор пока не найдем <div> элемент который  не содержит других <div> элементов. </li>
<li>Берем последний элемент в списке. Находим количество тегов. Запомним это значение как минимальное количество тегов.</li>
<li>Проходим по списку с конца считая количество тегов в каждом элементе списка. Выбираем тот который удовлетворяет условию: <ul><li>Количество тегов в элементе списка меньше минимального количества тегов + EPS.</li></ul>EPS - погрешность.</li>
</ul>

<h2>settings.py</h2>
<p>Настройки для изменения  результата.</p>
<p>Изменить результат можно</p>
<ul>
<li> Уменьшив значение DEEP.</li>
<li>Установив значение TEXT в True.</li>
<li>Добавляя теги в tags_settings.</li>
</ul>
<p>Настройки по умолчанию</p>
<pre>
# Режим поиска True - Искать текст. False - искать теги

TEXT = False

# Глубина поиска 
DEEP = 100
# Теги для поиска
tags_settings = {
                 'h1' : True,
                 'h2' : True, 
                 'h3' : True, 
                 'h4' : True, 
                 'p' :  True,
                 'pre': True,
                 'li':  True,
                 'a':True,
}
# Показывать ссылки в тексте
URL = True
</code>
</pre>
