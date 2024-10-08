## *Команды проверки*

* Проверка имени/почты
```sh
git config user.name
git config user.email
```

* Проверка файлов: 
```sh
git status
```

* Просмотр коммитов (версия): 
```sh
git log
```

* Укорачивание записи версий: 
```sh
git log --oneline
```

* Визуализация веток: 
```sh
git log --graph
```

* Отличие папки от последнего коммита: 
```sh
git diff
```

* Отличие двух версий: 
```sh
git diff num1 num2
```

## *Порядок добавления нового в гит*

1. Проверка файлов: 
```sh
git status
```

2. 1. Добавление одного неотслеживаемого файла: 
```sh
git add file_name\ with\ space.format
```

2. 2. Добавление всех неотслеживаемых файлов: 
```sh
git add .
```

3. Добавление комментария к сохранению: 
```sh
git commit -m ""
```

## *Слияние веток*

1. ```git checkout master ```- переход на основную ветку
2. ```git merge branch_name ```- вливаемая в основную ветка
3. нажать esc и ввести ```:wq ```- если открывается редактор (нет конфликтов)
4. принять либо отклонить изменения - если подсвечивается код (если есть конфликт)
5. 

## *Прочие команды версий*

* Добавление файла в игнор: 
```sh
git commit -m ""
```

* Откат версии: 
```sh
git checkout num_ver
```

* Возврат к последней версии: 
```sh
git checkout master
```

* Проверка текущей ветки и всех: 
```sh
git branch
```

* Создание новой ветки: 
```sh
git branch new_name
```

* Безопасное удаление ветки (метки): 
```sh
git branch -d name
```

* Ультимативное удаление ветки (метки): 
```sh
git branch -D name
```

* Переход на ветку: 
```sh
git checkout branch_name
```

* Откат версии файла до предыдущего коммита: 

```sh
git restore
```

>**! ! ! ВАЖНО ! ! !**
>>При добавлении изменений между add и commit при
повторном add вносятся текущие изменения, а при
commit - только добавленные ранее