import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd
from math import pi
import re
import plotly.graph_objs as go
import os

excel_data = pd.read_excel('grade_history .xlsx')
data = pd.DataFrame(excel_data)
all_us = data['Название'].unique()
all_event = data['Элемент оценивания'].unique()
# блок обработки данных
def edit( data = data):
    # сначала очищаются данные от не нужных стобцов
    data.drop(columns=['Адрес электронной почты','Исходная оценка', 'Оценщик', 'Источник', 'Переопределена', 'Заблокировано', 'Исключено из вычислений', 'Текст отзыва'],inplace=True)
    for i in data['Дата и время']:
        new_d = i.split()
        a = new_d[2]
        if 'сентябр'in a:
            a = '09'
        elif 'октябр'in a:
            a = '10'
        elif 'ноябр'in a:
            a = '11'
        elif 'декабр'in a:
            a = '12'
        elif 'январ'in a:
            a = '01'
        elif 'феврал'in a:
            a = '02'
        elif 'март'in a:
            a = '03'
        elif 'апрел'in a:
            a = '04'
        elif 'ма'in a:
            a = '05'
        b = f'{new_d[3][:-1:]}-{a}-{new_d[1]}'
        data = data.replace(i , b)
        # Теперь изменяют тип данных для работы со временм
    data['Дата и время'] = data['Дата и время'].astype("datetime64[ns]")

    for grade in data['Исправленная оценка'].dropna():
        b = grade.replace(',', '.')
        data = data.replace(grade, b)
    data['Исправленная оценка'] = data['Исправленная оценка'].astype("float")
    return data
data = edit(data)
def work( user, event, iter, data=data):
    date_start = pd.Timestamp('2022-09-01')
    max_score = {}
    for j in event:
        a = data[data['Элемент оценивания'] == j]
        max_score[j] = max(a['Исправленная оценка'])

    for month in range(3, 9):
        ndata = data.loc[(data['Дата и время'] < date_start + pd.DateOffset(months=month))]

        ts = {}
        sum_p = 0
        for numb, i in enumerate(all_us):
            ts2 = {}

            # обрабатываем все элементы в файле для сбора нужных оценок
            for j in event:
                a = ndata[ndata['Элемент оценивания'] == j]
                masiv = a
                a = a.dropna()
                if len(a['Исправленная оценка']) == 0:
                    max_grade = 0.0
                else:
                    max_grade = max(a['Исправленная оценка'])
                a = a[a['Название'] == i]
                if len(a['Исправленная оценка']) != 0:
                    a = a[a['Исправленная оценка'] == max(a['Исправленная оценка'])]
                    point = max(a['Исправленная оценка'])
                else:
                    point = 0
                if point != 0:
                    point = point / max_score[j]
                ts2[j] = [point]
            ts[i] = ts2
        # то что выше надо переделать для всех элементов которые подаются в файле
        df = pd.DataFrame(ts)
        # print( '----------')
        cat = df.columns
        # Рассчитываем среднее значение
        avg_sum = 0
        val_avg = []
        for ran in ts:
            val_avg = [0.0] * len(ts[ran])
            break
        deli = 0
        for kol2, avg_i in enumerate(ts):
            ar = [0] * len(ts[avg_i])
            for kol, _ in enumerate(ts[avg_i].keys()):
                ar[kol] += ts[avg_i][_][0]
            val_avg = list(map(sum, zip(val_avg, ar)))
        val_avg = list(map(lambda x: x / kol, val_avg))

        max_rat = []
        for ran in ts:
            max_rat = [0.0] * len(ts[ran])
            break
        # расчитываем макс оценку -->
        for kol2, us in enumerate(ts):
            arr = [0] * len(ts[us])
            for kol, _ in enumerate(ts[us].keys()):
                arr[kol] = ts[us][_][0]
            max_rat = list(map(max, zip(max_rat, arr)))
        # Блок визуализации, он проходит циклом по каждому пользователю
        vis = []
        res = []
        for kol23, ap_i in enumerate(ts):
            if ap_i == user[0]:
                values = []
                cat = list(ts[ap_i].keys())
                avg_sum = 0
                for kol, _ in enumerate(ts[ap_i].keys()):
                    qvo_sum = ts[ap_i][_][0]
                    values.append(ts[ap_i][_][0])

                fig = go.Figure()
                print('val avg', val_avg)
                print('cat', len(cat), cat)
                print('values', values)
                # print('max_rat', max_rat)
                # Выбирается что именно будет отображаться на визуализации(среднее значение, максимальное)
                if len(cat) < 5:
                    fig = go.Figure(data=[go.Bar(
                        name='среднее',
                        x=cat,
                        y=val_avg
                    ),
                        go.Bar(
                            name=ap_i,
                            x=cat,
                            y=values
                        )
                    ])
                else:
                    values.append(values[0])
                    max_rat.append(max_rat[0])
                    val_avg.append(val_avg[0])
                    cat.append(cat[0])
                    fig.add_trace(go.Scatterpolar(r=val_avg, theta=cat, fill='toself', name='среднее'))
                    fig.add_trace(go.Scatterpolar(r=values, theta=cat, fill='toself', name=ap_i))
                    # fig.add_trace(go.Scatterpolar(r=max_rat, theta=cat, fill='none', name='макисмальное значени'))
                    fig.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 1])), showlegend=True)
                vis.append(fig)

                for figure, figure_num in enumerate(vis):
                    figure_num.write_image(f"source/img_{ap_i}-{month}-{iter}.png")
                    res.append(figure_num)
        vis = []

def get_event():
    return sorted(list(all_event))
def get_user():
    return sorted(list(all_us))


# work( ['Лабораторная работа 6.', 'Лабораторная работа 3.', 'Лабораторная работа 4.',
# 'Лабораторная работа 5.', 'Тест 2.', 'Тест 1.', 'Лабораторная работа 2.', 'Лабораторная работа 1.'], 1)


