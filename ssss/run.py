from base import SSSS

topic = 'dynamic HVAC model'


sub_keyword_list1 = ['("dynamic model" OR "dynamic simulation")',
                     '("transient model" OR "transient simulation")',
                     '("time-dependent model" OR "time-varying model")',
                     'emulation',
                     '("data-driven model" OR "machine learning model" OR "neural network model")',
                     ]

sub_keyword_list2 = ['("fault detection and diagnosis" OR "anomaly detection")',
                     '("optimal control" OR "control optimization)',
                     'adaptive control',
                     'predictive control',
                     'reinforcement learning',
                     'demand response',
                     '("load flexibility" OR "energy flexibility")',
                     'frequency regulation',
                     '',]

sub_keyword_list3 = [
                     'chiller',
                     'cooling tower',
                     'air handling unit',
                     'coil',
                     'heat exchanger',
                     'thermal storage',
                     'thermal dynamics',
                     'airflow',
                     'indoor temperature distribution']
#
sub_keyword_list4 = ['("building" OR "HVAC")',]


sub_keyword_list = [sub_keyword_list1, sub_keyword_list2, sub_keyword_list3]
# sub_keyword_list = [sub_keyword_list1, sub_keyword_list2, sub_keyword_list3, sub_keyword_list4]

year_from = 2000
year_to = 2025

citation_threshold = 0

number_of_searches_per_key_word_per_year = 10

sleep_interval = 60

SSSS(topic, sub_keyword_list, year_from, year_to, citation_threshold, number_of_searches_per_key_word_per_year, sleep_interval)
