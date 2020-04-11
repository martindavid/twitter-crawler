producer1:
		python producer.py -c data/config.json -tu 0 -t stream -v

producer2:
		python producer.py -c data/config.json -tu 1 -t stream -v

consumer:
		python consumer.py -c data/config.json
