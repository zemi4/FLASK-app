from flask import Flask, render_template
from parsing_currency import *
from parsing_afisha2 import *
from parsing_weather import *


app = Flask(__name__)


@app.route('/')
def courses():

    return render_template('currency.html', E=get_money_euro(), U=get_money_usd(), R=get_money_rus(), A=get_money_aud(),
                           B=get_money_bgn(), UH=get_money_uah(), D=get_money_dkk(), P=get_money_pln(),
                           I=get_money_irr(), IS=get_money_isk())


@app.route('/movies/')
def movies():

    return render_template('kino.html', afis_text0=main_afisha0(), afis_img0=img0(),
                                        afis_link0=link0(),
                                        afis_text1=main_afisha1(), afis_img1=img1(), afis_link1=link1(),
                                        afis_text2=main_afisha2(), afis_img2=img2(), afis_link2=link2(),
                                        afis_text3=main_afisha3(), afis_img3=img3(), afis_link3=link3(),
                                        afis_text4=main_afisha4(), afis_img4=img4(), afis_link4=link4(),
                                        afis_text5=main_afisha5(), afis_img5=img5(), afis_link5=link5(),
                                        afis_text6=main_afisha6(), afis_img6=img6(), afis_link6=link6(),
                                        afis_text7=main_afisha7(), afis_img7=img7(), afis_link7=link7(),
                                        afis_text8=main_afisha8(), afis_img8=img8(), afis_link8=link8(),
                                        afis_text9=main_afisha9(), afis_img9=img9(), afis_link9=link9(),
                                        afis_text10=main_afisha10(), afis_img10=img10(), afis_link10=link10(),
                                        afis_text11=main_afisha11(), afis_img11=img11(), afis_link11=link11())


@app.route('/weather/')
def weather():

    return render_template('weather.html', weat3=Weather_3_hours(), weatday=Weather_day(), weat3temp=Weather_3_temp(),
                           weattemp=Weather_temp())


if __name__ == '__main__':
    app.run(debug=True)
