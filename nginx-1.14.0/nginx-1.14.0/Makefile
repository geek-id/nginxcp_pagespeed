
CC =	cc
CFLAGS =  -pipe  -O -W -Wall -Wpointer-arith -Wno-unused-parameter -Werror -g   -D_GLIBCXX_USE_CXX11_ABI=0 -Wno-unused-local-typedefs -Wno-error
CPP =	cc -E
LINK =	$(CC)


ALL_INCS = -I src/core \
	-I src/event \
	-I src/event/modules \
	-I src/os/unix \
	-I /root/installer/publicnginx/pcre-8.35 \
	-I /root/installer/publicnginx/openssl-1.1.0h/.openssl/include \
	-I /root/installer/publicnginx/zlib-1.2.11 \
	-I nginx-1.14.0 \
	-I src/http \
	-I src/http/modules \
	-I src/http/v2 \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/chromium/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/google-sparsehash/src/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/google-sparsehash/gen/arch/linux/x64/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/grpc/src/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/protobuf/src/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/re2/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/out/Release/obj/gen \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/out/Release/obj/gen/protoc_out/instaweb \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/apr/src/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/aprutil/src/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/apr/gen/arch/linux/x64/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/aprutil/gen/arch/linux/x64/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/url \
	-I src/mail \
	-I src/stream


CORE_DEPS = src/core/nginx.h \
	src/core/ngx_config.h \
	src/core/ngx_core.h \
	src/core/ngx_log.h \
	src/core/ngx_palloc.h \
	src/core/ngx_array.h \
	src/core/ngx_list.h \
	src/core/ngx_hash.h \
	src/core/ngx_buf.h \
	src/core/ngx_queue.h \
	src/core/ngx_string.h \
	src/core/ngx_parse.h \
	src/core/ngx_parse_time.h \
	src/core/ngx_inet.h \
	src/core/ngx_file.h \
	src/core/ngx_crc.h \
	src/core/ngx_crc32.h \
	src/core/ngx_murmurhash.h \
	src/core/ngx_md5.h \
	src/core/ngx_sha1.h \
	src/core/ngx_rbtree.h \
	src/core/ngx_radix_tree.h \
	src/core/ngx_rwlock.h \
	src/core/ngx_slab.h \
	src/core/ngx_times.h \
	src/core/ngx_shmtx.h \
	src/core/ngx_connection.h \
	src/core/ngx_cycle.h \
	src/core/ngx_conf_file.h \
	src/core/ngx_module.h \
	src/core/ngx_resolver.h \
	src/core/ngx_open_file_cache.h \
	src/core/ngx_crypt.h \
	src/core/ngx_proxy_protocol.h \
	src/core/ngx_syslog.h \
	src/event/ngx_event.h \
	src/event/ngx_event_timer.h \
	src/event/ngx_event_posted.h \
	src/event/ngx_event_connect.h \
	src/event/ngx_event_pipe.h \
	src/os/unix/ngx_time.h \
	src/os/unix/ngx_errno.h \
	src/os/unix/ngx_alloc.h \
	src/os/unix/ngx_files.h \
	src/os/unix/ngx_channel.h \
	src/os/unix/ngx_shmem.h \
	src/os/unix/ngx_process.h \
	src/os/unix/ngx_setaffinity.h \
	src/os/unix/ngx_setproctitle.h \
	src/os/unix/ngx_atomic.h \
	src/os/unix/ngx_gcc_atomic_x86.h \
	src/os/unix/ngx_thread.h \
	src/os/unix/ngx_socket.h \
	src/os/unix/ngx_os.h \
	src/os/unix/ngx_user.h \
	src/os/unix/ngx_dlopen.h \
	src/os/unix/ngx_process_cycle.h \
	src/os/unix/ngx_linux_config.h \
	src/os/unix/ngx_linux.h \
	src/core/ngx_thread_pool.h \
	src/event/ngx_event_openssl.h \
	src/core/ngx_regex.h \
	/root/installer/publicnginx/pcre-8.35/pcre.h \
	/root/installer/publicnginx/openssl-1.1.0h/.openssl/include/openssl/ssl.h \
	nginx-1.14.0/ngx_auto_config.h


CORE_INCS = -I src/core \
	-I src/event \
	-I src/event/modules \
	-I src/os/unix \
	-I /root/installer/publicnginx/pcre-8.35 \
	-I /root/installer/publicnginx/openssl-1.1.0h/.openssl/include \
	-I /root/installer/publicnginx/zlib-1.2.11 \
	-I nginx-1.14.0


HTTP_DEPS = src/http/ngx_http.h \
	src/http/ngx_http_request.h \
	src/http/ngx_http_config.h \
	src/http/ngx_http_core_module.h \
	src/http/ngx_http_cache.h \
	src/http/ngx_http_variables.h \
	src/http/ngx_http_script.h \
	src/http/ngx_http_upstream.h \
	src/http/ngx_http_upstream_round_robin.h \
	src/http/modules/ngx_http_ssi_filter_module.h \
	src/http/v2/ngx_http_v2.h \
	src/http/v2/ngx_http_v2_module.h \
	src/http/modules/ngx_http_ssl_module.h


HTTP_INCS = -I src/http \
	-I src/http/modules \
	-I src/http/v2 \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/chromium/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/google-sparsehash/src/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/google-sparsehash/gen/arch/linux/x64/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/grpc/src/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/protobuf/src/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/re2/src \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/out/Release/obj/gen \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/out/Release/obj/gen/protoc_out/instaweb \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/apr/src/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/aprutil/src/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/apr/gen/arch/linux/x64/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/third_party/aprutil/gen/arch/linux/x64/include \
	-I /root/installer/publicnginx/ngx_pagespeed/psol/include/url


MAIL_DEPS = src/mail/ngx_mail.h \
	src/mail/ngx_mail_ssl_module.h \
	src/mail/ngx_mail_pop3_module.h \
	src/mail/ngx_mail_imap_module.h \
	src/mail/ngx_mail_smtp_module.h


MAIL_INCS = -I src/mail


STREAM_DEPS = src/stream/ngx_stream.h \
	src/stream/ngx_stream_variables.h \
	src/stream/ngx_stream_script.h \
	src/stream/ngx_stream_upstream.h \
	src/stream/ngx_stream_upstream_round_robin.h \
	src/stream/ngx_stream_ssl_module.h


STREAM_INCS = -I src/stream


ADDON_DEPS = $(CORE_DEPS)  /root/installer/publicnginx/ngx_pagespeed/src/log_message_handler.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_base_fetch.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_caching_headers.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_event_connection.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_fetch.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_gzip_setter.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_list_iterator.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_message_handler.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_pagespeed.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_rewrite_driver_factory.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_rewrite_options.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_server_context.h /root/installer/publicnginx/ngx_pagespeed/src/ngx_url_async_fetcher.h /root/installer/publicnginx/ngx_pagespeed/psol/lib/Release/linux/x64/pagespeed_automatic.a $(HTTP_DEPS) $(MAIL_DEPS) $(STREAM_DEPS)


build:	binary modules manpage

binary:	nginx-1.14.0/nginx

nginx-1.14.0/nginx:	nginx-1.14.0/src/core/nginx.o \
	nginx-1.14.0/src/core/ngx_log.o \
	nginx-1.14.0/src/core/ngx_palloc.o \
	nginx-1.14.0/src/core/ngx_array.o \
	nginx-1.14.0/src/core/ngx_list.o \
	nginx-1.14.0/src/core/ngx_hash.o \
	nginx-1.14.0/src/core/ngx_buf.o \
	nginx-1.14.0/src/core/ngx_queue.o \
	nginx-1.14.0/src/core/ngx_output_chain.o \
	nginx-1.14.0/src/core/ngx_string.o \
	nginx-1.14.0/src/core/ngx_parse.o \
	nginx-1.14.0/src/core/ngx_parse_time.o \
	nginx-1.14.0/src/core/ngx_inet.o \
	nginx-1.14.0/src/core/ngx_file.o \
	nginx-1.14.0/src/core/ngx_crc32.o \
	nginx-1.14.0/src/core/ngx_murmurhash.o \
	nginx-1.14.0/src/core/ngx_md5.o \
	nginx-1.14.0/src/core/ngx_sha1.o \
	nginx-1.14.0/src/core/ngx_rbtree.o \
	nginx-1.14.0/src/core/ngx_radix_tree.o \
	nginx-1.14.0/src/core/ngx_slab.o \
	nginx-1.14.0/src/core/ngx_times.o \
	nginx-1.14.0/src/core/ngx_shmtx.o \
	nginx-1.14.0/src/core/ngx_connection.o \
	nginx-1.14.0/src/core/ngx_cycle.o \
	nginx-1.14.0/src/core/ngx_spinlock.o \
	nginx-1.14.0/src/core/ngx_rwlock.o \
	nginx-1.14.0/src/core/ngx_cpuinfo.o \
	nginx-1.14.0/src/core/ngx_conf_file.o \
	nginx-1.14.0/src/core/ngx_module.o \
	nginx-1.14.0/src/core/ngx_resolver.o \
	nginx-1.14.0/src/core/ngx_open_file_cache.o \
	nginx-1.14.0/src/core/ngx_crypt.o \
	nginx-1.14.0/src/core/ngx_proxy_protocol.o \
	nginx-1.14.0/src/core/ngx_syslog.o \
	nginx-1.14.0/src/event/ngx_event.o \
	nginx-1.14.0/src/event/ngx_event_timer.o \
	nginx-1.14.0/src/event/ngx_event_posted.o \
	nginx-1.14.0/src/event/ngx_event_accept.o \
	nginx-1.14.0/src/event/ngx_event_connect.o \
	nginx-1.14.0/src/event/ngx_event_pipe.o \
	nginx-1.14.0/src/os/unix/ngx_time.o \
	nginx-1.14.0/src/os/unix/ngx_errno.o \
	nginx-1.14.0/src/os/unix/ngx_alloc.o \
	nginx-1.14.0/src/os/unix/ngx_files.o \
	nginx-1.14.0/src/os/unix/ngx_socket.o \
	nginx-1.14.0/src/os/unix/ngx_recv.o \
	nginx-1.14.0/src/os/unix/ngx_readv_chain.o \
	nginx-1.14.0/src/os/unix/ngx_udp_recv.o \
	nginx-1.14.0/src/os/unix/ngx_send.o \
	nginx-1.14.0/src/os/unix/ngx_writev_chain.o \
	nginx-1.14.0/src/os/unix/ngx_udp_send.o \
	nginx-1.14.0/src/os/unix/ngx_udp_sendmsg_chain.o \
	nginx-1.14.0/src/os/unix/ngx_channel.o \
	nginx-1.14.0/src/os/unix/ngx_shmem.o \
	nginx-1.14.0/src/os/unix/ngx_process.o \
	nginx-1.14.0/src/os/unix/ngx_daemon.o \
	nginx-1.14.0/src/os/unix/ngx_setaffinity.o \
	nginx-1.14.0/src/os/unix/ngx_setproctitle.o \
	nginx-1.14.0/src/os/unix/ngx_posix_init.o \
	nginx-1.14.0/src/os/unix/ngx_user.o \
	nginx-1.14.0/src/os/unix/ngx_dlopen.o \
	nginx-1.14.0/src/os/unix/ngx_process_cycle.o \
	nginx-1.14.0/src/os/unix/ngx_linux_init.o \
	nginx-1.14.0/src/event/modules/ngx_epoll_module.o \
	nginx-1.14.0/src/os/unix/ngx_linux_sendfile_chain.o \
	nginx-1.14.0/src/os/unix/ngx_linux_aio_read.o \
	nginx-1.14.0/src/core/ngx_thread_pool.o \
	nginx-1.14.0/src/os/unix/ngx_thread_cond.o \
	nginx-1.14.0/src/os/unix/ngx_thread_mutex.o \
	nginx-1.14.0/src/os/unix/ngx_thread_id.o \
	nginx-1.14.0/src/event/modules/ngx_select_module.o \
	nginx-1.14.0/src/event/modules/ngx_poll_module.o \
	nginx-1.14.0/src/event/ngx_event_openssl.o \
	nginx-1.14.0/src/event/ngx_event_openssl_stapling.o \
	nginx-1.14.0/src/core/ngx_regex.o \
	nginx-1.14.0/src/http/ngx_http.o \
	nginx-1.14.0/src/http/ngx_http_core_module.o \
	nginx-1.14.0/src/http/ngx_http_special_response.o \
	nginx-1.14.0/src/http/ngx_http_request.o \
	nginx-1.14.0/src/http/ngx_http_parse.o \
	nginx-1.14.0/src/http/modules/ngx_http_log_module.o \
	nginx-1.14.0/src/http/ngx_http_request_body.o \
	nginx-1.14.0/src/http/ngx_http_variables.o \
	nginx-1.14.0/src/http/ngx_http_script.o \
	nginx-1.14.0/src/http/ngx_http_upstream.o \
	nginx-1.14.0/src/http/ngx_http_upstream_round_robin.o \
	nginx-1.14.0/src/http/ngx_http_file_cache.o \
	nginx-1.14.0/src/http/ngx_http_write_filter_module.o \
	nginx-1.14.0/src/http/ngx_http_header_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_chunked_filter_module.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_range_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_gzip_filter_module.o \
	nginx-1.14.0/src/http/ngx_http_postpone_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_ssi_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_charset_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_sub_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_addition_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_gunzip_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_userid_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_headers_filter_module.o \
	nginx-1.14.0/src/http/ngx_http_copy_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_not_modified_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_slice_filter_module.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_table.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_encode.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_huff_decode.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_huff_encode.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_static_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_gzip_static_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_dav_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_autoindex_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_index_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_random_index_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_mirror_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_try_files_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_auth_request_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_auth_basic_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_access_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_limit_conn_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_limit_req_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_realip_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_geo_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_map_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_split_clients_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_referer_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_rewrite_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_ssl_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_proxy_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_fastcgi_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_uwsgi_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_scgi_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_grpc_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_memcached_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_empty_gif_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_browser_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_secure_link_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_degradation_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_flv_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_mp4_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_hash_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_ip_hash_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_least_conn_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_keepalive_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_zone_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_stub_status_module.o \
	nginx-1.14.0/addon/src/log_message_handler.o \
	nginx-1.14.0/addon/src/ngx_base_fetch.o \
	nginx-1.14.0/addon/src/ngx_caching_headers.o \
	nginx-1.14.0/addon/src/ngx_event_connection.o \
	nginx-1.14.0/addon/src/ngx_fetch.o \
	nginx-1.14.0/addon/src/ngx_gzip_setter.o \
	nginx-1.14.0/addon/src/ngx_list_iterator.o \
	nginx-1.14.0/addon/src/ngx_message_handler.o \
	nginx-1.14.0/addon/src/ngx_pagespeed.o \
	nginx-1.14.0/addon/src/ngx_rewrite_driver_factory.o \
	nginx-1.14.0/addon/src/ngx_rewrite_options.o \
	nginx-1.14.0/addon/src/ngx_server_context.o \
	nginx-1.14.0/addon/src/ngx_url_async_fetcher.o \
	nginx-1.14.0/ngx_modules.o \
	/root/installer/publicnginx/pcre-8.35/.libs/libpcre.a \
	/root/installer/publicnginx/zlib-1.2.11/libz.a

	$(LINK) -o nginx-1.14.0/nginx \
	nginx-1.14.0/src/core/nginx.o \
	nginx-1.14.0/src/core/ngx_log.o \
	nginx-1.14.0/src/core/ngx_palloc.o \
	nginx-1.14.0/src/core/ngx_array.o \
	nginx-1.14.0/src/core/ngx_list.o \
	nginx-1.14.0/src/core/ngx_hash.o \
	nginx-1.14.0/src/core/ngx_buf.o \
	nginx-1.14.0/src/core/ngx_queue.o \
	nginx-1.14.0/src/core/ngx_output_chain.o \
	nginx-1.14.0/src/core/ngx_string.o \
	nginx-1.14.0/src/core/ngx_parse.o \
	nginx-1.14.0/src/core/ngx_parse_time.o \
	nginx-1.14.0/src/core/ngx_inet.o \
	nginx-1.14.0/src/core/ngx_file.o \
	nginx-1.14.0/src/core/ngx_crc32.o \
	nginx-1.14.0/src/core/ngx_murmurhash.o \
	nginx-1.14.0/src/core/ngx_md5.o \
	nginx-1.14.0/src/core/ngx_sha1.o \
	nginx-1.14.0/src/core/ngx_rbtree.o \
	nginx-1.14.0/src/core/ngx_radix_tree.o \
	nginx-1.14.0/src/core/ngx_slab.o \
	nginx-1.14.0/src/core/ngx_times.o \
	nginx-1.14.0/src/core/ngx_shmtx.o \
	nginx-1.14.0/src/core/ngx_connection.o \
	nginx-1.14.0/src/core/ngx_cycle.o \
	nginx-1.14.0/src/core/ngx_spinlock.o \
	nginx-1.14.0/src/core/ngx_rwlock.o \
	nginx-1.14.0/src/core/ngx_cpuinfo.o \
	nginx-1.14.0/src/core/ngx_conf_file.o \
	nginx-1.14.0/src/core/ngx_module.o \
	nginx-1.14.0/src/core/ngx_resolver.o \
	nginx-1.14.0/src/core/ngx_open_file_cache.o \
	nginx-1.14.0/src/core/ngx_crypt.o \
	nginx-1.14.0/src/core/ngx_proxy_protocol.o \
	nginx-1.14.0/src/core/ngx_syslog.o \
	nginx-1.14.0/src/event/ngx_event.o \
	nginx-1.14.0/src/event/ngx_event_timer.o \
	nginx-1.14.0/src/event/ngx_event_posted.o \
	nginx-1.14.0/src/event/ngx_event_accept.o \
	nginx-1.14.0/src/event/ngx_event_connect.o \
	nginx-1.14.0/src/event/ngx_event_pipe.o \
	nginx-1.14.0/src/os/unix/ngx_time.o \
	nginx-1.14.0/src/os/unix/ngx_errno.o \
	nginx-1.14.0/src/os/unix/ngx_alloc.o \
	nginx-1.14.0/src/os/unix/ngx_files.o \
	nginx-1.14.0/src/os/unix/ngx_socket.o \
	nginx-1.14.0/src/os/unix/ngx_recv.o \
	nginx-1.14.0/src/os/unix/ngx_readv_chain.o \
	nginx-1.14.0/src/os/unix/ngx_udp_recv.o \
	nginx-1.14.0/src/os/unix/ngx_send.o \
	nginx-1.14.0/src/os/unix/ngx_writev_chain.o \
	nginx-1.14.0/src/os/unix/ngx_udp_send.o \
	nginx-1.14.0/src/os/unix/ngx_udp_sendmsg_chain.o \
	nginx-1.14.0/src/os/unix/ngx_channel.o \
	nginx-1.14.0/src/os/unix/ngx_shmem.o \
	nginx-1.14.0/src/os/unix/ngx_process.o \
	nginx-1.14.0/src/os/unix/ngx_daemon.o \
	nginx-1.14.0/src/os/unix/ngx_setaffinity.o \
	nginx-1.14.0/src/os/unix/ngx_setproctitle.o \
	nginx-1.14.0/src/os/unix/ngx_posix_init.o \
	nginx-1.14.0/src/os/unix/ngx_user.o \
	nginx-1.14.0/src/os/unix/ngx_dlopen.o \
	nginx-1.14.0/src/os/unix/ngx_process_cycle.o \
	nginx-1.14.0/src/os/unix/ngx_linux_init.o \
	nginx-1.14.0/src/event/modules/ngx_epoll_module.o \
	nginx-1.14.0/src/os/unix/ngx_linux_sendfile_chain.o \
	nginx-1.14.0/src/os/unix/ngx_linux_aio_read.o \
	nginx-1.14.0/src/core/ngx_thread_pool.o \
	nginx-1.14.0/src/os/unix/ngx_thread_cond.o \
	nginx-1.14.0/src/os/unix/ngx_thread_mutex.o \
	nginx-1.14.0/src/os/unix/ngx_thread_id.o \
	nginx-1.14.0/src/event/modules/ngx_select_module.o \
	nginx-1.14.0/src/event/modules/ngx_poll_module.o \
	nginx-1.14.0/src/event/ngx_event_openssl.o \
	nginx-1.14.0/src/event/ngx_event_openssl_stapling.o \
	nginx-1.14.0/src/core/ngx_regex.o \
	nginx-1.14.0/src/http/ngx_http.o \
	nginx-1.14.0/src/http/ngx_http_core_module.o \
	nginx-1.14.0/src/http/ngx_http_special_response.o \
	nginx-1.14.0/src/http/ngx_http_request.o \
	nginx-1.14.0/src/http/ngx_http_parse.o \
	nginx-1.14.0/src/http/modules/ngx_http_log_module.o \
	nginx-1.14.0/src/http/ngx_http_request_body.o \
	nginx-1.14.0/src/http/ngx_http_variables.o \
	nginx-1.14.0/src/http/ngx_http_script.o \
	nginx-1.14.0/src/http/ngx_http_upstream.o \
	nginx-1.14.0/src/http/ngx_http_upstream_round_robin.o \
	nginx-1.14.0/src/http/ngx_http_file_cache.o \
	nginx-1.14.0/src/http/ngx_http_write_filter_module.o \
	nginx-1.14.0/src/http/ngx_http_header_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_chunked_filter_module.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_range_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_gzip_filter_module.o \
	nginx-1.14.0/src/http/ngx_http_postpone_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_ssi_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_charset_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_sub_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_addition_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_gunzip_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_userid_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_headers_filter_module.o \
	nginx-1.14.0/src/http/ngx_http_copy_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_not_modified_filter_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_slice_filter_module.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_table.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_encode.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_huff_decode.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_huff_encode.o \
	nginx-1.14.0/src/http/v2/ngx_http_v2_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_static_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_gzip_static_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_dav_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_autoindex_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_index_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_random_index_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_mirror_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_try_files_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_auth_request_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_auth_basic_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_access_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_limit_conn_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_limit_req_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_realip_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_geo_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_map_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_split_clients_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_referer_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_rewrite_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_ssl_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_proxy_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_fastcgi_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_uwsgi_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_scgi_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_grpc_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_memcached_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_empty_gif_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_browser_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_secure_link_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_degradation_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_flv_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_mp4_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_hash_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_ip_hash_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_least_conn_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_keepalive_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_upstream_zone_module.o \
	nginx-1.14.0/src/http/modules/ngx_http_stub_status_module.o \
	nginx-1.14.0/addon/src/log_message_handler.o \
	nginx-1.14.0/addon/src/ngx_base_fetch.o \
	nginx-1.14.0/addon/src/ngx_caching_headers.o \
	nginx-1.14.0/addon/src/ngx_event_connection.o \
	nginx-1.14.0/addon/src/ngx_fetch.o \
	nginx-1.14.0/addon/src/ngx_gzip_setter.o \
	nginx-1.14.0/addon/src/ngx_list_iterator.o \
	nginx-1.14.0/addon/src/ngx_message_handler.o \
	nginx-1.14.0/addon/src/ngx_pagespeed.o \
	nginx-1.14.0/addon/src/ngx_rewrite_driver_factory.o \
	nginx-1.14.0/addon/src/ngx_rewrite_options.o \
	nginx-1.14.0/addon/src/ngx_server_context.o \
	nginx-1.14.0/addon/src/ngx_url_async_fetcher.o \
	nginx-1.14.0/ngx_modules.o \
	-ldl -lpthread -lpthread -lcrypt /root/installer/publicnginx/ngx_pagespeed/psol/lib/Release/linux/x64/pagespeed_automatic.a -lstdc++ -lrt -pthread -lm /root/installer/publicnginx/pcre-8.35/.libs/libpcre.a /root/installer/publicnginx/openssl-1.1.0h/.openssl/lib/libssl.a /root/installer/publicnginx/openssl-1.1.0h/.openssl/lib/libcrypto.a -ldl -lpthread /root/installer/publicnginx/zlib-1.2.11/libz.a \
	-Wl,-E
	


modules:

nginx-1.14.0/ngx_modules.o:	$(CORE_DEPS) \
	nginx-1.14.0/ngx_modules.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/ngx_modules.o \
		nginx-1.14.0/ngx_modules.c


nginx-1.14.0/src/core/nginx.o:	$(CORE_DEPS) \
	src/core/nginx.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/nginx.o \
		src/core/nginx.c


nginx-1.14.0/src/core/ngx_log.o:	$(CORE_DEPS) \
	src/core/ngx_log.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_log.o \
		src/core/ngx_log.c


nginx-1.14.0/src/core/ngx_palloc.o:	$(CORE_DEPS) \
	src/core/ngx_palloc.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_palloc.o \
		src/core/ngx_palloc.c


nginx-1.14.0/src/core/ngx_array.o:	$(CORE_DEPS) \
	src/core/ngx_array.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_array.o \
		src/core/ngx_array.c


nginx-1.14.0/src/core/ngx_list.o:	$(CORE_DEPS) \
	src/core/ngx_list.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_list.o \
		src/core/ngx_list.c


nginx-1.14.0/src/core/ngx_hash.o:	$(CORE_DEPS) \
	src/core/ngx_hash.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_hash.o \
		src/core/ngx_hash.c


nginx-1.14.0/src/core/ngx_buf.o:	$(CORE_DEPS) \
	src/core/ngx_buf.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_buf.o \
		src/core/ngx_buf.c


nginx-1.14.0/src/core/ngx_queue.o:	$(CORE_DEPS) \
	src/core/ngx_queue.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_queue.o \
		src/core/ngx_queue.c


nginx-1.14.0/src/core/ngx_output_chain.o:	$(CORE_DEPS) \
	src/core/ngx_output_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_output_chain.o \
		src/core/ngx_output_chain.c


nginx-1.14.0/src/core/ngx_string.o:	$(CORE_DEPS) \
	src/core/ngx_string.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_string.o \
		src/core/ngx_string.c


nginx-1.14.0/src/core/ngx_parse.o:	$(CORE_DEPS) \
	src/core/ngx_parse.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_parse.o \
		src/core/ngx_parse.c


nginx-1.14.0/src/core/ngx_parse_time.o:	$(CORE_DEPS) \
	src/core/ngx_parse_time.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_parse_time.o \
		src/core/ngx_parse_time.c


nginx-1.14.0/src/core/ngx_inet.o:	$(CORE_DEPS) \
	src/core/ngx_inet.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_inet.o \
		src/core/ngx_inet.c


nginx-1.14.0/src/core/ngx_file.o:	$(CORE_DEPS) \
	src/core/ngx_file.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_file.o \
		src/core/ngx_file.c


nginx-1.14.0/src/core/ngx_crc32.o:	$(CORE_DEPS) \
	src/core/ngx_crc32.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_crc32.o \
		src/core/ngx_crc32.c


nginx-1.14.0/src/core/ngx_murmurhash.o:	$(CORE_DEPS) \
	src/core/ngx_murmurhash.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_murmurhash.o \
		src/core/ngx_murmurhash.c


nginx-1.14.0/src/core/ngx_md5.o:	$(CORE_DEPS) \
	src/core/ngx_md5.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_md5.o \
		src/core/ngx_md5.c


nginx-1.14.0/src/core/ngx_sha1.o:	$(CORE_DEPS) \
	src/core/ngx_sha1.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_sha1.o \
		src/core/ngx_sha1.c


nginx-1.14.0/src/core/ngx_rbtree.o:	$(CORE_DEPS) \
	src/core/ngx_rbtree.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_rbtree.o \
		src/core/ngx_rbtree.c


nginx-1.14.0/src/core/ngx_radix_tree.o:	$(CORE_DEPS) \
	src/core/ngx_radix_tree.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_radix_tree.o \
		src/core/ngx_radix_tree.c


nginx-1.14.0/src/core/ngx_slab.o:	$(CORE_DEPS) \
	src/core/ngx_slab.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_slab.o \
		src/core/ngx_slab.c


nginx-1.14.0/src/core/ngx_times.o:	$(CORE_DEPS) \
	src/core/ngx_times.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_times.o \
		src/core/ngx_times.c


nginx-1.14.0/src/core/ngx_shmtx.o:	$(CORE_DEPS) \
	src/core/ngx_shmtx.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_shmtx.o \
		src/core/ngx_shmtx.c


nginx-1.14.0/src/core/ngx_connection.o:	$(CORE_DEPS) \
	src/core/ngx_connection.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_connection.o \
		src/core/ngx_connection.c


nginx-1.14.0/src/core/ngx_cycle.o:	$(CORE_DEPS) \
	src/core/ngx_cycle.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_cycle.o \
		src/core/ngx_cycle.c


nginx-1.14.0/src/core/ngx_spinlock.o:	$(CORE_DEPS) \
	src/core/ngx_spinlock.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_spinlock.o \
		src/core/ngx_spinlock.c


nginx-1.14.0/src/core/ngx_rwlock.o:	$(CORE_DEPS) \
	src/core/ngx_rwlock.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_rwlock.o \
		src/core/ngx_rwlock.c


nginx-1.14.0/src/core/ngx_cpuinfo.o:	$(CORE_DEPS) \
	src/core/ngx_cpuinfo.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_cpuinfo.o \
		src/core/ngx_cpuinfo.c


nginx-1.14.0/src/core/ngx_conf_file.o:	$(CORE_DEPS) \
	src/core/ngx_conf_file.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_conf_file.o \
		src/core/ngx_conf_file.c


nginx-1.14.0/src/core/ngx_module.o:	$(CORE_DEPS) \
	src/core/ngx_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_module.o \
		src/core/ngx_module.c


nginx-1.14.0/src/core/ngx_resolver.o:	$(CORE_DEPS) \
	src/core/ngx_resolver.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_resolver.o \
		src/core/ngx_resolver.c


nginx-1.14.0/src/core/ngx_open_file_cache.o:	$(CORE_DEPS) \
	src/core/ngx_open_file_cache.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_open_file_cache.o \
		src/core/ngx_open_file_cache.c


nginx-1.14.0/src/core/ngx_crypt.o:	$(CORE_DEPS) \
	src/core/ngx_crypt.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_crypt.o \
		src/core/ngx_crypt.c


nginx-1.14.0/src/core/ngx_proxy_protocol.o:	$(CORE_DEPS) \
	src/core/ngx_proxy_protocol.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_proxy_protocol.o \
		src/core/ngx_proxy_protocol.c


nginx-1.14.0/src/core/ngx_syslog.o:	$(CORE_DEPS) \
	src/core/ngx_syslog.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_syslog.o \
		src/core/ngx_syslog.c


nginx-1.14.0/src/event/ngx_event.o:	$(CORE_DEPS) \
	src/event/ngx_event.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event.o \
		src/event/ngx_event.c


nginx-1.14.0/src/event/ngx_event_timer.o:	$(CORE_DEPS) \
	src/event/ngx_event_timer.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_timer.o \
		src/event/ngx_event_timer.c


nginx-1.14.0/src/event/ngx_event_posted.o:	$(CORE_DEPS) \
	src/event/ngx_event_posted.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_posted.o \
		src/event/ngx_event_posted.c


nginx-1.14.0/src/event/ngx_event_accept.o:	$(CORE_DEPS) \
	src/event/ngx_event_accept.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_accept.o \
		src/event/ngx_event_accept.c


nginx-1.14.0/src/event/ngx_event_connect.o:	$(CORE_DEPS) \
	src/event/ngx_event_connect.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_connect.o \
		src/event/ngx_event_connect.c


nginx-1.14.0/src/event/ngx_event_pipe.o:	$(CORE_DEPS) \
	src/event/ngx_event_pipe.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_pipe.o \
		src/event/ngx_event_pipe.c


nginx-1.14.0/src/os/unix/ngx_time.o:	$(CORE_DEPS) \
	src/os/unix/ngx_time.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_time.o \
		src/os/unix/ngx_time.c


nginx-1.14.0/src/os/unix/ngx_errno.o:	$(CORE_DEPS) \
	src/os/unix/ngx_errno.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_errno.o \
		src/os/unix/ngx_errno.c


nginx-1.14.0/src/os/unix/ngx_alloc.o:	$(CORE_DEPS) \
	src/os/unix/ngx_alloc.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_alloc.o \
		src/os/unix/ngx_alloc.c


nginx-1.14.0/src/os/unix/ngx_files.o:	$(CORE_DEPS) \
	src/os/unix/ngx_files.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_files.o \
		src/os/unix/ngx_files.c


nginx-1.14.0/src/os/unix/ngx_socket.o:	$(CORE_DEPS) \
	src/os/unix/ngx_socket.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_socket.o \
		src/os/unix/ngx_socket.c


nginx-1.14.0/src/os/unix/ngx_recv.o:	$(CORE_DEPS) \
	src/os/unix/ngx_recv.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_recv.o \
		src/os/unix/ngx_recv.c


nginx-1.14.0/src/os/unix/ngx_readv_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_readv_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_readv_chain.o \
		src/os/unix/ngx_readv_chain.c


nginx-1.14.0/src/os/unix/ngx_udp_recv.o:	$(CORE_DEPS) \
	src/os/unix/ngx_udp_recv.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_udp_recv.o \
		src/os/unix/ngx_udp_recv.c


nginx-1.14.0/src/os/unix/ngx_send.o:	$(CORE_DEPS) \
	src/os/unix/ngx_send.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_send.o \
		src/os/unix/ngx_send.c


nginx-1.14.0/src/os/unix/ngx_writev_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_writev_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_writev_chain.o \
		src/os/unix/ngx_writev_chain.c


nginx-1.14.0/src/os/unix/ngx_udp_send.o:	$(CORE_DEPS) \
	src/os/unix/ngx_udp_send.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_udp_send.o \
		src/os/unix/ngx_udp_send.c


nginx-1.14.0/src/os/unix/ngx_udp_sendmsg_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_udp_sendmsg_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_udp_sendmsg_chain.o \
		src/os/unix/ngx_udp_sendmsg_chain.c


nginx-1.14.0/src/os/unix/ngx_channel.o:	$(CORE_DEPS) \
	src/os/unix/ngx_channel.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_channel.o \
		src/os/unix/ngx_channel.c


nginx-1.14.0/src/os/unix/ngx_shmem.o:	$(CORE_DEPS) \
	src/os/unix/ngx_shmem.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_shmem.o \
		src/os/unix/ngx_shmem.c


nginx-1.14.0/src/os/unix/ngx_process.o:	$(CORE_DEPS) \
	src/os/unix/ngx_process.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_process.o \
		src/os/unix/ngx_process.c


nginx-1.14.0/src/os/unix/ngx_daemon.o:	$(CORE_DEPS) \
	src/os/unix/ngx_daemon.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_daemon.o \
		src/os/unix/ngx_daemon.c


nginx-1.14.0/src/os/unix/ngx_setaffinity.o:	$(CORE_DEPS) \
	src/os/unix/ngx_setaffinity.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_setaffinity.o \
		src/os/unix/ngx_setaffinity.c


nginx-1.14.0/src/os/unix/ngx_setproctitle.o:	$(CORE_DEPS) \
	src/os/unix/ngx_setproctitle.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_setproctitle.o \
		src/os/unix/ngx_setproctitle.c


nginx-1.14.0/src/os/unix/ngx_posix_init.o:	$(CORE_DEPS) \
	src/os/unix/ngx_posix_init.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_posix_init.o \
		src/os/unix/ngx_posix_init.c


nginx-1.14.0/src/os/unix/ngx_user.o:	$(CORE_DEPS) \
	src/os/unix/ngx_user.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_user.o \
		src/os/unix/ngx_user.c


nginx-1.14.0/src/os/unix/ngx_dlopen.o:	$(CORE_DEPS) \
	src/os/unix/ngx_dlopen.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_dlopen.o \
		src/os/unix/ngx_dlopen.c


nginx-1.14.0/src/os/unix/ngx_process_cycle.o:	$(CORE_DEPS) \
	src/os/unix/ngx_process_cycle.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_process_cycle.o \
		src/os/unix/ngx_process_cycle.c


nginx-1.14.0/src/os/unix/ngx_linux_init.o:	$(CORE_DEPS) \
	src/os/unix/ngx_linux_init.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_linux_init.o \
		src/os/unix/ngx_linux_init.c


nginx-1.14.0/src/event/modules/ngx_epoll_module.o:	$(CORE_DEPS) \
	src/event/modules/ngx_epoll_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/modules/ngx_epoll_module.o \
		src/event/modules/ngx_epoll_module.c


nginx-1.14.0/src/os/unix/ngx_linux_sendfile_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_linux_sendfile_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_linux_sendfile_chain.o \
		src/os/unix/ngx_linux_sendfile_chain.c


nginx-1.14.0/src/os/unix/ngx_linux_aio_read.o:	$(CORE_DEPS) \
	src/os/unix/ngx_linux_aio_read.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_linux_aio_read.o \
		src/os/unix/ngx_linux_aio_read.c


nginx-1.14.0/src/core/ngx_thread_pool.o:	$(CORE_DEPS) \
	src/core/ngx_thread_pool.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_thread_pool.o \
		src/core/ngx_thread_pool.c


nginx-1.14.0/src/os/unix/ngx_thread_cond.o:	$(CORE_DEPS) \
	src/os/unix/ngx_thread_cond.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_thread_cond.o \
		src/os/unix/ngx_thread_cond.c


nginx-1.14.0/src/os/unix/ngx_thread_mutex.o:	$(CORE_DEPS) \
	src/os/unix/ngx_thread_mutex.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_thread_mutex.o \
		src/os/unix/ngx_thread_mutex.c


nginx-1.14.0/src/os/unix/ngx_thread_id.o:	$(CORE_DEPS) \
	src/os/unix/ngx_thread_id.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/os/unix/ngx_thread_id.o \
		src/os/unix/ngx_thread_id.c


nginx-1.14.0/src/event/modules/ngx_select_module.o:	$(CORE_DEPS) \
	src/event/modules/ngx_select_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/modules/ngx_select_module.o \
		src/event/modules/ngx_select_module.c


nginx-1.14.0/src/event/modules/ngx_poll_module.o:	$(CORE_DEPS) \
	src/event/modules/ngx_poll_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/modules/ngx_poll_module.o \
		src/event/modules/ngx_poll_module.c


nginx-1.14.0/src/event/ngx_event_openssl.o:	$(CORE_DEPS) \
	src/event/ngx_event_openssl.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_openssl.o \
		src/event/ngx_event_openssl.c


nginx-1.14.0/src/event/ngx_event_openssl_stapling.o:	$(CORE_DEPS) \
	src/event/ngx_event_openssl_stapling.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/event/ngx_event_openssl_stapling.o \
		src/event/ngx_event_openssl_stapling.c


nginx-1.14.0/src/core/ngx_regex.o:	$(CORE_DEPS) \
	src/core/ngx_regex.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o nginx-1.14.0/src/core/ngx_regex.o \
		src/core/ngx_regex.c


nginx-1.14.0/src/http/ngx_http.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http.o \
		src/http/ngx_http.c


nginx-1.14.0/src/http/ngx_http_core_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_core_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_core_module.o \
		src/http/ngx_http_core_module.c


nginx-1.14.0/src/http/ngx_http_special_response.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_special_response.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_special_response.o \
		src/http/ngx_http_special_response.c


nginx-1.14.0/src/http/ngx_http_request.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_request.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_request.o \
		src/http/ngx_http_request.c


nginx-1.14.0/src/http/ngx_http_parse.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_parse.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_parse.o \
		src/http/ngx_http_parse.c


nginx-1.14.0/src/http/modules/ngx_http_log_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_log_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_log_module.o \
		src/http/modules/ngx_http_log_module.c


nginx-1.14.0/src/http/ngx_http_request_body.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_request_body.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_request_body.o \
		src/http/ngx_http_request_body.c


nginx-1.14.0/src/http/ngx_http_variables.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_variables.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_variables.o \
		src/http/ngx_http_variables.c


nginx-1.14.0/src/http/ngx_http_script.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_script.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_script.o \
		src/http/ngx_http_script.c


nginx-1.14.0/src/http/ngx_http_upstream.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_upstream.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_upstream.o \
		src/http/ngx_http_upstream.c


nginx-1.14.0/src/http/ngx_http_upstream_round_robin.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_upstream_round_robin.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_upstream_round_robin.o \
		src/http/ngx_http_upstream_round_robin.c


nginx-1.14.0/src/http/ngx_http_file_cache.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_file_cache.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_file_cache.o \
		src/http/ngx_http_file_cache.c


nginx-1.14.0/src/http/ngx_http_write_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_write_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_write_filter_module.o \
		src/http/ngx_http_write_filter_module.c


nginx-1.14.0/src/http/ngx_http_header_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_header_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_header_filter_module.o \
		src/http/ngx_http_header_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_chunked_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_chunked_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_chunked_filter_module.o \
		src/http/modules/ngx_http_chunked_filter_module.c


nginx-1.14.0/src/http/v2/ngx_http_v2_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2_filter_module.o \
		src/http/v2/ngx_http_v2_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_range_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_range_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_range_filter_module.o \
		src/http/modules/ngx_http_range_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_gzip_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_gzip_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_gzip_filter_module.o \
		src/http/modules/ngx_http_gzip_filter_module.c


nginx-1.14.0/src/http/ngx_http_postpone_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_postpone_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_postpone_filter_module.o \
		src/http/ngx_http_postpone_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_ssi_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_ssi_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_ssi_filter_module.o \
		src/http/modules/ngx_http_ssi_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_charset_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_charset_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_charset_filter_module.o \
		src/http/modules/ngx_http_charset_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_sub_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_sub_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_sub_filter_module.o \
		src/http/modules/ngx_http_sub_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_addition_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_addition_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_addition_filter_module.o \
		src/http/modules/ngx_http_addition_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_gunzip_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_gunzip_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_gunzip_filter_module.o \
		src/http/modules/ngx_http_gunzip_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_userid_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_userid_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_userid_filter_module.o \
		src/http/modules/ngx_http_userid_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_headers_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_headers_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_headers_filter_module.o \
		src/http/modules/ngx_http_headers_filter_module.c


nginx-1.14.0/src/http/ngx_http_copy_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_copy_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/ngx_http_copy_filter_module.o \
		src/http/ngx_http_copy_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_not_modified_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_not_modified_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_not_modified_filter_module.o \
		src/http/modules/ngx_http_not_modified_filter_module.c


nginx-1.14.0/src/http/modules/ngx_http_slice_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_slice_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_slice_filter_module.o \
		src/http/modules/ngx_http_slice_filter_module.c


nginx-1.14.0/src/http/v2/ngx_http_v2.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2.o \
		src/http/v2/ngx_http_v2.c


nginx-1.14.0/src/http/v2/ngx_http_v2_table.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2_table.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2_table.o \
		src/http/v2/ngx_http_v2_table.c


nginx-1.14.0/src/http/v2/ngx_http_v2_encode.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2_encode.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2_encode.o \
		src/http/v2/ngx_http_v2_encode.c


nginx-1.14.0/src/http/v2/ngx_http_v2_huff_decode.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2_huff_decode.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2_huff_decode.o \
		src/http/v2/ngx_http_v2_huff_decode.c


nginx-1.14.0/src/http/v2/ngx_http_v2_huff_encode.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2_huff_encode.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2_huff_encode.o \
		src/http/v2/ngx_http_v2_huff_encode.c


nginx-1.14.0/src/http/v2/ngx_http_v2_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/v2/ngx_http_v2_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/v2/ngx_http_v2_module.o \
		src/http/v2/ngx_http_v2_module.c


nginx-1.14.0/src/http/modules/ngx_http_static_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_static_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_static_module.o \
		src/http/modules/ngx_http_static_module.c


nginx-1.14.0/src/http/modules/ngx_http_gzip_static_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_gzip_static_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_gzip_static_module.o \
		src/http/modules/ngx_http_gzip_static_module.c


nginx-1.14.0/src/http/modules/ngx_http_dav_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_dav_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_dav_module.o \
		src/http/modules/ngx_http_dav_module.c


nginx-1.14.0/src/http/modules/ngx_http_autoindex_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_autoindex_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_autoindex_module.o \
		src/http/modules/ngx_http_autoindex_module.c


nginx-1.14.0/src/http/modules/ngx_http_index_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_index_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_index_module.o \
		src/http/modules/ngx_http_index_module.c


nginx-1.14.0/src/http/modules/ngx_http_random_index_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_random_index_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_random_index_module.o \
		src/http/modules/ngx_http_random_index_module.c


nginx-1.14.0/src/http/modules/ngx_http_mirror_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_mirror_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_mirror_module.o \
		src/http/modules/ngx_http_mirror_module.c


nginx-1.14.0/src/http/modules/ngx_http_try_files_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_try_files_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_try_files_module.o \
		src/http/modules/ngx_http_try_files_module.c


nginx-1.14.0/src/http/modules/ngx_http_auth_request_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_auth_request_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_auth_request_module.o \
		src/http/modules/ngx_http_auth_request_module.c


nginx-1.14.0/src/http/modules/ngx_http_auth_basic_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_auth_basic_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_auth_basic_module.o \
		src/http/modules/ngx_http_auth_basic_module.c


nginx-1.14.0/src/http/modules/ngx_http_access_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_access_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_access_module.o \
		src/http/modules/ngx_http_access_module.c


nginx-1.14.0/src/http/modules/ngx_http_limit_conn_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_limit_conn_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_limit_conn_module.o \
		src/http/modules/ngx_http_limit_conn_module.c


nginx-1.14.0/src/http/modules/ngx_http_limit_req_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_limit_req_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_limit_req_module.o \
		src/http/modules/ngx_http_limit_req_module.c


nginx-1.14.0/src/http/modules/ngx_http_realip_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_realip_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_realip_module.o \
		src/http/modules/ngx_http_realip_module.c


nginx-1.14.0/src/http/modules/ngx_http_geo_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_geo_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_geo_module.o \
		src/http/modules/ngx_http_geo_module.c


nginx-1.14.0/src/http/modules/ngx_http_map_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_map_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_map_module.o \
		src/http/modules/ngx_http_map_module.c


nginx-1.14.0/src/http/modules/ngx_http_split_clients_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_split_clients_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_split_clients_module.o \
		src/http/modules/ngx_http_split_clients_module.c


nginx-1.14.0/src/http/modules/ngx_http_referer_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_referer_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_referer_module.o \
		src/http/modules/ngx_http_referer_module.c


nginx-1.14.0/src/http/modules/ngx_http_rewrite_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_rewrite_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_rewrite_module.o \
		src/http/modules/ngx_http_rewrite_module.c


nginx-1.14.0/src/http/modules/ngx_http_ssl_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_ssl_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_ssl_module.o \
		src/http/modules/ngx_http_ssl_module.c


nginx-1.14.0/src/http/modules/ngx_http_proxy_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_proxy_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_proxy_module.o \
		src/http/modules/ngx_http_proxy_module.c


nginx-1.14.0/src/http/modules/ngx_http_fastcgi_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_fastcgi_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_fastcgi_module.o \
		src/http/modules/ngx_http_fastcgi_module.c


nginx-1.14.0/src/http/modules/ngx_http_uwsgi_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_uwsgi_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_uwsgi_module.o \
		src/http/modules/ngx_http_uwsgi_module.c


nginx-1.14.0/src/http/modules/ngx_http_scgi_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_scgi_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_scgi_module.o \
		src/http/modules/ngx_http_scgi_module.c


nginx-1.14.0/src/http/modules/ngx_http_grpc_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_grpc_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_grpc_module.o \
		src/http/modules/ngx_http_grpc_module.c


nginx-1.14.0/src/http/modules/ngx_http_memcached_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_memcached_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_memcached_module.o \
		src/http/modules/ngx_http_memcached_module.c


nginx-1.14.0/src/http/modules/ngx_http_empty_gif_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_empty_gif_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_empty_gif_module.o \
		src/http/modules/ngx_http_empty_gif_module.c


nginx-1.14.0/src/http/modules/ngx_http_browser_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_browser_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_browser_module.o \
		src/http/modules/ngx_http_browser_module.c


nginx-1.14.0/src/http/modules/ngx_http_secure_link_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_secure_link_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_secure_link_module.o \
		src/http/modules/ngx_http_secure_link_module.c


nginx-1.14.0/src/http/modules/ngx_http_degradation_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_degradation_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_degradation_module.o \
		src/http/modules/ngx_http_degradation_module.c


nginx-1.14.0/src/http/modules/ngx_http_flv_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_flv_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_flv_module.o \
		src/http/modules/ngx_http_flv_module.c


nginx-1.14.0/src/http/modules/ngx_http_mp4_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_mp4_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_mp4_module.o \
		src/http/modules/ngx_http_mp4_module.c


nginx-1.14.0/src/http/modules/ngx_http_upstream_hash_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_hash_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_upstream_hash_module.o \
		src/http/modules/ngx_http_upstream_hash_module.c


nginx-1.14.0/src/http/modules/ngx_http_upstream_ip_hash_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_ip_hash_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_upstream_ip_hash_module.o \
		src/http/modules/ngx_http_upstream_ip_hash_module.c


nginx-1.14.0/src/http/modules/ngx_http_upstream_least_conn_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_least_conn_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_upstream_least_conn_module.o \
		src/http/modules/ngx_http_upstream_least_conn_module.c


nginx-1.14.0/src/http/modules/ngx_http_upstream_keepalive_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_keepalive_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_upstream_keepalive_module.o \
		src/http/modules/ngx_http_upstream_keepalive_module.c


nginx-1.14.0/src/http/modules/ngx_http_upstream_zone_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_zone_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_upstream_zone_module.o \
		src/http/modules/ngx_http_upstream_zone_module.c


nginx-1.14.0/src/http/modules/ngx_http_stub_status_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_stub_status_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_stub_status_module.o \
		src/http/modules/ngx_http_stub_status_module.c


nginx-1.14.0/addon/src/log_message_handler.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/log_message_handler.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/log_message_handler.o \
		/root/installer/publicnginx/ngx_pagespeed/src/log_message_handler.cc


nginx-1.14.0/addon/src/ngx_base_fetch.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_base_fetch.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_base_fetch.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_base_fetch.cc


nginx-1.14.0/addon/src/ngx_caching_headers.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_caching_headers.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_caching_headers.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_caching_headers.cc


nginx-1.14.0/addon/src/ngx_event_connection.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_event_connection.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_event_connection.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_event_connection.cc


nginx-1.14.0/addon/src/ngx_fetch.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_fetch.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_fetch.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_fetch.cc


nginx-1.14.0/addon/src/ngx_gzip_setter.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_gzip_setter.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_gzip_setter.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_gzip_setter.cc


nginx-1.14.0/addon/src/ngx_list_iterator.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_list_iterator.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_list_iterator.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_list_iterator.cc


nginx-1.14.0/addon/src/ngx_message_handler.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_message_handler.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_message_handler.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_message_handler.cc


nginx-1.14.0/addon/src/ngx_pagespeed.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_pagespeed.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_pagespeed.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_pagespeed.cc


nginx-1.14.0/addon/src/ngx_rewrite_driver_factory.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_rewrite_driver_factory.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_rewrite_driver_factory.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_rewrite_driver_factory.cc


nginx-1.14.0/addon/src/ngx_rewrite_options.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_rewrite_options.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_rewrite_options.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_rewrite_options.cc


nginx-1.14.0/addon/src/ngx_server_context.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_server_context.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_server_context.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_server_context.cc


nginx-1.14.0/addon/src/ngx_url_async_fetcher.o:	$(ADDON_DEPS) \
	/root/installer/publicnginx/ngx_pagespeed/src/ngx_url_async_fetcher.cc
	$(CC) -c $(CFLAGS)  $(ALL_INCS) \
		-o nginx-1.14.0/addon/src/ngx_url_async_fetcher.o \
		/root/installer/publicnginx/ngx_pagespeed/src/ngx_url_async_fetcher.cc

nginx-1.14.0/addon/src/log_message_handler.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_base_fetch.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_caching_headers.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_event_connection.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_fetch.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_gzip_setter.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_list_iterator.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_message_handler.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_pagespeed.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_rewrite_driver_factory.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_rewrite_options.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_server_context.o : CFLAGS += --std=c++11
nginx-1.14.0/addon/src/ngx_url_async_fetcher.o : CFLAGS += --std=c++11

modules:	nginx-1.14.0/ngx_http_image_filter_module.so

nginx-1.14.0/ngx_http_image_filter_module.so:	nginx-1.14.0/src/http/modules/ngx_http_image_filter_module.o \
	nginx-1.14.0/ngx_http_image_filter_module_modules.o \
	/root/installer/publicnginx/pcre-8.35/.libs/libpcre.a \
	/root/installer/publicnginx/zlib-1.2.11/libz.a

	$(LINK) -o nginx-1.14.0/ngx_http_image_filter_module.so \
	nginx-1.14.0/src/http/modules/ngx_http_image_filter_module.o \
	nginx-1.14.0/ngx_http_image_filter_module_modules.o \
	-lgd \
	-shared


nginx-1.14.0/ngx_http_image_filter_module_modules.o:	$(CORE_DEPS) \
	nginx-1.14.0/ngx_http_image_filter_module_modules.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/ngx_http_image_filter_module_modules.o \
		nginx-1.14.0/ngx_http_image_filter_module_modules.c


nginx-1.14.0/src/http/modules/ngx_http_image_filter_module.o:	$(ADDON_DEPS) \
	src/http/modules/ngx_http_image_filter_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_image_filter_module.o \
		src/http/modules/ngx_http_image_filter_module.c


modules:	nginx-1.14.0/ngx_http_geoip_module.so

nginx-1.14.0/ngx_http_geoip_module.so:	nginx-1.14.0/src/http/modules/ngx_http_geoip_module.o \
	nginx-1.14.0/ngx_http_geoip_module_modules.o \
	/root/installer/publicnginx/pcre-8.35/.libs/libpcre.a \
	/root/installer/publicnginx/zlib-1.2.11/libz.a

	$(LINK) -o nginx-1.14.0/ngx_http_geoip_module.so \
	nginx-1.14.0/src/http/modules/ngx_http_geoip_module.o \
	nginx-1.14.0/ngx_http_geoip_module_modules.o \
	-lGeoIP \
	-shared


nginx-1.14.0/ngx_http_geoip_module_modules.o:	$(CORE_DEPS) \
	nginx-1.14.0/ngx_http_geoip_module_modules.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/ngx_http_geoip_module_modules.o \
		nginx-1.14.0/ngx_http_geoip_module_modules.c


nginx-1.14.0/src/http/modules/ngx_http_geoip_module.o:	$(ADDON_DEPS) \
	src/http/modules/ngx_http_geoip_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/http/modules/ngx_http_geoip_module.o \
		src/http/modules/ngx_http_geoip_module.c


modules:	nginx-1.14.0/ngx_mail_module.so

nginx-1.14.0/ngx_mail_module.so:	nginx-1.14.0/src/mail/ngx_mail.o \
	nginx-1.14.0/src/mail/ngx_mail_core_module.o \
	nginx-1.14.0/src/mail/ngx_mail_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_parse.o \
	nginx-1.14.0/src/mail/ngx_mail_ssl_module.o \
	nginx-1.14.0/src/mail/ngx_mail_pop3_module.o \
	nginx-1.14.0/src/mail/ngx_mail_pop3_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_imap_module.o \
	nginx-1.14.0/src/mail/ngx_mail_imap_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_smtp_module.o \
	nginx-1.14.0/src/mail/ngx_mail_smtp_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_auth_http_module.o \
	nginx-1.14.0/src/mail/ngx_mail_proxy_module.o \
	nginx-1.14.0/ngx_mail_module_modules.o \
	/root/installer/publicnginx/pcre-8.35/.libs/libpcre.a \
	/root/installer/publicnginx/zlib-1.2.11/libz.a

	$(LINK) -o nginx-1.14.0/ngx_mail_module.so \
	nginx-1.14.0/src/mail/ngx_mail.o \
	nginx-1.14.0/src/mail/ngx_mail_core_module.o \
	nginx-1.14.0/src/mail/ngx_mail_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_parse.o \
	nginx-1.14.0/src/mail/ngx_mail_ssl_module.o \
	nginx-1.14.0/src/mail/ngx_mail_pop3_module.o \
	nginx-1.14.0/src/mail/ngx_mail_pop3_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_imap_module.o \
	nginx-1.14.0/src/mail/ngx_mail_imap_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_smtp_module.o \
	nginx-1.14.0/src/mail/ngx_mail_smtp_handler.o \
	nginx-1.14.0/src/mail/ngx_mail_auth_http_module.o \
	nginx-1.14.0/src/mail/ngx_mail_proxy_module.o \
	nginx-1.14.0/ngx_mail_module_modules.o \
	-shared


nginx-1.14.0/ngx_mail_module_modules.o:	$(CORE_DEPS) \
	nginx-1.14.0/ngx_mail_module_modules.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/ngx_mail_module_modules.o \
		nginx-1.14.0/ngx_mail_module_modules.c


nginx-1.14.0/src/mail/ngx_mail.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail.o \
		src/mail/ngx_mail.c


nginx-1.14.0/src/mail/ngx_mail_core_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_core_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_core_module.o \
		src/mail/ngx_mail_core_module.c


nginx-1.14.0/src/mail/ngx_mail_handler.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_handler.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_handler.o \
		src/mail/ngx_mail_handler.c


nginx-1.14.0/src/mail/ngx_mail_parse.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_parse.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_parse.o \
		src/mail/ngx_mail_parse.c


nginx-1.14.0/src/mail/ngx_mail_ssl_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_ssl_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_ssl_module.o \
		src/mail/ngx_mail_ssl_module.c


nginx-1.14.0/src/mail/ngx_mail_pop3_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_pop3_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_pop3_module.o \
		src/mail/ngx_mail_pop3_module.c


nginx-1.14.0/src/mail/ngx_mail_pop3_handler.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_pop3_handler.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_pop3_handler.o \
		src/mail/ngx_mail_pop3_handler.c


nginx-1.14.0/src/mail/ngx_mail_imap_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_imap_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_imap_module.o \
		src/mail/ngx_mail_imap_module.c


nginx-1.14.0/src/mail/ngx_mail_imap_handler.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_imap_handler.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_imap_handler.o \
		src/mail/ngx_mail_imap_handler.c


nginx-1.14.0/src/mail/ngx_mail_smtp_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_smtp_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_smtp_module.o \
		src/mail/ngx_mail_smtp_module.c


nginx-1.14.0/src/mail/ngx_mail_smtp_handler.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_smtp_handler.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_smtp_handler.o \
		src/mail/ngx_mail_smtp_handler.c


nginx-1.14.0/src/mail/ngx_mail_auth_http_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_auth_http_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_auth_http_module.o \
		src/mail/ngx_mail_auth_http_module.c


nginx-1.14.0/src/mail/ngx_mail_proxy_module.o:	$(ADDON_DEPS) \
	src/mail/ngx_mail_proxy_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/mail/ngx_mail_proxy_module.o \
		src/mail/ngx_mail_proxy_module.c


modules:	nginx-1.14.0/ngx_stream_module.so

nginx-1.14.0/ngx_stream_module.so:	nginx-1.14.0/src/stream/ngx_stream.o \
	nginx-1.14.0/src/stream/ngx_stream_variables.o \
	nginx-1.14.0/src/stream/ngx_stream_script.o \
	nginx-1.14.0/src/stream/ngx_stream_handler.o \
	nginx-1.14.0/src/stream/ngx_stream_core_module.o \
	nginx-1.14.0/src/stream/ngx_stream_log_module.o \
	nginx-1.14.0/src/stream/ngx_stream_proxy_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_round_robin.o \
	nginx-1.14.0/src/stream/ngx_stream_write_filter_module.o \
	nginx-1.14.0/src/stream/ngx_stream_ssl_module.o \
	nginx-1.14.0/src/stream/ngx_stream_realip_module.o \
	nginx-1.14.0/src/stream/ngx_stream_limit_conn_module.o \
	nginx-1.14.0/src/stream/ngx_stream_access_module.o \
	nginx-1.14.0/src/stream/ngx_stream_geo_module.o \
	nginx-1.14.0/src/stream/ngx_stream_map_module.o \
	nginx-1.14.0/src/stream/ngx_stream_split_clients_module.o \
	nginx-1.14.0/src/stream/ngx_stream_return_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_hash_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_least_conn_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_zone_module.o \
	nginx-1.14.0/ngx_stream_module_modules.o \
	/root/installer/publicnginx/pcre-8.35/.libs/libpcre.a \
	/root/installer/publicnginx/zlib-1.2.11/libz.a

	$(LINK) -o nginx-1.14.0/ngx_stream_module.so \
	nginx-1.14.0/src/stream/ngx_stream.o \
	nginx-1.14.0/src/stream/ngx_stream_variables.o \
	nginx-1.14.0/src/stream/ngx_stream_script.o \
	nginx-1.14.0/src/stream/ngx_stream_handler.o \
	nginx-1.14.0/src/stream/ngx_stream_core_module.o \
	nginx-1.14.0/src/stream/ngx_stream_log_module.o \
	nginx-1.14.0/src/stream/ngx_stream_proxy_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_round_robin.o \
	nginx-1.14.0/src/stream/ngx_stream_write_filter_module.o \
	nginx-1.14.0/src/stream/ngx_stream_ssl_module.o \
	nginx-1.14.0/src/stream/ngx_stream_realip_module.o \
	nginx-1.14.0/src/stream/ngx_stream_limit_conn_module.o \
	nginx-1.14.0/src/stream/ngx_stream_access_module.o \
	nginx-1.14.0/src/stream/ngx_stream_geo_module.o \
	nginx-1.14.0/src/stream/ngx_stream_map_module.o \
	nginx-1.14.0/src/stream/ngx_stream_split_clients_module.o \
	nginx-1.14.0/src/stream/ngx_stream_return_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_hash_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_least_conn_module.o \
	nginx-1.14.0/src/stream/ngx_stream_upstream_zone_module.o \
	nginx-1.14.0/ngx_stream_module_modules.o \
	-shared


nginx-1.14.0/ngx_stream_module_modules.o:	$(CORE_DEPS) \
	nginx-1.14.0/ngx_stream_module_modules.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/ngx_stream_module_modules.o \
		nginx-1.14.0/ngx_stream_module_modules.c


nginx-1.14.0/src/stream/ngx_stream.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream.o \
		src/stream/ngx_stream.c


nginx-1.14.0/src/stream/ngx_stream_variables.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_variables.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_variables.o \
		src/stream/ngx_stream_variables.c


nginx-1.14.0/src/stream/ngx_stream_script.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_script.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_script.o \
		src/stream/ngx_stream_script.c


nginx-1.14.0/src/stream/ngx_stream_handler.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_handler.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_handler.o \
		src/stream/ngx_stream_handler.c


nginx-1.14.0/src/stream/ngx_stream_core_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_core_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_core_module.o \
		src/stream/ngx_stream_core_module.c


nginx-1.14.0/src/stream/ngx_stream_log_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_log_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_log_module.o \
		src/stream/ngx_stream_log_module.c


nginx-1.14.0/src/stream/ngx_stream_proxy_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_proxy_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_proxy_module.o \
		src/stream/ngx_stream_proxy_module.c


nginx-1.14.0/src/stream/ngx_stream_upstream.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_upstream.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_upstream.o \
		src/stream/ngx_stream_upstream.c


nginx-1.14.0/src/stream/ngx_stream_upstream_round_robin.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_upstream_round_robin.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_upstream_round_robin.o \
		src/stream/ngx_stream_upstream_round_robin.c


nginx-1.14.0/src/stream/ngx_stream_write_filter_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_write_filter_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_write_filter_module.o \
		src/stream/ngx_stream_write_filter_module.c


nginx-1.14.0/src/stream/ngx_stream_ssl_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_ssl_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_ssl_module.o \
		src/stream/ngx_stream_ssl_module.c


nginx-1.14.0/src/stream/ngx_stream_realip_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_realip_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_realip_module.o \
		src/stream/ngx_stream_realip_module.c


nginx-1.14.0/src/stream/ngx_stream_limit_conn_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_limit_conn_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_limit_conn_module.o \
		src/stream/ngx_stream_limit_conn_module.c


nginx-1.14.0/src/stream/ngx_stream_access_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_access_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_access_module.o \
		src/stream/ngx_stream_access_module.c


nginx-1.14.0/src/stream/ngx_stream_geo_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_geo_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_geo_module.o \
		src/stream/ngx_stream_geo_module.c


nginx-1.14.0/src/stream/ngx_stream_map_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_map_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_map_module.o \
		src/stream/ngx_stream_map_module.c


nginx-1.14.0/src/stream/ngx_stream_split_clients_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_split_clients_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_split_clients_module.o \
		src/stream/ngx_stream_split_clients_module.c


nginx-1.14.0/src/stream/ngx_stream_return_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_return_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_return_module.o \
		src/stream/ngx_stream_return_module.c


nginx-1.14.0/src/stream/ngx_stream_upstream_hash_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_upstream_hash_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_upstream_hash_module.o \
		src/stream/ngx_stream_upstream_hash_module.c


nginx-1.14.0/src/stream/ngx_stream_upstream_least_conn_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_upstream_least_conn_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_upstream_least_conn_module.o \
		src/stream/ngx_stream_upstream_least_conn_module.c


nginx-1.14.0/src/stream/ngx_stream_upstream_zone_module.o:	$(ADDON_DEPS) \
	src/stream/ngx_stream_upstream_zone_module.c
	$(CC) -c -fPIC $(CFLAGS) $(ALL_INCS) \
		-o nginx-1.14.0/src/stream/ngx_stream_upstream_zone_module.o \
		src/stream/ngx_stream_upstream_zone_module.c


/root/installer/publicnginx/pcre-8.35/pcre.h:	/root/installer/publicnginx/pcre-8.35/Makefile

/root/installer/publicnginx/pcre-8.35/Makefile:	nginx-1.14.0/Makefile
	cd /root/installer/publicnginx/pcre-8.35 \
	&& if [ -f Makefile ]; then $(MAKE) distclean; fi \
	&& CC="$(CC)" CFLAGS="-O2 -fomit-frame-pointer -pipe " \
	./configure --disable-shared  --enable-jit

/root/installer/publicnginx/pcre-8.35/.libs/libpcre.a:	/root/installer/publicnginx/pcre-8.35/Makefile
	cd /root/installer/publicnginx/pcre-8.35 \
	&& $(MAKE) libpcre.la


/root/installer/publicnginx/openssl-1.1.0h/.openssl/include/openssl/ssl.h:	nginx-1.14.0/Makefile
	cd /root/installer/publicnginx/openssl-1.1.0h \
	&& if [ -f Makefile ]; then $(MAKE) clean; fi \
	&& ./config --prefix=/root/installer/publicnginx/openssl-1.1.0h/.openssl no-shared no-threads  \
	&& $(MAKE) \
	&& $(MAKE) install_sw LIBDIR=lib


/root/installer/publicnginx/zlib-1.2.11/libz.a:	nginx-1.14.0/Makefile
	cd /root/installer/publicnginx/zlib-1.2.11 \
	&& $(MAKE) distclean \
	&& CFLAGS="-O2 -fomit-frame-pointer -pipe " CC="$(CC)" \
		./configure \
	&& $(MAKE) libz.a


manpage:	nginx-1.14.0/nginx.8

nginx-1.14.0/nginx.8:	man/nginx.8 nginx-1.14.0/ngx_auto_config.h
	sed -e "s|%%PREFIX%%|/etc/nginx|" \
		-e "s|%%PID_PATH%%|/var/run/nginx.pid|" \
		-e "s|%%CONF_PATH%%|/etc/nginx/nginx.conf|" \
		-e "s|%%ERROR_LOG_PATH%%|/var/log/nginx/error.log|" \
		< man/nginx.8 > $@

install:	build 
	test -d '$(DESTDIR)/etc/nginx' || mkdir -p '$(DESTDIR)/etc/nginx'

	test -d '$(DESTDIR)/usr/local' \
		|| mkdir -p '$(DESTDIR)/usr/local'
	test ! -f '$(DESTDIR)/usr/local/sbin' \
		|| mv '$(DESTDIR)/usr/local/sbin' \
			'$(DESTDIR)/usr/local/sbin.old'
	cp nginx-1.14.0/nginx '$(DESTDIR)/usr/local/sbin'

	test -d '$(DESTDIR)/etc/nginx' \
		|| mkdir -p '$(DESTDIR)/etc/nginx'

	cp conf/koi-win '$(DESTDIR)/etc/nginx'
	cp conf/koi-utf '$(DESTDIR)/etc/nginx'
	cp conf/win-utf '$(DESTDIR)/etc/nginx'

	test -f '$(DESTDIR)/etc/nginx/mime.types' \
		|| cp conf/mime.types '$(DESTDIR)/etc/nginx'
	cp conf/mime.types '$(DESTDIR)/etc/nginx/mime.types.default'

	test -f '$(DESTDIR)/etc/nginx/fastcgi_params' \
		|| cp conf/fastcgi_params '$(DESTDIR)/etc/nginx'
	cp conf/fastcgi_params \
		'$(DESTDIR)/etc/nginx/fastcgi_params.default'

	test -f '$(DESTDIR)/etc/nginx/fastcgi.conf' \
		|| cp conf/fastcgi.conf '$(DESTDIR)/etc/nginx'
	cp conf/fastcgi.conf '$(DESTDIR)/etc/nginx/fastcgi.conf.default'

	test -f '$(DESTDIR)/etc/nginx/uwsgi_params' \
		|| cp conf/uwsgi_params '$(DESTDIR)/etc/nginx'
	cp conf/uwsgi_params \
		'$(DESTDIR)/etc/nginx/uwsgi_params.default'

	test -f '$(DESTDIR)/etc/nginx/scgi_params' \
		|| cp conf/scgi_params '$(DESTDIR)/etc/nginx'
	cp conf/scgi_params \
		'$(DESTDIR)/etc/nginx/scgi_params.default'

	test -f '$(DESTDIR)/etc/nginx/nginx.conf' \
		|| cp conf/nginx.conf '$(DESTDIR)/etc/nginx/nginx.conf'
	cp conf/nginx.conf '$(DESTDIR)/etc/nginx/nginx.conf.default'

	test -d '$(DESTDIR)/var/run' \
		|| mkdir -p '$(DESTDIR)/var/run'

	test -d '$(DESTDIR)/var/log/nginx' \
		|| mkdir -p '$(DESTDIR)/var/log/nginx'

	test -d '$(DESTDIR)/etc/nginx/html' \
		|| cp -R html '$(DESTDIR)/etc/nginx'

	test -d '$(DESTDIR)/var/log/nginx' \
		|| mkdir -p '$(DESTDIR)/var/log/nginx'

	test -d '$(DESTDIR)/etc/nginx/modules' \
		|| mkdir -p '$(DESTDIR)/etc/nginx/modules'

	test ! -f '$(DESTDIR)/etc/nginx/modules/ngx_http_image_filter_module.so' \
		|| mv '$(DESTDIR)/etc/nginx/modules/ngx_http_image_filter_module.so' \
			'$(DESTDIR)/etc/nginx/modules/ngx_http_image_filter_module.so.old'
	cp nginx-1.14.0/ngx_http_image_filter_module.so '$(DESTDIR)/etc/nginx/modules/ngx_http_image_filter_module.so'

	test ! -f '$(DESTDIR)/etc/nginx/modules/ngx_http_geoip_module.so' \
		|| mv '$(DESTDIR)/etc/nginx/modules/ngx_http_geoip_module.so' \
			'$(DESTDIR)/etc/nginx/modules/ngx_http_geoip_module.so.old'
	cp nginx-1.14.0/ngx_http_geoip_module.so '$(DESTDIR)/etc/nginx/modules/ngx_http_geoip_module.so'

	test ! -f '$(DESTDIR)/etc/nginx/modules/ngx_mail_module.so' \
		|| mv '$(DESTDIR)/etc/nginx/modules/ngx_mail_module.so' \
			'$(DESTDIR)/etc/nginx/modules/ngx_mail_module.so.old'
	cp nginx-1.14.0/ngx_mail_module.so '$(DESTDIR)/etc/nginx/modules/ngx_mail_module.so'

	test ! -f '$(DESTDIR)/etc/nginx/modules/ngx_stream_module.so' \
		|| mv '$(DESTDIR)/etc/nginx/modules/ngx_stream_module.so' \
			'$(DESTDIR)/etc/nginx/modules/ngx_stream_module.so.old'
	cp nginx-1.14.0/ngx_stream_module.so '$(DESTDIR)/etc/nginx/modules/ngx_stream_module.so'
