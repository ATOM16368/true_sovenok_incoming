init:

    $ mods["Misha_technar"]=u"название сам придумай"

    $ ambience_rain = "mods/Mod_1/music/rain.mp3"

    image ext_domik_mishi_day = "mods/Mod_1/images/house_of_misha_day.jpg"
    image int_domik_mishi = "mods/Mod_1/images/int_house_of_misha.jpg"

label Misha_technar:
    $ persistent.sprite_time = "day"
    $ day_time()
    define hui = Character('Миша', color="#c8ffc8")
    play music music_list ["a_promise_from_distant_days"] fadein 1.5
    scene bg semen_room with dissolve
    "Меня зовут Миша.{w} мне 17 лет."
    "Ничего особенного, учусь на втором курсе технаря и больше ничем не занимаюсь."
    "Родители снимают мне квартиру, чтобы я жил один."
    "Все своё свободное время провожу за играми."
    "Бесконечное лето - мой фаворит. Эта история меня поражает! Как человек, похожий на меня, смог нормально адаптироваться в обществе."
    "Мечта каждого фаната бескончного лета - попасть в совёнок, ну а там каждый выберет для себя развлечение."
    "Я конечно хочу пройтись по самому лагерю, посмотреть его красоту, красоту настоящего лета, ведь у нас все только серое и нудное."
    "Так какового фаворита в женском персонаже у меня нет, но провести счастливую смену хотя бы с одной хочу."
    "Но это всего лишь мечты..."
    show blink
    $ renpy.pause(1.3)
    th "Надо ложиться спать, ведь завтра к первой паре и там сидеть еще 4."
    stop music fadeout 1.5
    $ renpy.pause(1.5)
    hide blink
    scene bg int_bus_night
    play music music_list ["lightness_radio_bus"] fadein 1.5
    show unblink
    "Лунный свет и тряска разбудили меня."
    "Я сидел на пасажирском месте в автобусе, который ехал куда-то."
    "За окном простилались бескончные поля."
    "Я осмотрел салон, в конце кто-то сидел."
    "Подойдя к нему, я заметил, что его глаза закрыты."
    th "Наверное спит."
    "Подёргав за плечо, он не обращял внимание."
    "Подойдя к месту модителя, я заметил, что на его месте никого нет, нас везла неведомая магия."
    th "И что же делать?"
    "Я еще раз попытался разбудить своего попутчика, но все без результатно."
    "Ничего не решив, я просто сел обратно и просто смотрел в окно."
    th "Красиво тут."
    "В сон клонило само, и я решил закрыть глаза."
    show blink
    $ renpy.pause(1.3)
    stop music fadeout 1.5
    $ renpy.pause(1.5)
    hide blink
    scene bg int_bus
    play music music_list ["no_tresspassing"] fadein 1.5
    show unblink
    "Проснувшись, я уже не ехал, и за окном был день."
    "Быстро встал и осмотрелся, человека на заднем ряду не было, что за магия, а водителя как и не было, так и не появился."
    "Были открыты двери и я вышел."
    scene bg ext_camp_entrance_day with dissolve
    "Что я увидел не поддаётся объяснению, настоящий Совенок."
    hui "Неужели я тут?"
    scene bg ext_bus with fade
    $ renpy.pause(0.2)
    scene bg ext_camp_entrance_day with fade
    "Посмотрев назад я убедился, что там стоял тот самый 410 Икарус прям из игры."
    stop music fadeout 2.5
    th "Так, ну сейчас должна будет выйти Славя.."
    $ renpy.pause(2.5)
    th "А ну, сам лучше все посмотрю."
    scene bg ext_clubs_day with dissolve
    play music music_list ["everyday_theme"] fadein 2
    "Пройдя ворота я увидел здание кружков."
    show un scared pioneer with dissolve
    show us laugh sport at left with dissolve
    show pi normal pioneer at right with dissolve
    "У дверей как и положено стояла Лена и Ульянка с сверчком, но на против них стоял кто-то, а это же тот из автобуса, но... стоп."
    hide us with moveoutleft
    hide un with moveoutleft
    show pi at center with moveinleft
    "Когда я подошел к дверям кружка, Лена и Ульяна ушли, но эта персона так же стояла на своем месте."
    hui "Привет, а ты кто?"
    me "Ой, привет, меня Семёном звать."
    "Чего? Семён? Одкуда и почему?"
    "Не дав мне спросить, он сказал"
    me "Мне пора."
    hide pi with moveoutright
    "И ушёл."
    th "Так стоп, какой к чертям Семён?"
    th "Почему он тут, если я тут, то я же должен быть тут один."
    th "Это получается не моя смена теперь, раз уж тут есть свой Семён."
    show el normal pioneer at cleft with dissolve
    show sh normal pioneer at cright with dissolve
    "Пока я размышлял из клуба вышел Электроник и Шурик."
    el "О, новенький? Меня Электронником звать, вот это Шурик. Как насчет того, что бы вступить в наш клуб, мы тут роботов сторим и..."
    hui "Нет, извините, я посмотрю другие кружки, если не найду ничего интересного, то пулей к вам сразу."
    el "Заметано."
    show sh serious pioneer
    sh "Тебе же к Ольге Дмитриевне нужно, тебе показали, где её домик? Может проводить тебя?"
    hui "Да не надо, сам как-нибудь разберусь."
    sh "ну ладно."
    hide sh with dissolve
    hide el with dissolve
    scene bg ext_square_day with fade
    "Я пошел к площади."
    "Конечно же я наврал им, я не имею никакого желания заниматься ротоботехникой, по мне, даже компания Жени будет интересней, чем эти двое."
    scene bg ext_houses_day with fade
    show dv normal pioneer2 far with dissolve
    "Проходя между домиками я закономерно увидел идущую мне на встречу Алису."
    show dv angry pioneer2 close with dissolve
    dv "Еще один. Новенький, да?"
    hui "И тебе привет."
    hide dv with  dissolve
    "Алиса лишь фыркнула и прошла мимо."
    scene bg ext_square_day
    "И вот я на площади, если мне не изменяет память, по канону сечас настоящий Семён на пристани, значит я могу прийти к Ольге первым."
    scene bg ext_house_of_mt_day with dissolve
    stop music fadeout 2
    "Дойдя быстрм шагом я постучался в дверь."
    play sound sfx_knock_door2
    mt "Войдите."
    play music music_list ["take_me_beautifully"] fadein 2
    scene bg int_house_of_mt_day
    "Зайдя, я заметил, что в домике кроме Ольги не было никого и сама она сидела за столиком и читала."
    show mt surprise pioneer with dissolve
    mt "Новенький?"
    show mt normal with dissolve 
    hui "Да. Зовут Миша."
    show mt smile with dissolve 
    mt "Да, меня зови Ольгой Дмитриевной. Так, надо поселить тебя куда-то. А вот нашла, придеться тебе одному побыть."
    hui "Да, переживу."
    mt "Так, но как ты дойдешь? хмм. Садись, скоро Славя подойдет, покажет тебе, кстати, она тебя встретила?"
    hui "Нет."
    show mt surprise with dissolve
    "Ольга Дмитриевна подняла брови."
    mt "Ну ладно, поговорю с ней."
    hide mt with dissolve
    "И дальше уткнулась в свою книжку."
    "Как мне помнится Ольга должна покричать на Улю, а потом уже прийдут Славя с Семёном."
    $ renpy.pause(1.5)
    "И сидели мы так долго или мне просто казалось, пока в дверь не постучались."
    play sound sfx_knocking_door_outside
    show mt normal pioneer at right with dissolve
    mt "Войдите."
    show sl normal pioneer with moveinleft
    show pi normal pioneer at left with moveinleft 
    "В дверь зашли Семён и Славя."
    show sl shy pioneer with dissolve
    sl "Ой, ты же новенький, извини, что не встретила, дел по горло было, меня кстати Славя зовут."
    show sl normal with dissolve
    hui "Меня Миша."
    sl "Но, как вижу ты сам нашел путь и пришел, Ольга Дмитриевна я вот вам другого новенького привела."
    show mt smile at right with dissolve
    mt "Вижу, ты кстати сходи ка с Мишей до его домика, 31."
    sl "Ладно."
    show sl smile with dissolve
    sl "Пойдем.."
    "Обратилась она ко мне."
    hui "Да."
    hide mt with dissolve
    hide pi with dissolve
    hide sl with dissolve
    "Я встал и Ольга в след сказала."
    mt "Если что-то случится спрашивай у меня или у Слави."
    stop music fadeout 1
    play ambience ambience_day_countryside_ambience fadein 1
    scene bg ext_house_of_mt_day
    "Мы вышли."
    show sl normal pioneer with dissolve
    sl "Так, 31 - это же в другой части лагеря, далекова то будешь от вожатой жить, ну пошли, дорога далёкая."
    scene bg ext_houses_day with dissolve
    "Всю дорогу мы шли молча."
    scene ext_domik_mishi_day with dissolve
    "И вот пришли."
    "Славя открыла двери ключем, который дала Ольга, отдала его мне и мы вошли."
    stop ambience
    scene int_domik_mishi with fade
    "На вид обычный пустой домик."
    show sl normal pioneer with dissolve
    sl "За постельным сходишь в склад, он за столовой, а одежда должна в шкафчике быть."
    "Славя открыла шкаф и там висела пионерская форма."
    sl "Вот. Ну распологайся, если что подойдешь ко мне и спросишь, я везде по лагерю хожу, надеюсь найдёшь."
    hui "Ну ладно, спасибо."
    show sl smile pioneer with dissolve
    hide sl with dissolve
    "Славя улыбнулась и вышла."
    "Я плюхнулся на одинокий мотрас на кровати."
    th "Эх, почему мне грустно, я же попал в свою мечту, из-за того, что тут уже есть свой Семён?"
    th "Может быть, но не надо отчаиваться."
    "И только сейчас я осознал, что понятия не имею в какой одежде сейчас."
    "Я был в обычных джинсах и черной кофте."
    "Пошарив в карманах я ничего там не нашёл."
    th "Хмм. Обычно я так хожу на учёбу, а вдруг..."
    "Мои размышления прервал стук в дверь."
    hui "Вой.."
    "Не дав мне договорить дверь распахнулась."
    play music music_list ["i_want_to_play"] fadein 1
    show us smile pioneer with dissolve
    show dv normal pioneer2 at left with dissolve
    "Это оказались Ульяна и Алиса."
    show us surp1 pioneer with dissolve
    us "Вау, это же тот новенький."
    hui "Здравствуйте."
    show us grin pioneer with dissolve
    us "Смотри как официально, или он просто боится нас?"
    show dv smile pioneer2 with dissolve
    "Алиса усмехнулась."
    hui "Я вас обоих поприветсвовал."
    show us smile pioneer with dissolve
    us "Ага, а как нас зовут ты хоть знаешь?"
    hui "Ну и как?"
    "Фальшивил я."
    us "Ну меня Ульяна, а ее.."
    show dv normal pioneer2 at left with dissolve
    dv "Алиса я."
    "Перебила Ульяну Алиса."
    hui "Меня Миша."
    hide dv with dissolve
    hide us with dissolve
    "Быть в такой компании мне не то, что бы хотелось, но сейчас я хотел прогуляться."
    "Ульяна запрыгнула на соседную кровать и начала на ней прыгать, а Алиса села на стул."
    show us surp1 pioneer with dissolve
    show dv normal pioneer2 at left with dissolve
    us "Ничего себе ему повезло, один живёт."
    dv "Ага."
    stop music fadeout 2
    hui "Давайте выходить, я хотел лагерь посмотреть и все такое."
    show us sad pioneer with dissolve
    us "Скучный ты какой-то."
    hui "Ага."
    "Ульяна с неохотой спрыгнула и мы уже было подошли к выходу."
    "Как тут."
    play sound sfx_thunder_wood
    show dv scared pioneer2
    show us fear pioneer
    with hpunch
    $ renpy.pause(0.2)
    play music ambience_rain fadein 2 volume 0.7
    show us normal pioneer with dissolve
    show dv smile pioneer2 at left with dissolve
    $ renpy.pause(1.5)
    "Оглушающий звук и продолжение в виде множества ударов по крыше могли означать только одно-"
    show us surp1 pioneer with dissolve
    us "Дождь! На улице Дождь!"
    "Радостно воскликала Ульяна смотря в окно."
    show dv normal pioneer2 at left with dissolve
    "Алиса немного нахмурилась."
    dv "Нашла чему радоваться, как мы обратно в домик вернёмся, да еще и обед скоро."
    hide dv with dissolve
    hide us with dissolve
    "Но Ульяна не слышала ее слова и радостными глазами смотрела в окно за дождем."