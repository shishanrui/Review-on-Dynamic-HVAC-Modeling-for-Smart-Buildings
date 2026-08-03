from base import SSSS

topic = 'dynamic HVAC model'

sub_keyword_list1 = [
    '("dynamic model" OR "dynamic simulation")',
    '("transient model" OR "transient simulation")',
    '("time-dependent model" OR "time-varying model")',
    'emulation',
    '("data-driven model" OR "machine learning model" OR "neural network model")',
]

sub_keyword_list2 = [
    '("fault detection and diagnosis" OR "anomaly detection")',
    '("optimal control" OR "control optimization")',
    'adaptive control',
    'predictive control',
    'reinforcement learning',
    'demand response',
    '("load flexibility" OR "energy flexibility")',
    'frequency regulation',
    '',
]

# Subsystem-level entries
sub_keyword_list3a = [
    '("cooling plant" OR "heating plant")',
    '"district heating and cooling"',
    '"variable air volume"',
    '"variable refrigerant flow"',
    '"dedicated outdoor air system"',
    '"vapor compression system"',
    '"heat pump"',
]

# Component-level entries
sub_keyword_list3b = [
    'chiller',
    '"cooling tower"',
    '"air handling unit"',
    'coil',
    '"heat exchanger"',
    '"thermal storage"',
    '"thermal dynamics"',
    'airflow',
    '"indoor temperature distribution"',
]


building_prefix = ['("building" OR "HVAC")']

subsystem_queries = [
    sub_keyword_list1,
    sub_keyword_list2,
    sub_keyword_list3a,
]

component_queries = [
    sub_keyword_list1,
    sub_keyword_list2,
    sub_keyword_list3b,
    building_prefix,
]

year_from = 2000
year_to = 2025

citation_threshold = 0

number_of_searches_per_key_word_per_year = 10

sleep_interval = 60

number_of_subsystem_queries = (
    len(sub_keyword_list1)
    * len(sub_keyword_list2)
    * len(sub_keyword_list3a)
)
number_of_component_queries = (
    len(sub_keyword_list1)
    * len(sub_keyword_list2)
    * len(sub_keyword_list3b)
    * len(building_prefix)
)


# Run both searches
SSSS(
    topic,
    subsystem_queries,
    year_from,
    year_to,
    citation_threshold,
    number_of_searches_per_key_word_per_year,
    sleep_interval,
)

# SSSS(
#     topic,
#     component_queries,
#     year_from,
#     year_to,
#     citation_threshold,
#     number_of_searches_per_key_word_per_year,
#     sleep_interval,
# )
