from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField, SubmitField, RadioField
from wtforms.validators import InputRequired, DataRequired

class MyForm(FlaskForm):
    distr = SelectField('Район', choices=[("6", "Подол"),  ("4", "Оболонь"), ("9", "Святошино"), ("7", "Шевченковский"), ("8", "Соломенский"),
                                           ("5", "Печерск"), ("3", "Голосеево"), ("0", "Дарница"), ("2", "Днепровский"), ("1", "Деснянский"),], validators=[InputRequired()])
    rooms=RadioField("Количество комнат", choices=[('1','1'), ('2','2'),('3','3'), ('4','4'), ('5','5')], validators=[DataRequired()])
    state = SelectField('Состояние',choices=[("1","Евроремонт"), ("4","Хорошее состояние"),("0","Требуется косметичесий ремонт"),
                                                  ("6","Удовлетворительное"), ("3","От застройщика(свободная планировка)")], validators=[InputRequired()])
    house_type = RadioField('Тип постройки', choices=[("2","Бетонномонолитный"), ("5","Типовая панель"),("1","Дореволюционный")], validators=[InputRequired()])

    square_min=DecimalField("Общая площадь", validators=[InputRequired()])
    square_max = DecimalField("Жилая площадь", validators=[InputRequired()])
    submit = SubmitField('Отправить')


