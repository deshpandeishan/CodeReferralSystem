from user import CallCodeGenerator
from sample_data import data
from link_list_dict import LinkListDict

generate_code = CallCodeGenerator()
link_items = LinkListDict()

for item in data:
    sub_dict = data[item]
    link_items.link(sub_dict, item)
generate_code.call_code()
generate_code.task()
