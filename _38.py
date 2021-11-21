def generate_sql(table_name, col_names):
    col_names = tuple(col_names)
    sql = 'CREATE TABLE {} {}'.format(table_name, col_names).replace("'",'')
    return sql


print(generate_sql('Product', ['Id', 'ProductName']))
