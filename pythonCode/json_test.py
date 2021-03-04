import json
from collections import OrderedDict

# rate_result = OrderedDict()
# rate_result['code'] = "068270"
# rate_result['name'] = "셀트리온"
# rate_result['predict_rate'] = 2.7
# rate_result['predict_rate2'] = [2.2, -1.7, 2.3, -3.5, 2.6, 2.8, -0.7]
# rate_result = json.dumps(rate_result, ensure_ascii=False, indent="\t")
# print(rate_result)

# rate_result = OrderedDict()
# company = OrderedDict()
# # rate_result['code'] = "068270"
# company['name'] = "셀트리온"
# company['predict_rate'] = 2.7
# company['predict_rate2'] = [2.2, -1.7, 2.3, -3.5, 2.6, 2.8, -0.7]
# rate_result['{}'.format("068270")] = company
# # rate_result = json.dumps(rate_result, ensure_ascii=False, indent="\t")
# print(rate_result)
# print(type(rate_result))
# #
# with open('../json_test_file.json', 'w', encoding="UTF-8") as outfile:
#     json.dump(rate_result, outfile, indent="\t")

with open("../json_test_file.json", 'r', encoding="UTF-8") as f:
    result = json.load(f)
print(result)
# print(result['068270'])

rate_result = OrderedDict()
company = OrderedDict()
# rate_result['code'] = "068270"
company['name'] = "삼성전자"
company['predict_rate'] = 1.7
company['predict_rate2'] = [1.2, -2.7, 1.3, -1.5, 1.6, 2.8, -0.7]
rate_result['{}'.format("005930")] = company

result.update(rate_result)
print(result)
print(result['005930'])

with open("../json_test_file.json", 'w', encoding="UTF-8") as f:
    json.dump(result, f, indent="\t")

with open("../json_test_file.json", 'r', encoding="UTF-8") as f:
    result2 = json.load(f)

print(result2)
