# test-online-book-store-project

link: http://selenium1py.pythonanywhere.com/

Final project of https://stepik.org/course/575


## Instructions to run the tests locally

Install Selenium:
```
pip install selenium
pip list 
```
ChromeDriver:

1. Go to page to know version ChromeDriver: https://sites.google.com/chromium.org/driver/

2. Download ChromeDriver and unzip file:
```
wget https://chromedriver.storage.googleapis.com/version-of-ChromeDriver/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```
3. Locate unzipped file:
```
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```

Run tests:

1. Create and activate env:
```
$ cd environments
$ python3 -m venv name_env
$ source name_env/bin/activate
```
2.  Install packages:
```
$ pip install -r requirements.txt
```
3. Run tests:

(name_env)name@user: ~/test-online-book-store-project$ pytest -v -s test_main_page.py

(name_env)name@user: ~/test-online-book-store-project$ pytest -v -s test_product_page.py

4. Run marked @pytest.mark.need_review tests:

(name_env)name@user: ~/test-online-book-store-project$ pytest -v --tb=line --language=en -m need_review test_product_page.py


