
# Withings dumper

[![CircleCI](https://circleci.com/gh/shirayu/withings-dumper.svg?style=svg)](https://circleci.com/gh/shirayu/withings-dumper)
[![Apache License](http://img.shields.io/badge/license-APACHE2-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## Install

```sh
sudo pip3 install requests_oauthlib
sudo pip3 install https://github.com/WarmongeR1/python-withings/archive/master.zip#egg=withings-0.4.0
```

## Initialization

```sh
cp config.template.json config.json
chmod 600 config.json

# Set your CONSUMER_KEY and CONSUMER_SECRET
vi config.json

# Get values
python3 dump.py --init -c config.json

# Set all values
vi config.json
```

## Sample

```sh
# Get yesterday data
python3 ./dump.py -c ./config.json --startdate=`date +s -d yesterday` --enddate=`date +s -d now`
```

## License
- [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
