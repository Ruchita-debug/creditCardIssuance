import urllib3, requests, json

def inference_call(data_list):
    mltoken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxMDAwMzMxMjY5IiwidXNlcm5hbWUiOiJ5Z3VhZiIsInJvbGUiOiJVc2VyIiwicGVybWlzc2lvbnMiOlsic2lnbl9pbl9vbmx5IiwiYWNjZXNzX2NhdGFsb2ciLCJ2aWV3X2dvdmVybmFuY2VfYXJ0aWZhY3RzIiwiYWNjZXNzX2luZm9ybWF0aW9uX2Fzc2V0cyIsInZpZXdfcXVhbGl0eSJdLCJncm91cHMiOlsxMDAwMF0sInN1YiI6InlndWFmIiwiaXNzIjoiS05PWFNTTyIsImF1ZCI6IkRTWCIsImlhdCI6MTYzNjM2Njc2NSwiZXhwIjozNjE2MzYzNjMxNjV9.GlyxHwa_35c0KNbOhQ1gd-K98EDvj6nD6AAJ8W9QkQKEY2OhRuSnZZafgHqQjAgXgTvIrCe2klwn2pFvEWhEu3szJ6zbbG3972X7wM6V8sdBKvd6w6-sULtbY-ZuGlUscnRrqjClsY9J1_g0jlEr_ip2bTNnknGLCZTSNTQPQ-PnYOgDJdCz_tNoECUnJogBQMYxn3ZqDDg80kKNHPb9Ig8-xzr2nD0nehtOCMAg8vYDi16tOIstj017j1Vqv9W8y39VGmOVHQ6cCjG1LvL64RMoN1-HN0SiCjSMgIVvLGb6gmmGEHCZc9WmFZ0fxg9vZ7yLJcMChaKKvXOrxCZ7iw'
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    payload_scoring = {"input_data": [
                                    {"fields": [['code_gender', 'flag_own_car', 'flag_own_realty', 'cnt_children', 'amt_income_total', 'name_income_type', 'name_education_type', 'name_family_status', 'name_housing_type', 'age_years', 'years_employed', 'cnt_fam_members']],
                                    "values": [data_list]
                                    }
                                ]
                    }

    response_scoring = requests.post('https://cpd-outcomes-cpd-cpd-outcomes.cp4d-prod-na-04-demo-b9aa1303e037748136e24e1f282ebee9-0000.us-south.containers.appdomain.cloud/ml/v4/deployments/c1d85649-3653-446b-a5bc-77ff2a2bd473/predictions?version=2021-11-10', json=payload_scoring, headers=header)
    print("Scoring response")
    predictions = response_scoring.json()
    print(json.loads(response_scoring.text))
    op = predictions['predictions'][0]['values'][0][0]
    return op