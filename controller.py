from flask import request

from config import pd, model


def predict_controller():
	data = request.get_json(force=True)
	score = 0
	credit_request = pd.DataFrame({
		'FLAG_OWN_CAR': data['FLAG_OWN_CAR'],
		'FLAG_OWN_REALTY': data['FLAG_OWN_REALTY'],
		'CNT_CHILDREN': data['CNT_CHILDREN'],
		'AMT_INCOME_TOTAL': data['AMT_INCOME_TOTAL'],
		'NAME_INCOME_TYPE': data['NAME_INCOME_TYPE'],
		'NAME_EDUCATION_TYPE': data['NAME_EDUCATION_TYPE'],
		'NAME_FAMILY_STATUS': data['NAME_FAMILY_STATUS'],
		'NAME_HOUSING_TYPE': data['NAME_HOUSING_TYPE'],
		'DAYS_BIRTH': data['DAYS_BIRTH'],
		'DAYS_EMPLOYED': data['DAYS_EMPLOYED'],
		'OCCUPATION_TYPE': data['OCCUPATION_TYPE'],
		'CNT_FAM_MEMBERS': data['CNT_FAM_MEMBERS'],
		'CNT_ADULTS': data['CNT_ADULTS'],
		'AMT_INCOME_PER_CHILDREN': data['AMT_INCOME_PER_CHILDREN'],
		'AMT_INCOME_PER_FAM_MEMBER': data['AMT_INCOME_PER_FAM_MEMBER']
	})
	for index, row in credit_request.iterrows():
		score = model.predict([row])
	return {"score": round(score[0] * 100)}