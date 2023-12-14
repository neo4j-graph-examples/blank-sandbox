# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (n)
RETURN COUNT(n) AS count
LIMIT $limit
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        limit="10",
        database_="neo4j")
    for record in result.records:
        print(record['count'])
