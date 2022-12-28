from Models.User import User
import lightgbm as lgb
import pandas as pd


class UserController(object):
    user: User

    def __init__(self, user: User):
        self.user = user

    def get_predictions(self):
        credit_test = pd.DataFrame({'client_id': pd.Series(dtype='int64'),
                                    'gender': pd.Series(dtype='object'),
                                    'age': pd.Series(dtype='int64'),
                                    'marital_status': pd.Series(dtype='object'),
                                    'job_position': pd.Series(dtype='object'),
                                    'credit_sum': pd.Series(dtype='float64'),
                                    'credit_month': pd.Series(dtype='int64'),
                                    'tariff_id': pd.Series(dtype='float64'),
                                    'score_shk': pd.Series(dtype='float64'),
                                    'education': pd.Series(dtype='object'),
                                    'living_region': pd.Series(dtype='object'),
                                    'monthly_income': pd.Series(dtype='float64'),
                                    'credit_count': pd.Series(dtype='float64'),
                                    'overdue_credit_count': pd.Series(dtype='float64')})

        new_row = {}
        for col in credit_test.columns:
            new_row[col] = getattr(self.user, col)

        if self.user.living_region not in self.districts_map:
            new_row['living_region'] = list(self.districts_map.values())[0]
        if self.user.education not in self.education_list:
            new_row['education'] = 'SCH'
        credit_test.loc[0] = new_row.values()

        credit_test["living_region"] = credit_test["living_region"].astype("category")
        credit_test["tariff_id"] = credit_test["tariff_id"].astype("category")
        credit_test["job_position"] = credit_test["job_position"].astype("category")
        credit_test["marital_status"] = credit_test["marital_status"].astype("category")
        credit_test["gender"] = credit_test["gender"].astype("category")
        credit_test["education"] = credit_test["education"].astype("category")

        try:
            x_test = credit_test.drop('client_id', axis=1)
            gbm = lgb.Booster(model_file='static/models/model.txt')
            print(x_test)
            print(gbm.predict(x_test))
            prediction = gbm.predict(x_test)[0]
            return prediction
        except:
            return -1.0

    education_list = ['GRD', 'SCH', 'UGR', 'PGR', 'ACD']

    districts_map = {'ОБЛ МОСКОВСКАЯ': 'ОБЛ МОСКОВСКАЯ',
                     'КРАСНОДАРСКИЙ КРАЙ': 'КРАСНОДАРСКИЙ КРАЙ',
                     'САНКТ-ПЕТЕРБУРГ': 'САНКТ-ПЕТЕРБУРГ',
                     'Г САНКТ-ПЕТЕРБУРГ': 'САНКТ-ПЕТЕРБУРГ',
                     'МОСКВА': 'МОСКВА',
                     'МОСКОВСКИЙ П': 'МОСКВА',
                     'ТАТАРСТАН РЕСП': 'ТАТАРСТАН РЕСП',
                     'РЕСП БАШКОРТОСТАН': 'РЕСП БАШКОРТОСТАН',
                     'ОБЛ ИРКУТСКАЯ': 'ОБЛ ИРКУТСКАЯ',
                     'СВЕРДЛОВСКАЯ ОБЛ': 'СВЕРДЛОВСКАЯ ОБЛ',
                     'МОСКВА Г': 'МОСКВА',
                     'ОБЛ НИЖЕГОРОДСКАЯ': 'ОБЛ НИЖЕГОРОДСКАЯ',
                     'ОБЛ ЛЕНИНГРАДСКАЯ': 'ОБЛ ЛЕНИНГРАДСКАЯ',
                     'РОСТОВСКАЯ ОБЛ': 'РОСТОВСКАЯ ОБЛ',
                     'КРАСНОЯРСКИЙ КРАЙ': 'КРАСНОЯРСКИЙ КРАЙ',
                     'ЧЕЛЯБИНСКАЯ ОБЛ': 'ЧЕЛЯБИНСКАЯ ОБЛ',
                     'ОБЛ САМАРСКАЯ': 'ОБЛ САМАРСКАЯ',
                     'ОБЛ КЕМЕРОВСКАЯ': 'ОБЛ КЕМЕРОВСКАЯ',
                     'ПЕРМСКИЙ КРАЙ': 'ПЕРМСКИЙ КРАЙ',
                     'САНКТ-ПЕТЕРБУРГ Г': 'САНКТ-ПЕТЕРБУРГ',
                     'КРАЙ СТАВРОПОЛЬСКИЙ': 'КРАЙ СТАВРОПОЛЬСКИЙ',
                     'ОБЛ АСТРАХАНСКАЯ': 'ОБЛ АСТРАХАНСКАЯ',
                     'ОБЛ ВОЛОГОДСКАЯ': 'ОБЛ ВОЛОГОДСКАЯ',
                     'ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ - ЮГРА': 'ХАНТЫ-МАНСИЙСКИЙ АО',
                     'АО ХАНТЫ-МАНСИЙСКИЙ-ЮГРА': 'ХАНТЫ-МАНСИЙСКИЙ АО',
                     'ОБЛ ВОЛГОГРАДСКАЯ': 'ОБЛ ВОЛГОГРАДСКАЯ',
                     'ВОЛГОГРАДСКАЯ': 'ОБЛ ВОЛГОГРАДСКАЯ',
                     'РЕСПУБЛИКА ТАТАРСТАН': 'ТАТАРСТАН РЕСП',
                     'ОБЛ НОВОСИБИРСКАЯ': 'ОБЛ НОВОСИБИРСКАЯ',
                     'СВЕРДЛОВСКАЯ ОБЛАСТЬ': 'СВЕРДЛОВСКАЯ ОБЛ',
                     'СТАВРОПОЛЬСКИЙ КРАЙ': 'КРАЙ СТАВРОПОЛЬСКИЙ',
                     'ЯМАЛО-НЕНЕЦКИЙ АО': 'ЯМАЛО-НЕНЕЦКИЙ АО',
                     'ЯМАЛО-НЕНЕЦКИЙ': 'ЯМАЛО-НЕНЕЦКИЙ АО',
                     'ОБЛ ВОРОНЕЖСКАЯ': 'ОБЛ ВОРОНЕЖСКАЯ',
                     'ОБЛ АРХАНГЕЛЬСКАЯ': 'ОБЛ АРХАНГЕЛЬСКАЯ',
                     'ЧЕЛЯБИНСКАЯ ОБЛАСТЬ': 'ЧЕЛЯБИНСКАЯ ОБЛ',
                     'ХАБАРОВСКИЙ КРАЙ': 'ХАБАРОВСКИЙ КРАЙ',
                     'ОБЛ ВЛАДИМИРСКАЯ': 'ОБЛ ВЛАДИМИРСКАЯ',
                     'ХАНТЫ-МАНСИЙСКИЙ АО': 'ХАНТЫ-МАНСИЙСКИЙ АО',
                     'РЕСП. БАШКОРТОСТАН': 'РЕСП БАШКОРТОСТАН',
                     'САРАТОВСКАЯ ОБЛ': 'САРАТОВСКАЯ ОБЛ',
                     'САМАРСКАЯ ОБЛ': 'ОБЛ САМАРСКАЯ',
                     'ОБЛ МУРМАНСКАЯ': 'ОБЛ МУРМАНСКАЯ',
                     'ОБЛ СВЕРДЛОВСКАЯ': 'СВЕРДЛОВСКАЯ ОБЛ',
                     'ОБЛ КУРГАНСКАЯ': 'ОБЛ КУРГАНСКАЯ',
                     'РЕСП КОМИ': 'РЕСП КОМИ',
                     'ПРИМОРСКИЙ КРАЙ': 'ПРИМОРСКИЙ КРАЙ',
                     'САХА /ЯКУТИЯ/ РЕСП': 'САХА /ЯКУТИЯ/ РЕСП',
                     'РЕСП БУРЯТИЯ': 'РЕСП БУРЯТИЯ',
                     'ТЮМЕНСКАЯ ОБЛ': 'ТЮМЕНСКАЯ ОБЛ',
                     'КРАЙ ЗАБАЙКАЛЬСКИЙ': 'КРАЙ ЗАБАЙКАЛЬСКИЙ',
                     'ОБЛ КУРСКАЯ': 'ОБЛ КУРСКАЯ',
                     'ОБЛ КАЛУЖСКАЯ': 'ОБЛ КАЛУЖСКАЯ',
                     'РОСТОВСКАЯ ОБЛАСТЬ': 'РОСТОВСКАЯ ОБЛ',
                     'ОРЕНБУРГСКАЯ ОБЛ': 'ОРЕНБУРГСКАЯ ОБЛ',
                     'ОРЕНБУРГСКАЯ': 'ОРЕНБУРГСКАЯ ОБЛ',
                     'ОБЛ ИВАНОВСКАЯ': 'ОБЛ ИВАНОВСКАЯ',
                     'ТВЕРСКАЯ ОБЛ': 'ТВЕРСКАЯ ОБЛ',
                     'КРАЙ КРАСНОДАРСКИЙ': 'КРАСНОДАРСКИЙ КРАЙ',
                     'ТУЛЬСКАЯ ОБЛ': 'ТУЛЬСКАЯ ОБЛ',
                     'ОБЛ ЛИПЕЦКАЯ': 'ОБЛ ЛИПЕЦКАЯ',
                     'КРАЙ ПЕРМСКИЙ': 'ПЕРМСКИЙ КРАЙ',
                     'САМАРСКАЯ ОБЛАСТЬ': 'ОБЛ САМАРСКАЯ',
                     'ОБЛ АМУРСКАЯ': 'ОБЛ АМУРСКАЯ',
                     'ОБЛ БРЯНСКАЯ': 'ОБЛ БРЯНСКАЯ',
                     'УДМУРТСКАЯ РЕСП': 'УДМУРТСКАЯ РЕСП',
                     'ОБЛ НОВГОРОДСКАЯ': 'ОБЛ НОВГОРОДСКАЯ',
                     'САРАТОВСКАЯ ОБЛАСТЬ': 'САРАТОВСКАЯ ОБЛ',
                     'ОБЛ КАЛИНИНГРАДСКАЯ': 'ОБЛ КАЛИНИНГРАДСКАЯ',
                     'ОБЛ БЕЛГОРОДСКАЯ': 'ОБЛ БЕЛГОРОДСКАЯ',
                     'ОБЛ ЧЕЛЯБИНСКАЯ': 'ЧЕЛЯБИНСКАЯ ОБЛ',
                     'СМОЛЕНСКАЯ ОБЛ': 'СМОЛЕНСКАЯ ОБЛ',
                     'ТАМБОВСКАЯ ОБЛ': 'ТАМБОВСКАЯ ОБЛ',
                     'ОБЛ КИРОВСКАЯ': 'ОБЛ КИРОВСКАЯ',
                     'ОБЛ ТЮМЕНСКАЯ': 'ТЮМЕНСКАЯ ОБЛ',
                     'ТЮМЕНСКАЯ ОБЛАСТЬ': 'ТЮМЕНСКАЯ ОБЛ',
                     'РЕСП КАБАРДИНО-БАЛКАРСКАЯ': 'РЕСП КАБАРДИНО-БАЛКАРСКАЯ',
                     'ОМСКАЯ ОБЛ': 'ОМСКАЯ ОБЛ',
                     'УЛЬЯНОВСКАЯ ОБЛ': 'УЛЬЯНОВСКАЯ ОБЛ',
                     'РЕСП КАРЕЛИЯ': 'РЕСП КАРЕЛИЯ',
                     'РЕСПУБЛИКА КОМИ': 'РЕСП КОМИ',
                     'РЕСП КАРАЧАЕВО-ЧЕРКЕССКАЯ': 'РЕСП КАРАЧАЕВО-ЧЕРКЕССКАЯ',
                     'АО ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ - Ю': 'ХАНТЫ-МАНСИЙСКИЙ АО',
                     'ЯРОСЛАВСКАЯ ОБЛ': 'ЯРОСЛАВСКАЯ ОБЛ',
                     'КРАЙ АЛТАЙСКИЙ': 'КРАЙ АЛТАЙСКИЙ',
                     'РЕСП. САХА (ЯКУТИЯ)': 'САХА /ЯКУТИЯ/ РЕСП',
                     'ТВЕРСКАЯ ОБЛАСТЬ': 'ТВЕРСКАЯ ОБЛ',
                     'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ': 'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ',
                     'ОБЛ КОСТРОМСКАЯ': 'ОБЛ КОСТРОМСКАЯ',
                     'ПЕНЗЕНСКАЯ ОБЛ': 'ПЕНЗЕНСКАЯ ОБЛ',
                     'ПЕНЗЕНСКАЯ': 'ПЕНЗЕНСКАЯ ОБЛ',
                     'РЕСП МАРИЙ ЭЛ': 'РЕСП МАРИЙ ЭЛ',
                     'РЕСП МОРДОВИЯ': 'РЕСП МОРДОВИЯ',
                     'САХАЛИНСКАЯ ОБЛ': 'САХАЛИНСКАЯ ОБЛ',
                     'Г. ЧЕЛЯБИНСК': 'ЧЕЛЯБИНСКАЯ ОБЛ',
                     'ОРЛОВСКАЯ ОБЛ': 'ОРЛОВСКАЯ ОБЛ',
                     'ОРЛОВСКАЯ': 'ОРЛОВСКАЯ ОБЛ',
                     'ТУЛЬСКАЯ ОБЛАСТЬ': 'ТУЛЬСКАЯ ОБЛ',
                     'КРАЙ КАМЧАТСКИЙ': 'КРАЙ КАМЧАТСКИЙ',
                     'ТЫВА РЕСП': 'ТЫВА РЕСП',
                     'РЯЗАНСКАЯ ОБЛ': 'РЯЗАНСКАЯ ОБЛ',
                     'ТАМБОВСКАЯ ОБЛАСТЬ': 'ТАМБОВСКАЯ ОБЛ',
                     'РЕСПУБЛИКА БУРЯТИЯ': 'РЕСП БУРЯТИЯ',
                     'РЕСП АДЫГЕЯ': 'РЕСП АДЫГЕЯ',
                     'МОСКОВСКАЯ ОБЛ': 'ОБЛ МОСКОВСКАЯ',
                     'ТОМСКАЯ ОБЛ': 'ТОМСКАЯ ОБЛ',
                     'ПЕНЗЕНСКАЯ ОБЛАСТЬ': 'ПЕНЗЕНСКАЯ ОБЛ',
                     'ХАКАСИЯ РЕСП': 'ХАКАСИЯ РЕСП',
                     'УЛЬЯНОВСКАЯ ОБЛАСТЬ': 'УЛЬЯНОВСКАЯ ОБЛ',
                     'ЯРОСЛАВСКАЯ ОБЛАСТЬ': 'ЯРОСЛАВСКАЯ ОБЛ',
                     'РЕСП ТАТАРСТАН': 'ТАТАРСТАН РЕСП',
                     'УДМУРТСКАЯ РЕСПУБЛИКА': 'УДМУРТСКАЯ РЕСП',
                     'СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ РЕСП': 'СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ РЕСП',
                     'СМОЛЕНСКАЯ ОБЛАСТЬ': 'СМОЛЕНСКАЯ ОБЛ',
                     'РЯЗАНСКАЯ ОБЛАСТЬ': 'РЯЗАНСКАЯ ОБЛ',
                     'ЧУВАШСКАЯ РЕСПУБЛИКА': 'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ',
                     'ОРЕНБУРГСКАЯ ОБЛАСТЬ': 'ОРЕНБУРГСКАЯ ОБЛ',
                     'ОМСКАЯ ОБЛАСТЬ': 'ОМСКАЯ ОБЛ',
                     'ОБЛ РОСТОВСКАЯ': 'РОСТОВСКАЯ ОБЛ',
                     'МОСКОВСКАЯ ОБЛАСТЬ': 'ОБЛ МОСКОВСКАЯ',
                     'ОБЛ. МОСКОВСКАЯ': 'ОБЛ МОСКОВСКАЯ',
                     'ОРЛОВСКАЯ ОБЛАСТЬ': 'ОРЛОВСКАЯ ОБЛ',
                     'ПСКОВСКАЯ ОБЛ': 'ПСКОВСКАЯ ОБЛ',
                     'ПСКОВСКАЯ': 'ПСКОВСКАЯ ОБЛ',
                     'ТОМСКАЯ ОБЛАСТЬ': 'ТОМСКАЯ ОБЛ',
                     'РЕСПУБЛИКА МОРДОВИЯ': 'РЕСП МОРДОВИЯ',
                     'ОБЛ ПСКОВСКАЯ': 'ПСКОВСКАЯ ОБЛ',
                     'САХАЛИНСКАЯ ОБЛАСТЬ': 'САХАЛИНСКАЯ ОБЛ',
                     'РЕСП КАЛМЫКИЯ': 'РЕСП КАЛМЫКИЯ',
                     'КРАЙ КРАСНОЯРСКИЙ': 'КРАСНОЯРСКИЙ КРАЙ',
                     'ЕВРЕЙСКАЯ АОБЛ': 'ЕВРЕЙСКАЯ АОБЛ',
                     'РЕСПУБЛИКА МАРИЙ ЭЛ': 'РЕСП МАРИЙ ЭЛ',
                     'РЕСПУБЛИКА АДЫГЕЯ': 'РЕСП АДЫГЕЯ',
                     'ОБЛ МАГАДАНСКАЯ': 'ОБЛ МАГАДАНСКАЯ',
                     'НЕНЕЦКИЙ АО': 'ЯМАЛО-НЕНЕЦКИЙ АО',
                     'АСТРАХАНСКАЯ ОБЛАСТЬ': 'ОБЛ АСТРАХАНСКАЯ',
                     'РЕСПУБЛИКА ТЫВА': 'ТЫВА РЕСП',
                     'РЕСП ХАКАСИЯ': 'ХАКАСИЯ РЕСП',
                     'АО ЯМАЛО-НЕНЕЦКИЙ': 'ЯМАЛО-НЕНЕЦКИЙ АО',
                     'ИРКУТСКАЯ ОБЛ': 'ОБЛ ИРКУТСКАЯ',
                     'ПСКОВСКАЯ ОБЛАСТЬ': 'ПСКОВСКАЯ ОБЛ',
                     'БАШКОРТОСТАН РЕСП': 'РЕСП БАШКОРТОСТАН',
                     'ОБЛ САРАТОВСКАЯ': 'САРАТОВСКАЯ ОБЛ',
                     'ЛЕНИНГРАДСКАЯ ОБЛАСТЬ': 'ОБЛ ЛЕНИНГРАДСКАЯ',
                     'РЕСПУБЛИКА КАРЕЛИЯ': 'РЕСП КАРЕЛИЯ',
                     'РЕСПУБЛИКА КАЛМЫКИЯ': 'РЕСП КАЛМЫКИЯ',
                     'ОБЛ ОРЕНБУРГСКАЯ': 'ОРЕНБУРГСКАЯ ОБЛ',
                     'ИРКУТСКАЯ ОБЛАСТЬ': 'ОБЛ ИРКУТСКАЯ',
                     'ОБЛ ТВЕРСКАЯ': 'ТВЕРСКАЯ ОБЛ',
                     'ОБЛ ОМСКАЯ': 'ОМСКАЯ ОБЛ',
                     'ЛЕНИНГРАДСКАЯ ОБЛ': 'ОБЛ ЛЕНИНГРАДСКАЯ',
                     'ОБЛ ТУЛЬСКАЯ': 'ТУЛЬСКАЯ ОБЛ',
                     'ОБЛ ОРЛОВСКАЯ': 'ОРЛОВСКАЯ ОБЛ',
                     'ОБЛ ПЕНЗЕНСКАЯ': 'ПЕНЗЕНСКАЯ ОБЛ',
                     'РЕСП САХА /ЯКУТИЯ/': 'САХА /ЯКУТИЯ/ РЕСП',
                     'ЧУВАШСКАЯ - ЧУВАШИЯ РЕСП': 'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ',
                     'КРАЙ ХАБАРОВСКИЙ': 'ХАБАРОВСКИЙ КРАЙ',
                     'НИЖЕГОРОДСКАЯ ОБЛ': 'ОБЛ НИЖЕГОРОДСКАЯ',
                     'Г. МОСКВА': 'МОСКВА',
                     'ОБЛ ТАМБОВСКАЯ': 'ТАМБОВСКАЯ ОБЛ',
                     'ОБЛ РЯЗАНСКАЯ': 'РЯЗАНСКАЯ ОБЛ',
                     'ЗАБАЙКАЛЬСКИЙ КРАЙ': 'КРАЙ ЗАБАЙКАЛЬСКИЙ',
                     'РЕСП УДМУРТСКАЯ': 'УДМУРТСКАЯ РЕСП',
                     'РЕСП ДАГЕСТАН': 'ДАГЕСТАН РЕСП',
                     'ЧУВАШИЯ ЧУВАШСКАЯ РЕСПУБЛИКА -': 'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ',
                     'ОБЛ ЯРОСЛАВСКАЯ': 'ЯРОСЛАВСКАЯ ОБЛ',
                     'КУРСКАЯ ОБЛ': 'ОБЛ КУРСКАЯ',
                     'НИЖЕГОРОДСКАЯ ОБЛАСТЬ': 'ОБЛ НИЖЕГОРОДСКАЯ',
                     'РЕСП АЛТАЙ': 'РЕСПУБЛИКА АЛТАЙ',
                     'ОБЛ ТОМСКАЯ': 'ТОМСКАЯ ОБЛ',
                     'ПЕРМСКАЯ ОБЛ': 'ПЕРМСКИЙ КРАЙ',
                     'ОБЛ УЛЬЯНОВСКАЯ': 'УЛЬЯНОВСКАЯ ОБЛ',
                     'ОБЛ СМОЛЕНСКАЯ': 'СМОЛЕНСКАЯ ОБЛ',
                     'КУРСКАЯ ОБЛАСТЬ': 'ОБЛ КУРСКАЯ',
                     'СЕВ. ОСЕТИЯ - АЛАНИЯ': 'СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ РЕСП',
                     'РЕСП СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ': 'СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ РЕСП',
                     'НОВОСИБИРСКАЯ ОБЛ': 'ОБЛ НОВОСИБИРСКАЯ',
                     'КРАЙ ПРИМОРСКИЙ': 'ПРИМОРСКИЙ КРАЙ',
                     'ВОЛОГОДСКАЯ ОБЛАСТЬ': 'ОБЛ ВОЛОГОДСКАЯ',
                     'ВОЛОГОДСКАЯ': 'ОБЛ ВОЛОГОДСКАЯ',
                     'САМАРСКАЯ': 'ОБЛ САМАРСКАЯ',
                     'ВОЛГОГРАДСКАЯ ОБЛАСТЬ': 'ОБЛ ВОЛГОГРАДСКАЯ',
                     'КАБАРДИНО-БАЛКАРСКАЯ РЕСП': 'РЕСП КАБАРДИНО-БАЛКАРСКАЯ',
                     'Г. САНКТ-ПЕТЕРБУРГ': 'САНКТ-ПЕТЕРБУРГ',
                     'КЕМЕРОВСКАЯ ОБЛ': 'ОБЛ КЕМЕРОВСКАЯ',
                     'ЧУКОТСКИЙ АО': 'ЧУКОТСКИЙ АО',
                     'ЧУКОТСКИЙ АO': 'ЧУКОТСКИЙ АО',
                     'АО ЧУКОТСКИЙ': 'ЧУКОТСКИЙ АО',
                     'ВЛАДИМИРСКАЯ ОБЛ': 'ОБЛ ВЛАДИМИРСКАЯ',
                     'АСТРАХАНСКАЯ ОБЛ': 'ОБЛ АСТРАХАНСКАЯ',
                     'РЕСП ТЫВА': 'ТЫВА РЕСП',
                     'ВОЛГОГРАДСКАЯ ОБЛ': 'ОБЛ ВОЛГОГРАДСКАЯ',
                     'БЕЛГОРОДСКАЯ ОБЛ': 'ОБЛ БЕЛГОРОДСКАЯ',
                     'БУРЯТИЯ РЕСП': 'РЕСП БУРЯТИЯ',
                     'БЕЛГОРОДСКАЯ ОБЛАСТЬ': 'ОБЛ БЕЛГОРОДСКАЯ',
                     'КУРГАНСКАЯ ОБЛ': 'ОБЛ КУРГАНСКАЯ',
                     'БАШКОРТОСТАН': 'РЕСП БАШКОРТОСТАН',
                     'АСТРАХАНСКАЯ': 'ОБЛ АСТРАХАНСКАЯ',
                     'КЕМЕРОВСКАЯ ОБЛАСТЬ': 'ОБЛ КЕМЕРОВСКАЯ',
                     'ВЛАДИМИРСКАЯ ОБЛАСТЬ': 'ОБЛ ВЛАДИМИРСКАЯ',
                     'ОБЛ САХАЛИНСКАЯ': 'САХАЛИНСКАЯ ОБЛ',
                     'ЛЕНИНГРАДСКАЯ': 'ОБЛ ЛЕНИНГРАДСКАЯ',
                     'АО НЕНЕЦКИЙ': 'ЯМАЛО-НЕНЕЦКИЙ АО',
                     'АМУРСКАЯ ОБЛАСТЬ': 'ОБЛ АМУРСКАЯ',
                     'ГОРЬКОВСКАЯ ОБЛ': 'ОБЛ НИЖЕГОРОДСКАЯ',
                     'РЕСП ИНГУШЕТИЯ': 'РЕСП ИНГУШЕТИЯ',
                     'АРХАНГЕЛЬСКАЯ ОБЛ': 'ОБЛ АРХАНГЕЛЬСКАЯ',
                     'БУРЯТИЯ': 'РЕСП БУРЯТИЯ',
                     'Г МОСКВА': 'МОСКВА',
                     'КОМИ РЕСП': 'РЕСП КОМИ',
                     'РЕСП ЧЕЧЕНСКАЯ': 'РЕСП ЧЕЧЕНСКАЯ',
                     'МУРМАНСКАЯ ОБЛ': 'ОБЛ МУРМАНСКАЯ',
                     'ЧИТИНСКАЯ ОБЛ': 'ЧИТИНСКАЯ ОБЛ',
                     'МАРИЙ ЭЛ РЕСП': 'РЕСП МАРИЙ ЭЛ',
                     'НОВГОРОДСКАЯ ОБЛ': 'ОБЛ НОВГОРОДСКАЯ',
                     'КАРАЧАЕВО-ЧЕРКЕССКАЯ РЕСП': 'РЕСП КАРАЧАЕВО-ЧЕРКЕССКАЯ',
                     'ВОРОНЕЖСКАЯ ОБЛ': 'ОБЛ ВОРОНЕЖСКАЯ',
                     'КАЛИНИНГРАДСКАЯ ОБЛ': 'ОБЛ КАЛИНИНГРАДСКАЯ',
                     'КАЛУЖСКАЯ ОБЛАСТЬ': 'ОБЛ КАЛУЖСКАЯ',
                     'БРЯНСКАЯ ОБЛ': 'ОБЛ БРЯНСКАЯ',
                     'КАЛУЖСКАЯ ОБЛ': 'ОБЛ КАЛУЖСКАЯ',
                     'ЛИПЕЦКАЯ ОБЛАСТЬ': 'ОБЛ ЛИПЕЦКАЯ',
                     'ЛИПЕЦКАЯ ОБЛ': 'ОБЛ ЛИПЕЦКАЯ',
                     'АМУРСКАЯ ОБЛ': 'ОБЛ АМУРСКАЯ',
                     'КАБАРДИНО-БАЛКАРСКАЯ': 'РЕСП КАБАРДИНО-БАЛКАРСКАЯ',
                     'МУРМАНСКАЯ ОБЛАСТЬ': 'ОБЛ МУРМАНСКАЯ',
                     'ЕВРЕЙСКАЯ АВТОНОМНАЯ': 'ЕВРЕЙСКАЯ АОБЛ',
                     'ЧЕЧЕНСКАЯ РЕСП': 'РЕСП ЧЕЧЕНСКАЯ',
                     'КАМЧАТСКИЙ КРАЙ': 'КРАЙ КАМЧАТСКИЙ',
                     'КРАСНОДАРСКИЙ': 'КРАСНОДАРСКИЙ КРАЙ',
                     'ВОРОНЕЖСКАЯ ОБЛАСТЬ': 'ОБЛ ВОРОНЕЖСКАЯ',
                     'АДЫГЕЯ РЕСП': 'РЕСП АДЫГЕЯ',
                     'АРХАНГЕЛЬСКАЯ ОБЛАСТЬ': 'ОБЛ АРХАНГЕЛЬСКАЯ',
                     'КУРГАНСКАЯ ОБЛАСТЬ': 'ОБЛ КУРГАНСКАЯ',
                     'АЛТАЙСКИЙ КРАЙ': 'КРАЙ АЛТАЙСКИЙ',
                     'КИРОВСКАЯ ОБЛ': 'ОБЛ КИРОВСКАЯ',
                     'ВОЛОГОДСКАЯ ОБЛ': 'ОБЛ ВОЛОГОДСКАЯ',
                     'МОСКОВСКАЯ': 'ОБЛ МОСКОВСКАЯ',
                     'МОРДОВИЯ РЕСП': 'РЕСП МОРДОВИЯ',
                     'НОВОСИБИРСКАЯ ОБЛАСТЬ': 'ОБЛ НОВОСИБИРСКАЯ',
                     'БРЯНСКАЯ ОБЛАСТЬ': 'ОБЛ БРЯНСКАЯ',
                     'ИВАНОВСКАЯ ОБЛ': 'ОБЛ ИВАНОВСКАЯ',
                     'ДАГЕСТАН РЕСП': 'ДАГЕСТАН РЕСП',
                     'ИВАНОВСКАЯ ОБЛАСТЬ': 'ОБЛ ИВАНОВСКАЯ',
                     'РЕСПУБЛИКА ДАГЕСТАН': 'ДАГЕСТАН РЕСП',
                     'НОВГОРОДСКАЯ ОБЛАСТЬ': 'ОБЛ НОВГОРОДСКАЯ',
                     'КОСТРОМСКАЯ ОБЛ': 'ОБЛ КОСТРОМСКАЯ',
                     'АОБЛ ЕВРЕЙСКАЯ': 'ЕВРЕЙСКАЯ АОБЛ',
                     'КОСТРОМСКАЯ ОБЛАСТЬ': 'ОБЛ КОСТРОМСКАЯ',
                     'РОСТОВСКАЯ': 'РОСТОВСКАЯ ОБЛ',
                     'СТАВРОПОЛЬСКИЙ': 'КРАЙ СТАВРОПОЛЬСКИЙ',
                     'КАМЧАТСКАЯ ОБЛАСТЬ': 'КРАЙ КАМЧАТСКИЙ',
                     'КАМЧАТС??ИЙ КРАЙ': 'КРАЙ КАМЧАТСКИЙ',
                     'ОБЛ. СВЕРДЛОВСКАЯ': 'СВЕРДЛОВСКАЯ ОБЛ',
                     'ЧЕЧЕНСКАЯ РЕСПУБЛИКА': 'РЕСП ЧЕЧЕНСКАЯ',
                     'РЕСПУБЛИКА АЛТАЙ': 'РЕСПУБЛИКА АЛТАЙ',
                     'КАЛМЫКИЯ РЕСП': 'РЕСП КАЛМЫКИЯ',
                     'АЛТАЙСКИЙ': 'КРАЙ АЛТАЙСКИЙ',
                     'КАРЕЛИЯ РЕСП': 'РЕСП КАРЕЛИЯ',
                     'РОССИЯ': 'ОБЛ МОСКОВСКАЯ',
                     'МЫТИЩИНСКИЙ Р-Н': 'ОБЛ МОСКОВСКАЯ',
                     'СВЕРДЛОВСКАЯ': 'СВЕРДЛОВСКАЯ ОБЛ',
                     'ЧУВАШСКАЯ РЕСП': 'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ',
                     'РЕСП. КОМИ': 'РЕСП КОМИ',
                     'ОБЛ.САРАТОВСКАЯ': 'САРАТОВСКАЯ ОБЛ',
                     'ОРЁЛ': 'ОРЛОВСКАЯ ОБЛ',
                     'ОБЛ.МОСКОВСКАЯ': 'ОБЛ МОСКОВСКАЯ',
                     'РЕСПУБЛИКА ХАКАСИЯ': 'ХАКАСИЯ РЕСП',
                     'КРАЙ. СТАВРОПОЛЬСКИЙ': 'КРАЙ СТАВРОПОЛЬСКИЙ',
                     'ОБЛ. КУРГАНСКАЯ': 'ОБЛ КУРГАНСКАЯ',
                     'КАРЕЛИЯ': 'РЕСП КАРЕЛИЯ',
                     'МОСКВОСКАЯ ОБЛ': 'ОБЛ МОСКОВСКАЯ',
                     '74': 'ЧЕЛЯБИНСКАЯ ОБЛ',
                     'ОБЛ. ВЛАДИМИРСКАЯ': 'ОБЛ ВЛАДИМИРСКАЯ',
                     'КАЛУЖСКАЯ': 'ОБЛ КАЛУЖСКАЯ',
                     'КРАЙ. ПЕРМСКИЙ': 'ПЕРМСКИЙ КРАЙ',
                     'ОБЛ.НИЖЕГОРОДСКАЯ': 'ОБЛ НИЖЕГОРОДСКАЯ',
                     'ОБЛ. ЧЕЛЯБИНСКАЯ': 'ЧЕЛЯБИНСКАЯ ОБЛ',
                     'Г.МОСКВА': 'МОСКВА',
                     'КОМИ': 'РЕСП КОМИ',
                     'ПЕРМСКИЙ': 'ПЕРМСКИЙ КРАЙ',
                     'ОБЛ. ЛИПЕЦКАЯ': 'ОБЛ ЛИПЕЦКАЯ',
                     'НОВОСИБИРСКАЯ': 'ОБЛ НОВОСИБИРСКАЯ',
                     'ИНГУШЕТИЯ РЕСП': 'РЕСП ИНГУШЕТИЯ',
                     'САХА /ЯКУТИЯ/': 'САХА /ЯКУТИЯ/ РЕСП',
                     'КИРОВСКАЯ ОБЛАСТЬ': 'ОБЛ КИРОВСКАЯ',
                     'КАРАЧАЕВО-ЧЕРКЕССКАЯ': 'РЕСП КАРАЧАЕВО-ЧЕРКЕССКАЯ',
                     'ОМСКАЯ': 'ОМСКАЯ ОБЛ',
                     'КРАЙ.ПЕРМСКИЙ': 'ПЕРМСКИЙ КРАЙ',
                     '98': 'САНКТ-ПЕТЕРБУРГ',
                     'АРХАНГЕЛЬСКАЯ': 'ОБЛ АРХАНГЕЛЬСКАЯ',
                     'ОБЛ. МУРМАНСКАЯ': 'ОБЛ МУРМАНСКАЯ',
                     'МАГАДАНСКАЯ ОБЛАСТЬ': 'ОБЛ МАГАДАНСКАЯ',
                     'ДАЛЬНИЙ ВОСТОК': 'ОБЛ АМУРСКАЯ',
                     'ТЮМЕНСКАЯ': 'ТЮМЕНСКАЯ ОБЛ',
                     'КАЛИНИНГРАДСКАЯ ОБЛ.': 'ОБЛ КАЛИНИНГРАДСКАЯ',
                     'ОБЛ. НОВОСИБИРСКАЯ': 'ОБЛ НОВОСИБИРСКАЯ',
                     'ХАКАСИЯ': 'ХАКАСИЯ РЕСП',
                     'ОБЛ.РОСТОВСКАЯ': 'РОСТОВСКАЯ ОБЛ',
                     'РЕСПУБЛИКА САХА': 'САХА /ЯКУТИЯ/ РЕСП',
                     'РЕСП.БАШКОРТОСТАН': 'РЕСП БАШКОРТОСТАН',
                     'БРЯНСКИЙ': 'ОБЛ БРЯНСКАЯ',
                     'ОБЛ. КИРОВСКАЯ': 'ОБЛ КИРОВСКАЯ',
                     'ПРИВОЛЖСКИЙ ФЕДЕРАЛЬНЫЙ ОКРУГ': 'ОБЛ НИЖЕГОРОДСКАЯ',
                     'ВОЛОГОДСКАЯ ОБЛ.': 'ОБЛ ВОЛОГОДСКАЯ',
                     'ОБЛ. БЕЛГОРОДСКАЯ': 'ОБЛ БЕЛГОРОДСКАЯ',
                     'РЕСП ЧУВАШСКАЯ - ЧУВАШИЯ': 'ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ',
                     'ТОМСКАЯ': 'ТОМСКАЯ ОБЛ',
                     'ГУСЬ-ХРУСТАЛЬНЫЙ Р-Н': 'ОБЛ ВЛАДИМИРСКАЯ',
                     'КЕМЕРОВСКАЯ': 'ОБЛ КЕМЕРОВСКАЯ',
                     'ЭВЕНКИЙСКИЙ АО': 'ЭВЕНКИЙСКИЙ АО',
                     'РЕСПУБЛИКАТАТАРСТАН': 'ТАТАРСТАН РЕСП',
                     'РЕСП.ТАТАРСТАН': 'ТАТАРСТАН РЕСП',
                     'КАЛМЫКИЯ': 'РЕСП КАЛМЫКИЯ',
                     'Г.ОДИНЦОВО МОСКОВСКАЯ ОБЛ': 'ОБЛ МОСКОВСКАЯ',
                     'КРАЙ. КРАСНОЯРСКИЙ': 'КРАСНОЯРСКИЙ КРАЙ'}
