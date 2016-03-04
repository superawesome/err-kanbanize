# err-kanbanize
Configuration is done via the standard 'errobot' plugin config command:

!plugin config Kanbanize

This will show the default and current-running config. To set a new one, it'll be something like this:

!plugin config Kanbanize {'APIKEY': 'xxx', 'BOARDID': x, 'SUBDOMAIN': 'x', 'CHANNEL': 'x'}

Fill in the details in the last bit- make sure to provide values for every setting listed in the default config (in case things are changed since this README was updated).
