
# Withings dumper

## Install

```sh
sudo pip3 install requests_oauthlib
sudo pip3 install https://github.com/WarmongeR1/python-withings/archive/master.zip#egg=withings-0.4.0
```

## Initialization

```sh
cp config.template.json config.json

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
