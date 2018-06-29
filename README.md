#How to install NGINXCP + Pagespeed on cPanel 

Clone Repository
   ```git clone https://github.com/geek-id/nginxcp_pagespeed.git``` 

Open folder nginxcp_pagespeed
   ```cd nginxcp_pagespeed```

Generate Remote Access Key
   ```/script/convert_acceshash_to_token```
 
Running installer nginxcp
   ```./nginxinstaller install```

Restart web server
   ```systemctl restart httpd```

Register the plugin with cPanel
   ```/usr/local/cpanel/bin/register_appconfig /var/cpanel/apps/nginxcp.conf```

Setting up cron job to clean up temporary files
   ```crontab -e -u root```

Add the following cron job to the end of line list
   ```0 */1 * * * /usr/sbin/tmpwatch -am 1 /tmp/nginx_client```
