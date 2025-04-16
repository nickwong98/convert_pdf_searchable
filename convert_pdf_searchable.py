import os
import fitz  # PyMuPDF
from pathlib import Path

def get_text_percentage(file_name: str) -> float:
    """
    Calculate the percentage of document that is covered by (searchable) text.

    If the returned percentage of text is very low, the document is
    most likely a scanned PDF
    """
    total_page_area = 0.0
    total_text_area = 0.0

    doc = fitz.open(file_name)

    for page_num, page in enumerate(doc):
        total_page_area = total_page_area + abs(page.rect)
        text_area = 0.0
        for b in page.get_text_blocks():
            r = fitz.Rect(b[:4])  # rectangle where block text appears
            text_area = text_area + abs(r)
        total_text_area = total_text_area + text_area
    doc.close()
    return total_text_area / total_page_area

if __name__ == "__main__":
    input_directory = ".\\input"
    output_directory = ".\\output"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for file in os.listdir(input_directory):
        if file.endswith(".pdf"):
            filepath = os.path.join(input_directory, file)
            filenamenoext = Path(filepath).stem
            print("\nFile: " + filepath)
            text_perc = get_text_percentage(filepath)
            print("Text Percentage: " + str(text_perc))
            if text_perc < 0.1:
                print("fully scanned PDF - no relevant text")
                # docker image jbarlow83/ocrmypdf:latest is needed
                # add languages to the OCR command as needed
                os.system(f"docker run -i --rm jbarlow83/ocrmypdf --force-ocr -l eng+deu - - <\"{filepath}\" >\"{output_directory}\\{filenamenoext}_ocr.pdf\"")
            else:
                print("not fully scanned PDF - text is present")