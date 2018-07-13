# **NginCP + SSL + Pagespeed**

This repository modification of NginxCP.
What feature modification ?
- Enable SSL on NginxCP
- Add module Pagespeed on NginxCP

**How to install:**

1. Clone Repository<br/>
```git clone https://github.com/geek-id/nginxcp_pagespeed.git``` <br/>

2. Open folder nginxcp_pagespeed<br/>
```cd nginxcp_pagespeed```<br/>

3. Running installer nginxcp<br/>
```./nginx-installer.py```<br/>

4. Restart web server <br/>
```systemctl restart httpd```<br/>

5. Register the plugin nginxcp on cPanel <br/>
```/usr/local/cpanel/bin/register_appconfig /var/cpanel/apps/nginxcp.conf```<br/>

6. Setting up cron job to clean up temporary files <br/>
```crontab -e -u root```<br/>
Add the following cron job to the end of line list <br/>
```0 */1 * * * /usr/sbin/tmpwatch -am 1 /tmp/nginx_client```<br/>


Regards,
Geek-ID
