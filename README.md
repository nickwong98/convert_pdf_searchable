**Description**

PDF files may be non-searchable if the text content is embedded as an image, making it impossible to search, select, or copy the text.
This python code detects and converts non-searchable pdf files to searchable ones.


**Tested Environment**

Python 3.12

[Docker Image for OCR](https://hub.docker.com/r/jbarlow83/ocrmypdf)


**How to use**
1. Ready jbarlow83/ocrmypdf image in Docker Desktop, no need to create container
2. Create input folder "input"
3. Put original pdf files in input folder, they can be both searchable and non-searchable, the app will analyze and convert if needed
4. Install all requirements --> *pip install -r requirement.txt*
5. Run app locally --> *python convert_pdf_searchable.py*
6. Find converted searchable pdf files in output folder "output"