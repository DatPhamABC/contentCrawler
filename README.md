# contentCrawler
Hướng dẫn cài đặt:

## 1. Yêu cầu:
 - Python 3.0 hoặc hơn [python](https://www.python.org/downloads/)
 - Miniconda (không bắt buộc) [miniconda](https://docs.conda.io/en/latest/miniconda.html)
 - [MongoDB](https://docs.mongodb.com/manual/installation/)

## 2. Tạo môi trường (virtual environment - venv):
###  2.1. Không cài đặt Miniconda:
  - Sau khi đã cài đặt python, mở command prompt tại folder muốn chứa môi trường và tạo môi trường (tên môi trường: scrapy):
  	```bash
	python -m venv scrapy
	```
  - Kích hoạt môi trường:
  	```bash
	scrapy\Scripts\activate.bat
	```
  - Cài đặt môi trường theo file requirements.txt: dẫn đến folder có chứa file requirements.txt và chạy:
  	```bash
	pip install -r requirement.txt
	```

###  2.2. Có cài đặt Miniconda:
  - Mở anaconda prompt và chạy:
  	```bash
	conda create --name scrapy
	```
  - Kích hoạt môi trường:
  	```bash
	conda activate scrapy
	```
  - Cài đặt môi trường theo file requirements.txt:
  	```bash
	pip install -r requirement.txt
	```

## 3. Cài đặt và chạy source code:
 - Pull từ github và đặt source code trong folder song song với folder của venv (nếu không có anaconda) hoặc đặt source code trong folder tùy ý (nếu có anaconda)
 - Mở command prompt hoặc anaconda prompt, dẫn đến folder chứa file crawlerRun.py và chạy:
 	```bash
	python crawlerRun.py
	```
	
## 4. Source code:
### 4.1. crawlerRun.py:
 - Chạy spider từ script
 
### 4.2. contentCrawler.py:
 - class của một spider
 - input: begin_date và end_date: giới hạn thời gian để chọn bài báo được đăng
          link: được lấy trực tiếp từ mongoDB database scrapedLink, collection link
 - output: nội dung các bài báo được lọc theo thời gian đăng
 - Các tham số:
    name = 'dtSpider': tên spider
    
    start_urls = [] : list các trang cần lọc
    
    date: thời gian đăng bài (đã format theo định dạng %Y/%m/%d từ date_extract)
    
    content: lưu các nội dung của bài đăng (bao gồm tiêu đề (title), tóm tắt (summary), hình ảnh minh họa (image), nội dung bài đăng (article) đối với báo chữ)
                                           (bao gồm tiêu đề (title), tóm tắt (summary), nội dung bài đăng (article - gồm hình (image) và mô tả hình ảnh (image description) được lưu trong list items) đối với báo hình)

### 4.3. Ghi chú:
 - Dữ liệu được lưu trong MongoDB với hostname localhost và port 27017 với database: scrapedContent,  collection: content
 - Cần chạy linkCrawler trước để lấy link cho contentCrawler
