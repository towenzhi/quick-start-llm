import json as JSON


def jsonl_to_json(jsonl_file, json_file):
    dict_list = []

    with open(jsonl_file, 'r', encoding='utf-8') as f:
        jsonl_data = f.readlines()
        for line in jsonl_data:
            line_dict = JSON.loads(line)
            del line_dict['task_type']
            del line_dict['domain']
            del line_dict['metadata']
            del line_dict['answer_from']
            del line_dict['human_verified']
            del line_dict['copyright']

            dict_list.append(line_dict)

    with open(json_file, 'w', encoding='utf-8') as f:
        JSON.dump(dict_list, f, indent=4, ensure_ascii=False)


jsonl_file = 'data/COIG-CQIA_xhs.jsonl'
json_file = 'data/COIG-CQIA_xhs.json'

if __name__ == '__main__':
    jsonl_to_json(jsonl_file, json_file)
