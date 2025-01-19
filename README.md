[![codecov](https://codecov.io/github/amirhossein226/simple-url-shortener/graph/badge.svg?token=HX5UPD14Y2)](https://codecov.io/github/amirhossein226/simple-url-shortener)
# Simple Url Shortener Using [Yhttp](https://github.com/yhttp/yhttp.git) Framework
Follow below steps to run this program on your machine:
### Get Project:
Get the project using `clone` command:
```
git clone https://github.com/amirhossein226/simple-url-shortener.git
```
and:
```
cd simple-url-shortener
```
### Prepare Environment :
Create the virtual environment using `make` command:
```
make <your_venv_name>
```
And activate your venv:
```
source <your_venv_name>/bin/activate
```
> Reaplce `<your_venv_name>` with your intended virtual environment name.

### Dependencies:
Install required packages using below command:
```
make shortener
```
Above command will install the package and its dependencies.
### Test:
You could test the Api either by using `make` command or directly using `curl` command:
```
make test
```
Using `curl`:
First of all ensure that `curl` is installed.
```
which curl
```
If it was not installed, then install it:
```
sudo apt-get install curl
```
Before using `curl`, you must open a new terminal(use `tmux`) and runn below command:
```
shortener serve
```
After running above command the api will start on *localhost:8080*.There will be two endpoint for this api, */url_shortener* is the first one.The request sending to this endpoint must be a **POST** request with a body containing **url** parameter. And second endpoint is a **GET** request like *http://localhost:8080/ABC123* in which the */ABC123* is the key generated using first endpoint, lets see an example for better illustration. 
Push below line into your terminal(I assume you did previous steps, so far): 
```
curl -X 'POST' -F "url=https://asre-amn.com/ct/%d8%aa%d9%84%d8%aa%d9%88%d9%86%db%8c%da%a9%d8%a7/" http://localhost:8080/url_shortener
```
After above command you'll get a shorter url, copy it because we'll use it on below command:
```
curl <your_copied_url>
```
You will now see anything as result.But if you check the terminal in which you used `shortener serve` command, you can see the *301* status code that indicate you redirected to the original url(https://asre-amn.com/ct/%d8%aa%d9%84%d8%aa%d9%88%d9%86%db%8c%da%a9%d8%a7/).

