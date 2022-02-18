import csv
import random
from objectifiedetree import *
import xml.etree.ElementTree as ET

f = open('TestTemplate.csv', 'r')
csv_data = csv.reader(f)
data = []

for row in csv_data:
    data.append(row)

data = data[1:-1]
print(data)


def GenerateXML(fileName):
    price_list = ET.Element('price_list')
    plan = ET.Element('plan')
    plan.attrib = {'ondemand_billing': 'no'}
    deal = ET.Element('deal')
    deal.attrib = {'customization_flag': 'optional', 'ondemand_billing': 'no', 'grant_resources_as_group': 'no'}
    product = ET.Element('product')

    for row in data:
        plan_name = ET.Element('plan_name')
        plan_name.text = row[0]

        plan_code = ET.Element('plan_code')
        plan_code.text = row[0]

        description = ET.Element('description')
        description.text = row[0]

        service_deal = ET.Element('service_deal')

        service_name = ET.Element('service_name')
        service_name.text = row[7]

        service_id = ET.Element('service_id')
        service_id.text = row[7] + " " + str(random.randint(100, 999))

        deal_array_elem = ET.Element('deal_array_elem')
        deal_array_elem.text = row[0] + " " + row[3] + " " + row[4]

        bal_info_index = ET.Element('bal_info_index')
        bal_info_index.text = '0'

        subscription_index = ET.Element('subscription_index')
        subscription_index.text = '0'

        service_deal.append(service_name)
        service_deal.append(service_id)
        service_deal.append(deal_array_elem)
        service_deal.append(bal_info_index)
        service_deal.append(subscription_index)

        deal_name = ET.Element('deal_name')
        deal_name.text = row[0] + ' ' + row[3] + ' ' + row[4]

        deal_code = ET.Element('deal_code')
        deal_code.text = row[0] + ' ' + row[3] + ' ' + row[4]

        description_deal = ET.Element('description')
        description_deal.text = row[0] + ' ' + row[3] + ' ' + row[4]

        start_time = ET.Element('start_time')

        datetime = ET.Element('datetime')

        date = ET.Element('date')
        time = ET.Element('time')

        datetime.append(date)
        datetime.append(time)

        start_time.append(datetime)

        permitted = ET.Element('permitted')
        permitted.text = row[7]

        deal_product = ET.Element('deal_product')
        deal_product.attrib = {'status': 'active'}

        deal_product = ET.Element('deal_product')
        deal_product.attrib = {'status': 'active'}

        product_name = ET.Element('product_name')
        product_name.text = row[0] + " " + row[3] + " " + row[4]

        product_code = ET.Element('product_code')
        product_code.text = row[0] + " " + row[3] + " " + row[4]

        quantity = ET.Element('quantity')
        quantity.text = '1.0'

        purchase_discount = ET.Element('purchase_discount')
        purchase_discount.text = '0.0'

        cycle_discount = ET.Element('cycle_discount')
        cycle_discount.text = '0.0'

        usage_discount = ET.Element('usage_discount')
        usage_discount.text = '0.0'

        status_flag = ET.Element('status_flag')
        status_flag.text = '0'

        deal_product.append(product_name)
        deal_product.append(product_code)
        deal_product.append(quantity)
        deal_product.append(purchase_discount)
        deal_product.append(cycle_discount)
        deal_product.append(usage_discount)
        deal_product.append(status_flag)

    plan.append(plan_name)
    plan.append(plan_code)
    plan.append(description)
    plan.append(service_deal)

    deal.append(deal_name)
    deal.append(deal_code)
    deal.append(description_deal)
    deal.append(start_time)
    deal.append(permitted)
    deal.append(deal_product)

    price_list.append(plan)
    price_list.append(deal)

    tree = ET.ElementTree(price_list)

    with open(fileName, 'wb') as files:
        tree.write(files)


if __name__ == "__main__":
    GenerateXML('Customer3.xml')
