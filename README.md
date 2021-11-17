# ScrapingAnything
Scrape any website


## Table of Contents


- [Export Data Module](#export-data-module)
- [Steam Spider](#steam-spider)
- [Support Command-line](#support-command-line)


## Export Data Module

**Usage**:


```console
$ export_data.py [-h] [-s {csv,excel,all}]
```


**Options**:

- `-h` `--help`: Show this message and exit.
- `-s` `--save_type`: Save as ``csv`` or ``excel`` or ``all`` file (default: None, file name = **export_data**).

### The process

**Functions**:
- **clean_text(string)** : clear `\n ` and`multi whitespaces`
- **real_time(elapsed)** : show elapsed time with digital clock format. 
- **csv2excel(csv_filename, excel_filename)**: convert from `csv_filename` to `excel_filename`
- **save_data(list_data, save_type, header, file_name)**: save `list data` as `save type` file with `header` and `file name`


**Example**: 

* Run the process and save as csv file.
```console
$ py .\scraping_local_titles.py -s csv
```


**Output**:
```
No such file or directory: 'sample_output.csv'
Elapsed: 00:00:00.04
```

## Steam Spider
Get all games in Steam store.

Show sale-free games.

**Usage**:


```console
$ steam_game_spider.py [-h] [-s {csv,excel,all}]
```


**Options**:

- `-h` `--help`: Show this message and exit.
- `-s` `--save_type`: Save as ``csv`` or ``excel`` or ``all`` file (default: None, file name = **export_data**).

### The process

**Show**:


- A number of games. 
- How long the process run.
- List sale free games.



**Example**: 

* Run the process and save as csv file.
```console
$ py .\scraping_local_titles.py -s csv
```


**Output**:
```
2021-11-11 22:46:21 [scrapy.utils.log] INFO: Scrapy 2.5.0 started (bot: scrapybot)
2021-11-11 22:46:21 [scrapy.utils.log] INFO: Versions: lxml 4.6.3.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 21.2.0, Python 3.9.3 (tags/v3.9.3:e723086, Apr  2 2021, 11:35:20) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 20.0.1 (OpenSSL 1.1.1k  25 Mar 2021), cryptography 3.4.7, Platform Windows-10-10.0.19041-SP0     
2021-11-11 22:46:21 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor        
2021-11-11 22:46:21 [scrapy.crawler] INFO: Overridden settings:
{}
...............
2021-11-11 22:46:23 [scrapy.core.engine] INFO: Spider closed (finished)
Total: 25 games
Elapsed: 00:00:02.14
Sale free game:  [('Beholder', '9 Nov, 2016', 'Free', -100.0, 'https://store.steampowered.com/app/475550/Beholder/?snr=1_7_7_230_150_3')]
```
If you want to have a good list, you can go to [SteamDB](https://steamdb.info/sales/)


## Support Command-line

- Create requirements.txt :

```console
$ py -m pipreqs.pipreqs . --encoding=utf8
``` 
- Install requirements:
```console
$ pip install -r requirements.txt
```
- Use pytest:
```console
$ pytest tests
$ pytest tests/test_export_data.py::TestRealTime
$ pytest tests/test_export_data.py::TestRealTime::test_real_time_negative
```
- Upgrade library:

```console
$ pip install -U <library>
```
- Upgrade pip:

```console
$ py -m pip install --upgrade pip
```

###### [on top](#table-of-contents)