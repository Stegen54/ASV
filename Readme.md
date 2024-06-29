How to set up the MYSQL database:

1. Install MYSQL on your computer
2. You might need to add MYSQL to your PATH
3. Edit you MYSQL configuration file to allow for local infile loading
    - Open the file 'my.ini' in the MYSQL installation folder
    - Add the following lines to the file under the [mysqld] section:
        ```
        local-infile=1
        ```
    - Save the file and restart the MYSQL server
4. navigate to the database folder in the terminal 
    for ulms it is 'umls-2024AA-metathesaurus-level-0\2024AA\META\mysql_tables.sql'
    for Rxnorm it is 'RxNorm_full_06032024\rrf'
5. Run the following command to create the tables:
    mysql --local-infile=1 -u username -p
    create database database_name;
    use database_name;  
    # for ulms
    source mysql_tables.sql
    source mysql_indexes.sql
    # for Rxnorm
    # also create and use the database
    source Table_scripts_mysql_rxn.sql
    source Load_scripts_mysql_rxn_win.sql
    source Indexes_mysql_rxn.sql