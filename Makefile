run:
	uv run main.py

update:
	ssh noc@192.168.2.112 'cd ~/smartlinkapi/ && git pull origin main && sudo systemctl restart smartlink'

restart:
	ssh noc@192.168.2.112 'sudo systemctl restart smartlink'

.PHONY: run update restart
