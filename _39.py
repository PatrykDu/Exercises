def generate_sql(table_name, col_names, constraints):
    sql = "CREATE TABLE {} ({} {}, {} {})".format(table_name, col_names[0], constraints[0], col_names[1], constraints[1]).rstrip()
    return sql


print(generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL']))
print(generate_sql('Product', ['Id', 'QuantityName'], ['INTEGER PRIMARY KEY', '']))
