import json
import requests
import streamlit as st


def query_few_shot_learning(API_URL, HEADERS, payload='', parameters=None, options={'use_cache': False}):
    body = {
        "inputs": payload, 
        'parameters': parameters, 
        'options': options
        }
    response = requests.request("POST", API_URL, headers=HEADERS, data=json.dumps(body))
    if str(response) == "<Response [400]>":
        st.markdown("INVALID TOKEN")
        return 'invalid_token'
    else:
        test = json.loads(response.content.decode("utf-8"))
        return (response.json()[0]['generated_text'], test)


def generate_prompt(model, test):
    task = model['task']
    examples = model['examples']
    stop = model['parameters']['end_sequence']
    prompt = task + '\n\n'
    for shot in examples:
        ex = shot[0]
        sol = shot[1]
        prompt += ex + '\n' + sol + '\n' + stop + '\n'
    prompt += test + '\n'
    return prompt


def get_challenge_output(API_URL, HEADERS, prompt, parameters):
    data = query_few_shot_learning(API_URL, HEADERS, prompt, parameters)
    if data == "invalid_token":
        return data
    else:
        return data[0][len(prompt):] 


def get_model_score(test, model):
  l_desc = len(model["task"])
  n_ex = len(model["examples"])
  test['predicted'] = test['test_text'].map(lambda x: get_challenge_output(generate_prompt(model, x), model['parameters']))
  test['is_ok'] = test['label'] == test['predicted']
  n_ok = test['is_ok'].sum()
  print('predicted df head', test['predicted'].head(10))
  print('l_desc:', l_desc, 'n_ok:', n_ok, 'n_ex:',n_ex)
  score = min(200/l_desc, 10) + n_ok * (1.3 - n_ex/10)
  return score


def send_simple_message(contact_pseudo: str, contact_mail: str, submitted_model: str):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxe92723bea09e43b99780f267ff7e75c2.mailgun.org/messages",
		auth=("api", st.secrets["mailgun_api_key"]),
		data={"from": "Mailgun Sandbox <postmaster@sandboxe92723bea09e43b99780f267ff7e75c2.mailgun.org>",
			"to": "Théo Badoz <theo.badoz@gmail.com>",
			"subject": contact_pseudo + " submission",
			"text": "mail: " + contact_mail + "\nmodel: " + submitted_model})