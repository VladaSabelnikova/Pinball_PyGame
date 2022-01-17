### Лицей Академии Яндекса
#### Основы промышленного программирования
#### Москва - 1560 - 1 - Д2
#### Сабельникова Влада Яновна
#### Селиванова Александра Васильевна
# Motley Pinball
### Проектная работа № 2 PyGame

### Постановка задачи
Написать игру, в которую захочется сыграть даже после защиты проекта и не только авторам.

### Логика игры
Игра Motley Pinball. 

В игре есть:

1. Мяч, движущийся по законам физического мира (запас мячей на игру — 3 штуки)


2. Три банки с красками, которые нужно сбить мячом.


3. Одна лунка. Попадая в неё мячик теряется.


4. Две доски с регулируемой силой удара для отбивания мяча.


5. Препятствия, мешающие движению мяча.

###
#### Задача:

Отбивая мяч досками не попасть мячиком в лунку и разбить все банки.

Выигрыш — все банки разбиты (о принципе подсчета очков ниже).

Проигрыш — Не все банки разбиты, а запас мячей иссяк.

###
#### Как играть:

Нажатием на левый или правый CTRL вы поднимаете соответствующую доску.

Нажатием на стрелку вверх или вниз вы изменяете силу взмаха доски
(шкала силы будет справа внизу при запуске игры)


###
#### Принцип подсчета очков:

Очки начисляются по сложной формуле. Логика формулы такова:

Нужно сбить все банки за минимальное время, минимальным кол-вом мячей
с минимальной силой взмаха доски. 

Т.е вы будете набирать меньше очков если:

1. Будете увеличивать силу взмаха доски


2. Будете терять мячи в лунке


3. Будете тратить много времени на игру

Ваши очки сохраняются на диске в обычном txt файле,
однако они зашифрованы и подделать их будет не просто.

###
### Принцип работы программы

Для запуска из корневой папки программы введите:

      $ python main.py

В появившемся окне есть три кнопки, каждая из которых — отдельный уровень игры:
1. Тренировка
2. Игра
3. NIGHTMARE

###
#### Уровень Тренировка:
Для того, что бы ознакомится с интерфейсом и "пощупать" игру — нажмите "Тренировка".
С небольшой гравитацией вы сможете понять принцип работы игры.
Баллы за этот уровень не начисляются, он нужен для ознакомления.

###
#### Уровень Игра:
Если вы уже поняли принцип работы и готовы набирать очки — нажимайте "Игра"!

С нормальной гравитацией, дополнительными препятствиями и классной музыкой вы будете 
набирать очки за каждый выигрыш!

###
#### Уровень NIGHTMARE:
Если вы уже профи и вам скучно на уровне "Игра" — добро пожаловать на хардкор!
Сразу предупреждаем — выиграть не просто,
мы расставили дополнительные препятствия и еще увеличили гравитацию!

Соответственно очки так же начисляются за каждый выигрыш.

### Используемые технологи
1. Стартовое окно


2. Финальное окно


3. Подсчет результатов


4. Спрайты


5. Работа со столкновениями collide


6. Анимация


7. Несколько уровней
   * Тренировка
   * Игра
   * NIGHTMARE


8. Хранение зашифрованных очков в txt


9. Шифрование и дешифрование набранных очков.


10. Формирование workflow и работа с git и github


11. requirements.txt


12. Использование пакетов


### Перспективы дальнейшего развития
1. Улучшение графики и анимации


2. Разработка новых уровней


3. Реализация многопользовательской версии с сетевым хранилищем (базой данных)
и получение обратной связи от пользователей,
а так же совершенствование функционала и интерфейса.