# -*- coding:utf-8 -*-
# Author：LukcinSven
# Form_pc: Home_win10
# Creat_Date：2020-03-00
# Topic_for：_what_

# -*- coding:utf-8 -*-
# Author：LukcinSven
# Form_pc: Home_win10
# Creat_Date：2021-01-07
# Topic_for：_shoadn_script_learn_

import shodan

# 更换自己的Key
SHODAN_API_KEY = "XXX"

api = shodan.Shodan(SHODAN_API_KEY)
try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')

        print("sven-hhh")
except shodan.APIError as e:
    print('Error: {}'.format(e))
