# https://dev.mysql.com/doc/refman/8.0/en/show-tables.html
show_tables = """
SHOW FULL TABLES;
"""

# https://dev.mysql.com/doc/refman/8.0/en/show-columns.html
show_columns_tmpl = """
SHOW FULL COLUMNS FROM {table_name};
"""
