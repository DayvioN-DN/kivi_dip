# Дипломная работа 
Данное приложение создано для визуализации данных из среды обучения Moodle.
На основе данных постпающих из данных производится обработка данных и привидение обрабатываемому виду и после, на основе выбранных пользователей и отображаемых параметров строится дашборд, данные которого можно скачать, сохранить и использовать снова.  
  
grade_history .xlsx - пример датасета где хранятся данные, в такой форме и должны отправляться с системы обучения для их обработки  
obrabot.py - обрабатываются дасеты а именно: изменяются виды даты для её преобразования в тип данных обрабытываемый pandas (datetime64), убираются пропуски в числах, данные по оценкам приводятся к типу float и в дальнейшем фильтруются по месяцу и визуализируются по нему же.  
priloj.py - создаётся интерфейс для пользователя и выводятся данные  
requirements.txt - билиотеки требуемые для работы 
