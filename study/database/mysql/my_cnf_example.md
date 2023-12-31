```mysql
[mysqld]
server-id=1

user=mysql
datadir=/data/mysql/
default_storage_engine=innodb
default_tmp_storage_engine=innodb
table_open_cache=30000
table_open_cache_instances=16

open-files-limit=65535
default-time-zone='+09:00'
socket=/tmp/mysql.sock
local_infile=OFF
block_encryption_mode='aes-256-ecb'

core_file
innodb_buffer_pool_in_core_file=OFF

max_allowed_packet=67108864
explicit_defaults_for_timestamp=ON
sql-mode="STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION"

character-set-server=utf8mb4
character-set-filesystem=utf8mb4
collation_server=utf8mb4_0900_ai_ci
skip-character-set-client-handshake

max_connections=100
max_connect_errors=999999

activate_all_roles_on_login=1
skip-name-resolve

ngram_token_size=2
max_heap_size=10M
tmp_table_size=10M
tmpdir=/data/mytmp/
secure-file-priv=/data/securefile/
default_password_lifetime=0

sysdate-is-now

#### InnoDB ---------------------------------------------------------------------------------------------------------
innodb_sort_buffer_size=5M


innodb_data_home_dir=/data/mysql/
innodb_data_file_path=ibdata1:100M:autoextend
innodb_temp_data_file_path=ibtmp1:12M:autoextend


innodb_log_group_home_dir=/log/innodb-log
innodb_log_files_in_group=2
innodb_log_file_size=1024M
innodb_file_per_table=ON


innodb_undo_directory=/log/innodb-undo/
innodb_rollback_segments=64
innodb_undo_tablespaces=2
innodb_max_undo_log_size=536870912
innodb_undo_log_truncate=ON


innodb_status_output_locks=ON
innodb_print_all_deadlocks=ON
innodb_adaptive_hash_index=OFF
innodb_buffer_pool_size=200M
innodb_buffer_pool_instances=1
innodb_doublewrite=OFF
innodb_checksum_algorithm=CRC32
innodb_flush_log_at_trx_commit=0
innodb_flush_method=O_DIRECT_NO_FSYNC
innodb_io_capacity=100
innodb_io_capacity_max=400
innodb_ft_enable_stopword=OFF
innodb_cmp_per_index_enable=ON


#### Performance schema
performance_schema=ON
performance-schema-instrument='stage/%=ON'
performance-schema-instrument='memory/%=ON'
performance-schema-instrument='wait/%=ON'


performance-schema-consumer-events_stages_current=ON
performance-schema-consumer-events_stages_history=ON
performance-schema-consumer-events_stages_history_long=ON
performance-schema-consumer-events_statements_history=OFF
performance-schema-consumer-events_statements_history_long=ON
performance-schema-consumer-events_waits_current=ON
performance-schema-consumer-events_waits_history=ON
performance-schema-consumer-events_waits_history_long=ON


performance_schema_events_stages_history_long_size=50000
performance_schema_events_stages_history_size=10
performance_schema_events_statements_history_long_size=50000
performance_schema_events_statements_history_size=10
performance_schema_events_waits_history_long_size=50000
performance_schema_events_waits_history_size=10


#### TDE (Encryption) ------------------------------------------------------------------------------------
early-plugin-load=keyring_file.so
keyring_file_data=/data/tde/tde_master.key

#### Password validate -----------------------------------------------------------------------------------
password_history=5
validate_password.length=8
validate_password.mixed_case_count=2
validate_password.number_count=2
validate_password.special_char_count=2
validate_password.dictionary_file=prohibitive_dictionary.data
validate_password.policy=STRONG


#### MySQL BinLog ----------------------------------------------------------------------------------------
log-bin=/log/mysql-bin/mysql-bin
sync_binlog=0
enforce_gtid_consistency=ON
gtid-mode=ON
binlog_checksum=CRC32
binlog_order_commits=ON
binlog_format=ROW
binlog_row_image=MINIMAL
max_binlog_size=104857600


#### MySQL Replica Options --------------------------------------------------------------------------------
slave_parallel_type=LOGICAL_CLOCK
slave_parallel_workers=4
slave_preserve_commit_order=1
binlog_rows_query_log_events=ON
log_slave_updates


#### Relay Log --------------------------------------------------------------------------------------------
relay-log=/log/relay-bin/relay-bin
relay_log_info_repository=TABLE
relay_log_recovery=ON
relay_log_purge=ON


#### MySQL ErrorLog ---------------------------------------------------------------------------------------
log-error=/log/mysql-err.log
log_error_verbosity=1


#### MySQL Slow Log ---------------------------------------------------------------------------------------
slow-query-log=1
long_query_time=1
log_slow_extra=1
log_slow_admin_statements=1
log_slow_slave_statements=1
slow_query_log_file=/log/mysql-slow.log


#### MySQL Log Expire -------------------------------------------------------------------------------------
binlog_expire_logs_seconds=259200
log-raw
log_timestamps=SYSTEM


[client]
socket=/tmp/mysql.sock
```

