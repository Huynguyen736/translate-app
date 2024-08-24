import json
import requests

def get_mw_data(word):
	api_key = "0ce55ada-b016-4ebc-bf6b-0ef882015e5b"
	url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		return None

def safe_get(data, *keys, default=None):
	for key in keys:
		if isinstance(data, dict) and key in data:
			data = data[key]
		elif isinstance(data, list) and isinstance(key, int) and 0 <= key < len(data):
			data = data[key]
		else:
			return default
	return data


def extract_definitions(entry):
	definitions = []
	def_data = safe_get(entry, "shortdef")
	if isinstance(def_data, list):
		for definition in def_data:
			definitions.append(definition)
	return definitions


def extract_examples(entry):
	examples = []
	def_data = safe_get(entry, "def")
	if isinstance(def_data, list):
		for sense_seq in def_data:
			for sense in safe_get(sense_seq, "sseq", default=[]):
				for subsense in sense:
					if subsense[0] == "sense":
						dt = safe_get(subsense[1], "dt")
						if isinstance(dt, list):
							for d in dt:
								if isinstance(d, list) and d[0] == "vis":
									for example in d[1]:
										examples.append(example.get("t", ""))
								if isinstance(d, list) and d[0] == "uns":
									for subd in d[1]:
										for subd2 in subd:
											if isinstance(subd2, list) and subd2[0] == "vis":
												for example in subd2[1]:
													examples.append(example.get("t", ""))
	return examples


def get_word_data(word):
	mw_data = get_mw_data(word)
	word_data = {
		"word": word,
		"entries": []
	}
	
	for entry in mw_data:
		if isinstance(entry, dict):
			entry_data = {
				"homograph": safe_get(entry, "hom", default="1"),
				"functional_label": safe_get(entry, "fl", default=""),
				"definitions": extract_definitions(entry),
				"examples": extract_examples(entry),
				"pronunciations": [],
				"audio_urls": []
			}
			
			prs = safe_get(entry, "hwi", "prs")
			if isinstance(prs, list):
				for pr in prs:
					ipa = safe_get(pr, "mw")
					if ipa:
						entry_data["pronunciations"].append(ipa)
					
					audio_name = safe_get(pr, "sound", "audio")
					if audio_name:
						subdirectory = audio_name[:1]
						audio_url = f"https://media.merriam-webster.com/soundc11/{subdirectory}/{audio_name}.wav"
						entry_data["audio_urls"].append(audio_url)
			
			word_data["entries"].append(entry_data)
	
	return word_data


#result = get_word_data("hell")
#print(json.dumps(result, indent=2))