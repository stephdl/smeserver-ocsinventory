# OCS Inventory NG MySQL init template
#
# This files creates/updates OCS' MySQL database infos


USE mysql;

CREATE DATABASE IF NOT EXISTS { $ocs{DbName} };

REPLACE INTO user (
                     host,
                     user,
                     password)
            VALUES (
                     'localhost',
                     '{ $ocs{DbUser} }',
                     PASSWORD ('{ $ocs{DbPassword} }'));

REPLACE INTO user (
                     host,
                     user,
                     password)
            VALUES (
                     '%',
                     '{ $ocs{DbUser} }',
                     PASSWORD ('{ $ocs{DbPassword} }'));

REPLACE INTO db (
                   host,
                   db,
                   user,
                   select_priv, insert_priv, update_priv, delete_priv,
                   create_priv, alter_priv, index_priv, drop_priv, create_tmp_table_priv,
                   grant_priv, lock_tables_priv, references_priv) 
          VALUES (
                   'localhost',
                   '{ $ocs{DbName} }',
                   '{ $ocs{DbUser} }',
                   'Y', 'Y', 'Y', 'Y',
                   'Y', 'Y', 'Y', 'Y', 'Y',
                   'N', 'Y', 'Y');

REPLACE INTO db (
                   host,
                   db,
                   user,
                   select_priv, insert_priv, update_priv, delete_priv,
                   create_priv, alter_priv, index_priv, drop_priv, create_tmp_table_priv,
                   grant_priv, lock_tables_priv, references_priv) 
          VALUES (
                   '%',
                   '{ $ocs{DbName} }',
                   '{ $ocs{DbUser} }',
                   'Y', 'Y', 'Y', 'Y',
                   'Y', 'Y', 'Y', 'Y', 'Y',
                   'N', 'Y', 'Y');

FLUSH PRIVILEGES;
