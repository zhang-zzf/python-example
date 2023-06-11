from elasticsearch7 import Elasticsearch
from elasticsearch7.helpers import bulk

es = Elasticsearch(
    hosts="http://10.0.9.18:9200",
    http_auth=("elastic", "Gt4AvnA0zkqe")
)

ping = es.ping()
print(ping)

es.index(index="family_accounts_pay",
         body={})
