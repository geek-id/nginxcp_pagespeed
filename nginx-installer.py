#!/usr/bin/env python
# Nginx Admin Installer
# website: www.nginxcp.COM
#
# Copyright (c) NGINXCP.COM.
#
# Modified by : GeekID | GeekHost
#

import subprocess
import os
import sys
import time
import re
import getpass
import threading
import time

sys.path.append('/scripts/')
currentdir = os.getcwd()

# print currentdir
def findhttpdversion():
    proc = subprocess.Popen(["/sbin/httpd", "-V"], stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    m = re.search("Apache/(2\.[0-9]+\.[0-9]+)", output)
    if not m:
        print "Unsupported HTTPD Version"
        sys.exit(1)
    return m.group(1)

httpd_version = findhttpdversion()

# print httpd_version

if os.path.exists('/root/.accesshash'):
    pass
else:
    proc = subprocess.Popen("/scripts/convert_accesshash_to_token > /dev/null 2>&1", shell=True)
    output = proc.communicate()
    # print "Please, generate Access Key! Access Key doesn't exist"
    # print "Go to SSH > run command `/scripts/convert_accesshash_to_token`"
    sys.exit(1)

cpanel_version = open("/usr/local/cpanel/version", "r")
cpanel_version_string = cpanel_version.read(5)
cpanel_version.close

# print cpanel_version
if cpanel_version_string >= "11.28":
    pass
else:
    print "Upgrade your cPanel version to higher version"
    sys.exit()

srcpath=currentdir
# print srcpath
nginx_path = currentdir + "/nginx-1.14.0"
pagespeed_path = currentdir + "/ngx_pagespeed"
zlib_path = currentdir + "/zlib-1.2.11"
openssl_path = currentdir + "/openssl-1.1.0h"
pcre_path = currentdir + "/pcre-8.35"
setuptools_path = currentdir + "/setuptools-5.7"

# print nginx_path
# print pagespeed_path
# print zlib_path
# print openssl_path

proc = subprocess.Popen("yum groupinstall \"Development Tools\" -y", shell=True)
output = proc.communicate()
proc = subprocess.Popen("yum install -y gcc gd-devel GeoIP-devel", shell=True)
output = proc.communicate()

nginx_compile = """./configure --prefix=/etc/nginx --with-http_flv_module --with-http_mp4_module --with-pcre=%s --with-openssl=%s --with-zlib=%s --add-module=%s --sbin-path=/usr/local/sbin  --conf-path=/etc/nginx/nginx.conf --pid-path=/var/run/nginx.pid  --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-file-aio --with-threads --with-poll_module --lock-path=/var/run/nginx.lock --build=CloudLinux --builddir=nginx-1.14.0 --with-select_module --with-http_addition_module --with-http_image_filter_module=dynamic --with-http_dav_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_auth_request_module --with-http_random_index_module --with-http_secure_link_module --with-http_geoip_module=dynamic --with-http_sub_module --with-http_realip_module --with-http_v2_module --with-http_ssl_module  --http-client-body-temp-path=/tmp/nginx_client --http-proxy-temp-path=/tmp/nginx_proxy --with-http_degradation_module --with-http_slice_module --http-fastcgi-temp-path=/tmp/nginx_fastcgi  --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --with-mail=dynamic --with-mail_ssl_module --with-stream=dynamic --with-stream_ssl_module --with-stream_realip_module --with-pcre-jit --with-compat --user=nobody --group=nobody --with-http_stub_status_module""" % (pcre_path, openssl_path, zlib_path, pagespeed_path)

user = getpass.getuser()
# print user
print "Hello, %s "% (user)
print "Welcome to the Nginx Admin Installer...Starting Install"
# print "Wait a moment .................."

def animated_loading():
    chars = "/-\|"
    for char in chars:
        sys.stdout.write('\r'+'Wait a moment... '+char)
        time.sleep(.1)
        sys.stdout.flush()

def process_function():
    proc = ''
    for processing in proc:
        time.sleep(1)
        sys.stdout.write('\n\r'+'Wait... processing')
        sys.stdout.flush()
    sys.stdout.write('\n\r'+'Processing... finished      \n')

the_process = threading.Thread(name='process', target=process_function)

proc = subprocess.Popen("mkdir -p /usr/local/cpanel/hooks/addondomain > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/addaddondomain /usr/local/cpanel/hooks/addondomain > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /usr/local/cpanel/hooks/addondomain/addaddondomain > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/deladdondomain /usr/local/cpanel/hooks/addondomain > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /usr/local/cpanel/hooks/addondomain/deladdondomain > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/park /usr/local/cpanel/hooks/park > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /usr/local/cpanel/hooks/park/park > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/unpark /usr/local/cpanel/hooks/park > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /usr/local/cpanel/hooks/park/unpark > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/delsubdomain /usr/local/cpanel/hooks/subdomain > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /usr/local/cpanel/hooks/subdomain/delsubdomain > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/addsubdomain /usr/local/cpanel/hooks/subdomain > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /usr/local/cpanel/hooks/subdomain/addsubdomain > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("/usr/local/cpanel/bin/register_hooks > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/iplist.py /scripts/iplist.py > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/iplist.py > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/createvhosts.py /scripts/createvhosts.py > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/createvhosts.py > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/createvhostsssl.py /scripts/createvhostsssl.py > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/createvhostsssl.py > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/rebuildvhosts /scripts/rebuildvhosts > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/rebuildvhosts > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/xmlapi.py /scripts/xmlapi.py > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/xmlapi.py", shell=True)
output = proc.communicate()

if not httpd_version.startswith("2.4."):
    proc = subprocess.Popen("tar zxvf mod_rpaf-0.6.tar.gz", shell=True, cwd=srcpath)
    output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/installmodrpaf /scripts/ > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/installmodrpaf > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/installmodremoteip /scripts/ > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/installmodremoteip > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/after_apache_make_install /scripts/ > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/after_apache_make_install > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/nginx_restart /scripts/ > /dev/null 2>&1", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/nginx_restart > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("sed -i 's/=80/=8080/g' /etc/chkserv.d/httpd", shell=True)
output = proc.communicate()

sedcurrentdir=currentdir.replace('/','\/')

proc = subprocess.Popen("sed -i '4i srcpath=" + sedcurrentdir + "' /scripts/after_apache_make_install > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("sed -i '1i nginx:1' /etc/chkserv.d/chkservd.conf > /dev/null 2>&1", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/nginx /etc/init.d/nginx ", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /etc/init.d/nginx", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/postwwwacct /scripts/postwwwacct", shell=True)
output = proc.communicate()
proc = subprocess.Popen("chmod +x /scripts/postwwwacct", shell=True)
output = proc.communicate()

proc = subprocess.Popen("tar -zxf pcre-8.35.tar.gz > /dev/null 2>&1", shell=True, cwd=srcpath, stdout=None)
output = proc.communicate()
proc = subprocess.Popen("tar -zxf nginx-1.14.0.tar.gz > /dev/null 2>&1", shell=True, cwd=srcpath, stdout=None)
output = proc.communicate()
proc = subprocess.Popen("chkconfig --add nginx", shell=True)
output = proc.communicate()

proc = subprocess.Popen(nginx_compile, shell=True, cwd=nginx_path)
output = proc.communicate()
proc = subprocess.Popen("make", shell=True, cwd=nginx_path, stdout=None)
output = proc.communicate()
proc = subprocess.Popen("make install", shell=True, cwd=nginx_path, stdout=None)
output = proc.communicate()

# proc = subprocess.Popen("rm -f /etc/nginx/nginx.conf > /dev/null 2>&1", shell=True)
# output = proc.communicate()
proc = subprocess.Popen("cp " + currentdir + "/nginx.conf /etc/nginx/nginx.conf", shell=True)
output = proc.communicate()

# proc = subprocess.Popen("rm -f /etc/nginx/proxy.inc > /dev/null 2>&1", shell=True)
# output = proc.communicate()
proc = subprocess.Popen("cp " + currentdir + "/proxy.inc /etc/nginx/proxy.inc", shell=True)
output = proc.communicate()

# proc = subprocess.Popen("rm -f /etc/nginx/microcache.inc > /dev/null 2>&1", shell=True)
# output = proc.communicate()
proc = subprocess.Popen("cp " + currentdir + "/microcache.inc /etc/nginx/microcache.inc", shell=True)
output = proc.communicate()

proc = subprocess.Popen("tar -zxf setuptools-5.7.tar.gz", shell=True, cwd=srcpath, stdout=None)
output = proc.communicate()
proc = subprocess.Popen("python setup.py build > /dev/null 2>&1", shell=True, cwd=setuptools_path, stdout=None)
output = proc.communicate()
proc = subprocess.Popen("easy_install PyYAML > /dev/null 2>&1", shell=True)
output = proc.communicate()

# time.sleep(5)

print "Generating vhosts..."
proc = subprocess.Popen("/scripts/createvhosts.py", shell=True, stdout=None)
output = proc.communicate()

print "Generating ssl vhosts..."
proc = subprocess.Popen("/scripts/createvhostsssl.py", shell=True, stdout=None)
output = proc.communicate()

print "Installing WHM interface..."
proc = subprocess.Popen("cp " + currentdir + "/nginxcp.conf /var/cpanel/apps/nginxcp.conf", shell=True)
output = proc.communicate()

proc = subprocess.Popen("cp " + currentdir + "/cpnginx/* /usr/local/cpanel/whostmgr/docroot/cgi", shell=True)
output = proc.communicate()

proc = subprocess.Popen("sed -i 's/=use whmlib/=#use whmlib/g' /usr/local/cpanel/whostmgr/docroot/cgi/addon_nginx.cgi", shell=True)
output = proc.communicate()

if httpd_version.startswith("2.4.") and os.path.exists("/var/cpanel/templates/apache2_4"):
    print "Installing mod_remoteip..."
    remoteip_path = "/home/cpeasyapache/src/httpd-2.4/modules/metadata"
    if not os.path.exists(remoteip_path):
        print "RemoteIP module not found at : "+remoteip_path
        sys.exit(1)
    proc = subprocess.Popen("/usr/local/apache/bin/apxs -i -c -n mod_remoteip.so mod_remoteip.c > /dev/null 2>&1", shell=True, cwd=remoteip_path)
    output = proc.communicate()
else:
    print "Installing mod_rpaf..."
    proc = subprocess.Popen("/usr/local/apache/bin/apxs -i -c -n mod_rpaf-2.0.so mod_rpaf-2.0.c > /dev/null 2>&1", shell=True, cwd=srcpath+"/mod_rpaf-0.6")
    output = proc.communicate()

print "Updating cPanel Configuration..."
proc = subprocess.Popen(currentdir+'/nginxinstaller2'+ sys.argv[1], shell=True, cwd=currentdir)
output = proc.communicate()

the_process.start()

while the_process.isAlive():
    animated_loading()
