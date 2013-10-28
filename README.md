Project302
----------

This is a quick hack to setup HTTP based redirections without needing to
edit nginx/apache configuration files.

Install
-------
```sh
$ git clone git://github.com/daniellawrence/project302
$ cd project302
$ pip install -r requirements.txt
$ gunicorn project302.wsgi:application
````

Should I use this?
------------------

No.