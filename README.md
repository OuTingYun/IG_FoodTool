## IG Foody Scraper Website base on Django
This project includes 2 page. One for searching food sorting by region/ig_accounts, the other is for sraping more data from IG account. 
### Environment

```python
python    = 3.7.10
django    = 3.2.9
```

### How to use
1. In `./IG_FoodTool` you can find `manage.py` then open cmd under this folder and input instruction
```cmd 
> python3 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 14, 2022 - 16:50:07
Django version 3.2.9, using settings 'IG_FoodTool.settings'
Starting development server at http://127.0.0.1:8000/ 
Quit the server with CTRL-BREAK.
Not Found: /

``` 
2. Open `http://127.0.0.1:8000/regionsearch/` and `http://127.0.0.1:8000/scrap/` I write two pages here.

### Searching Page
1. Chooing what you want to show on left side and submit. Then you will see the result on right side.

2. The small blue button on left-down of the page, is used to go `scrape page`.

3. you can click the picture and find what origin conetent is.

![gifs](https://github.com/OuTingYun/Images/blob/master/IG_FoodTool/ig1.gif)

### Scrape Page
1. Input the IG Account name int the textarea.
2. Choose how many scroll's number you want to get. The larger the scroll's number is. the more data you will get, also you  need ti wait more time to get.
3. The small blue button on left-down of the page, is used to go `scrape page`.

![gif](https://github.com/OuTingYun/Images/blob/master/IG_FoodTool/ig2.gif)
