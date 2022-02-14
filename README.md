# object-recognition

Проект <b>train.ipynb</b> предназначен для обучения, а проект <b>detect.ipynb</b> для распознования объектов.
Модели:
<ui>
<li>
cars_birds_trees_weights.h5
</li>
<li>
cars_birds_trees_weights(1).h5
</li>
<li>
cars_birds_trees.h5
</li>
<li>
cars_birds.h5
</li>
<li>
cars_birds_trees(1).h5
</li>
<li>
cars_birds_trees_weights(2).h5
</li>
<ui>
это обученные мной модели. Самой точной на данные момент из них является модель <b>cars_birds_trees_weights(2).h5</b>. Обучение проводил с нескольками тысячами картинок. Библитотека tensorflow keras. 

___

В проекте <b>Object_detected.py</b> есть 3 режима. Для переключения между режимами надо изменять переменную mode в коде. Данный проект уже использует обученную модель. Это модель была обучена кем то на несколько объектов. В проекте использовался библиотека OpenCV.
Запуск проекта через терминал командой: <b>python Object_detected.py</b>

<ui>
<li>
0 режим: Распазнает одну картинку. Картина указыается в переменой <b><i>imageName</i></b>. Дальше после запуска получим новую картинку в распознанном формате.
</li>
<li>
1 режим: Запускает видеокамеру и в режиме реального времени распознает объеты.
</li>
<li>
2 режим: Принимает несколько картин и распознает объекты в них. Дальше складывает распознанные и не распозннанные объекты в папку <b>sortedImg</b>. Папка указывается в переменной <b><i>imagesFolderURL</i></b>
</li>
</ui>



