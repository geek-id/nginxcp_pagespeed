#!/usr/bin/env python
# Nginx Admin Installer
# Website: www.nginxcp.com
#
# Copyright (C) NGINXCP.COM.
#
import yaml
import os
from xml.dom import minidom
import sys
sys.path.append('/scripts/')
import xmlapi
import re

def wildcard_safe(domain):
        return domain.replace('*', '_wildcard_')

def writeconfded(user, domain, docroot, passedip, alias):
        f = open("/var/cpanel/ssl/apache_tls/"+domain+"/combined")
        path_ssl = '/etc/nginx/ssl/'

        # find line of Private key
        key_start = re.compile("-----BEGIN RSA PRIVATE KEY-----")
        key_end = re.compile("-----END RSA PRIVATE KEY-----")

        # # find line Certificate
        crt_start = re.compile("^-----BEGIN CERTIFICATE-----.*")
        crt_end = re.compile("-----END CERTIFICATE-----")

        # find line match with Private Key
        def re_range_key(f, key_start, key_end) :
            for line in f:
                if key_start.match(line):
                    yield line
                    break
            for line in f:
                yield line
                if key_end.match(line):
                    break

        # find line match with Certificate
        def re_range_crt(f, crt_start, crt_end):
            for line in f:
                if crt_start.match(line):
                    yield line
                    break
            for line in f:
                yield line
                if crt_end.match(line):
                    if crt_start.match(line):
                        yield line
                        break
        # read Private key line to create new file private key file
        key_line = ''
        for keyline in re_range_key(f, key_start, key_end):
            key_line += keyline

        if not os.path.exists (path_ssl):
            os.makedirs(path_ssl)
        if os.path.exists (path_ssl+ domain + '.key'):
            pass
        else:
            ssl_key = open(path_ssl+ domain +'.key', 'w')
            ssl_key.write(key_line)
            ssl_key.close

        # read certifcate line to create new file certificate file
        crt_line = ''
        for crtline in re_range_crt(f, crt_start, crt_end):
            crt_line += crtline

        if not os.path.exists (path_ssl):
            os.makedirs(path_ssl)
        if os.path.exists (path_ssl+ domain +'.crt'):
            pass
        else:
            ssl_crt = open(path_ssl+ domain +'.crt', 'w')
            ssl_crt.write(crt_line)
            ssl_crt.close

	user = user
        domain = domain
        passedip = passedip
        dedipvhost = """server {
          error_log /var/log/nginx/vhost-error_log warn;
          listen %s:443 ssl;
          listen [::]:443 ssl;
	  server_name %s %s %s;
          access_log /usr/local/apache/domlogs/%s bytes_log;
          access_log /usr/local/apache/domlogs/%s combined;
          root %s;

          ssl on;
          ssl_certificate /etc/nginx/ssl/%s.crt;
          ssl_certificate_key /etc/nginx/ssl/%s.key;

          pagespeed on;
          pagespeed FileCachePath /var/ngx_pagespeed_cache;
          pagespeed RewriteLevel CoreFilters;
          pagespeed EnableFilters collapse_whitespace,remove_comments,extend_cache,combine_css,combine_javascript;
          location ~ "\.pagespeed\.([a-z]\.)?[a-z]{2}\.[^.]{10}\.[^.]+" {
      add_header "" "";
      }
          location ~ "^/ngx_pagespeed_static/" { }
          location ~ "^/ngx_pagespeed_beacon$" { }
          pagespeed Statistics on;
          pagespeed StatisticsLogging on;
          pagespeed LogDir /var/log/pagespeed;

          #location / {
          location ~*.*\.(3gp|gif|jpg|jpeg|png|ico|wmv|avi|asf|asx|mpg|mpeg|mp4|pls|mp3|mid|wav|swf|flv|html|htm|txt|js|css|exe|zip|tar|rar|gz|tgz|bz2|uha|7z|doc|docx|xls|xlsx|pdf|iso)$ {
          expires 1M;
          try_files $uri @backend;
          }

          location / {
	  error_page 405 = @backend;
          add_header X-Cache "HIT from Backend";
          proxy_pass https://%s:8443;
          include proxy.inc;
	  include microcache.inc;
	  }

          location @backend {
          internal;
          proxy_pass https://%s:8443;
          include proxy.inc;
	  include microcache.inc;
          }

          location ~ .*\.(php|jsp|cgi|pl|py)?$ {
          proxy_pass https://%s:8443;
          include proxy.inc;
          include microcache.inc;
	  }

          location ~ /\.ht {
          deny all;
          }
        }""" % (passedip, domain, alias, passedip, wildcard_safe(domain) + "-bytes_log", wildcard_safe(domain), docroot, domain, domain, passedip, passedip, passedip)
        if not os.path.exists( '/etc/nginx/vhosts'):
                os.makedirs('/etc/nginx/vhosts')
        if os.path.exists( '/etc/nginx/staticvhosts/' + domain + '.ssl'):
                pass
        else:
                domainvhost = open ('/etc/nginx/vhosts/' + domain + '.ssl', 'w')
                domainvhost.writelines( dedipvhost )
                domainvhost.close()

def writeconfshared(user,domain,docroot,passedip, alias):
        f = open("/var/cpanel/ssl/apache_tls/"+domain+"/combined")
        path_ssl = '/etc/nginx/ssl/'

        # find line of Private key
        key_start = re.compile("-----BEGIN RSA PRIVATE KEY-----")
        key_end = re.compile("-----END RSA PRIVATE KEY-----")

        # # find line Certificate
        crt_start = re.compile("^-----BEGIN CERTIFICATE-----.*")
        crt_end = re.compile("-----END CERTIFICATE-----")

        # find line match with Private Key
        def re_range_key(f, key_start, key_end) :
            for line in f:
                if key_start.match(line):
                    yield line
                    break
            for line in f:
                yield line
                if key_end.match(line):
                    break

        # find line match with Certificate
        def re_range_crt(f, crt_start, crt_end):
            for line in f:
                if crt_start.match(line):
                    yield line
                    break
            for line in f:
                yield line
                if crt_end.match(line):
                    if crt_start.match(line):
                        yield line
                        break
        # read Private key line to create new file private key file
        key_line = ''
        for keyline in re_range_key(f, key_start, key_end):
            key_line += keyline

        if not os.path.exists (path_ssl):
            os.makedirs(path_ssl)
        if os.path.exists (path_ssl+ domain + '.key'):
            pass
        else:
            ssl_key = open(path_ssl+domain+'.key', 'w')
            ssl_key.write(key_line)
            ssl_key.close

        # read certifcate line to create new file certificate file
        crt_line = ''
        for crtline in re_range_crt(f, crt_start, crt_end):
            crt_line += crtline

        if not os.path.exists (path_ssl):
            os.makedirs(path_ssl)
        if os.path.exists (path_ssl+domain+'.crt'):
            pass
        else:
            ssl_crt = open(path_ssl+domain+'.crt', 'w')
            ssl_crt.write(crt_line)
            ssl_crt.close

        sharedipvhost = """server {
          error_log /var/log/nginx/vhost-error_log warn;
          listen %s:443 ssl;
	  server_name %s %s;
          access_log /usr/local/apache/domlogs/%s bytes_log;
          access_log /usr/local/apache/domlogs/%s combined;
          root %s;

          ssl on;
          ssl_certificate /etc/nginx/ssl/%s.crt;
          ssl_certificate_key /etc/nginx/ssl/%s.key;
          ssl_dhparam /etc/ssl/dhparam.pem;
          ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
          ssl_session_cache shared:SSL:10m;
          ssl_prefer_server_ciphers on;
          ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK';


          pagespeed on;
          pagespeed FileCachePath /var/ngx_pagespeed_cache;
          pagespeed RewriteLevel CoreFilters;
          pagespeed EnableFilters collapse_whitespace,remove_comments,extend_cache,combine_css,combine_javascript;
          location ~ "\.pagespeed\.([a-z]\.)?[a-z]{2}\.[^.]{10}\.[^.]+" {
      add_header "" "";
      }
          location ~ "^/ngx_pagespeed_static/" { }
          location ~ "^/ngx_pagespeed_beacon$" { }
          pagespeed Statistics on;
          pagespeed StatisticsLogging on;
          pagespeed LogDir /var/log/pagespeed;

          #location / {
          location ~*.*\.(3gp|gif|jpg|jpeg|png|ico|wmv|avi|asf|asx|mpg|mpeg|mp4|pls|mp3|mid|wav|swf|flv|html|htm|txt|js|css|exe|zip|tar|rar|gz|tgz|bz2|uha|7z|doc|docx|xls|xlsx|pdf|iso)$ {
          expires 1M;
          try_files $uri @backend;
          }

          location / {
	  error_page 405 = @backend;
          add_header X-Cache "HIT from Backend";
          proxy_pass https://%s:8443;
          include proxy.inc;
	  include microcache.inc;
          }

          location @backend {
          internal;
          proxy_pass https://%s:8443;
          include proxy.inc;
	  include microcache.inc;
          }

          location ~ .*\.(php|jsp|cgi|pl|py)?$ {
          proxy_pass https://%s:8443;
          include proxy.inc;
	  include microcache.inc;
          }

          location ~ /\.ht {
          deny all;
          }
        }""" % (passedip, domain, alias, wildcard_safe(domain) + "-bytes_log", wildcard_safe(domain), docroot, domain, domain, passedip, passedip, passedip)
        if not os.path.exists( '/etc/nginx/vhosts'):
                os.makedirs('/etc/nginx/vhosts')
        if os.path.exists( '/etc/nginx/staticvhosts/' + domain + '.ssl'):
                pass
        else:
                domainvhost = open ('/etc/nginx/vhosts/' + domain + '.ssl', 'w')
                domainvhost.writelines( sharedipvhost )
                domainvhost.close()

#def redirectfunc():



def getmainip():
        ipDOC = xmlapi.api("listips")
        parsedipDOC = minidom.parseString(ipDOC)
        iptaglist = parsedipDOC.getElementsByTagName('ip')
        serverip = iptaglist[0].childNodes[0].toxml()
        return serverip

def getipliststring():
        ipDOC = xmlapi.api("listips")
        parsedipDOC = minidom.parseString(ipDOC)
        iptaglist = parsedipDOC.getElementsByTagName('ip')
        iplist =[]

        q = 0
        while q < len(iptaglist):
                iplist.append(str(iptaglist[q].childNodes[0].toxml()))
                q = q + 1
        ipliststring = ' '.join(iplist)

        return ipliststring



def getvars(ydomain):
        DOC = xmlapi.api("domainuserdata?domain=" + ydomain)
        parsedDOC = minidom.parseString(DOC)
        docroottaglist = parsedDOC.getElementsByTagName('documentroot')
        yiptaglist = parsedDOC.getElementsByTagName('ip')
        aliastaglist=[]
        aliastaglist = parsedDOC.getElementsByTagName('serveralias')
        aliaslist =[]
        a = 0
        while a < len(aliastaglist):
                newalias = str(aliastaglist[a].childNodes[0].toxml())
                if not newalias.startswith("www.*."):
                        aliaslist.append(newalias)
                a = a + 1
        alias = ''.join(aliaslist)
        docroot=""
        yip=""
        try:
                docroot = docroottaglist[0].childNodes[0].toxml()
                yip = yiptaglist[0].childNodes[0].toxml()

        except IndexError:
                errf=open('/root/failedcreation.txt', 'a')
                import time
                from time import strftime
                t=strftime("%Y-%m-%d %H:%M:%S")
                errortxt="%s Failed to create vhost for %s\n" % (t, ydomain)
                errf.write(errortxt)
                errf.close()

        return docroot, yip, alias

if __name__ == '__main__':
        DOC = xmlapi.api("listaccts")
        parsedDOC = minidom.parseString(DOC)
        usertaglist = parsedDOC.getElementsByTagName('user')
        userlist = []
        numusers = 0
        while numusers < len(usertaglist):
                userlist.append(str(usertaglist[numusers].childNodes[0].toxml()))
                numusers = numusers + 1
        for i in userlist:
                f = open('/var/cpanel/userdata/' + i + '/main')
                ydata = yaml.load(f)
                f.close()
                sublist = ydata['sub_domains']
                addondict = ydata['addon_domains']
                parkedlist = ydata['parked_domains']
                mainlist = ydata['main_domain']
                serverip = getmainip()
                if len(sublist) != 0:
                        slcont = 0
                        while slcont < len(sublist):
                                domain = sublist[slcont]
                                docroot, yip, alias = getvars(sublist[slcont])
                                if docroot == "":
                                        slcont = slcont + 1
                                else:
                                        if yip == serverip:
                                                writeconfshared(i, domain, docroot, yip, alias)
                                        else:
                                                writeconfded(i, domain, docroot, yip, alias)
                                        slcont = slcont + 1


                DOC = xmlapi.api("accountsummary?user=" + i)
                parsedDOC = minidom.parseString(DOC)
                domaintaglist = parsedDOC.getElementsByTagName('domain')
                domain = domaintaglist[0].childNodes[0].toxml()
                docroot, yip, alias = getvars(domain)
                if yip == serverip:
                       writeconfshared(i, domain, docroot, yip, alias)
                else:
                       writeconfded(i, domain, docroot, yip, alias)
