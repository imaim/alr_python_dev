
curl "http://{{ansible_host}}/master/check_mk/webapi.py?_secret={{vault_ansible_automation}}&_username={{auto_user}}&action=activate_changes" -d 'request={"sites":["{{omd_site}}"],"allow_foreign_changes":"1"}'
print("teste")
print("233")
