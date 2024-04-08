# Python Crawling

Python+Selenium library for crawling

## Any issues?

After the Selenium Update 4.6, there were some changes that I had issues with, particularly when closing in few second the Chrome browser while crawling


Please click the GIF file for more detail 

![PythonCrawling](https://github.com/NAry-Byun/PythonCrawling/assets/153330377/1a3032e5-7493-4633-8135-41fca02ca43c)

## How to solved the problems
Line 30. except code
Behind each Driver change to find_element. 
It is working without closing. However need to impliment the save file fuction.

