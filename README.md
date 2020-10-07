# keyakiblog
keyakiblog is a Keyakizaka blog archive and statistic website

## Usage
### name.py
return member list and statistic of blog data
### soup.py
Using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape image link and other data
```python
createMemberJSON()       #create empty JSON file, run only once
writeMemberJSON(member)  #initially scraping a member's blog and save to JSON
writeAllMemberJSON()     #initially scraping all member's blog 
updateMemberJSON(member) #update a member's JSON file
updateAllMemberJSON()    #update all member's JSON file
```

## Link
https://keyakiblog.herokuapp.com

## License
[MIT](https://choosealicense.com/licenses/mit/)