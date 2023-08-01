

# import module
from pdf2image import convert_from_path
import glob, os
# from ironpdf import *
 
 
def convert_file(file_path):   
    
    images = convert_from_path(file_path, poppler_path = "poppler-23.07.0/Library/bin")
    
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save(f"{file_path}_page{i:0>3}.jpg", 'JPEG')
        
    # pdf = PdfDocument.FromFile(file_path)
    # pdf.RasterizeToImageFiles(f"{file_path}*.jpg",DPI=96)
    

def get_pdf_files(source_dir):
    
    return glob.glob(source_dir + '/*.pdf')


def main():
    
    pdf_files = get_pdf_files("convert_pdf_to_jpg")
    
    for pdf_file in pdf_files:
        convert_file(pdf_file)
        # print(os.path.basename(pdf_file))


if __name__ == "__main__":
    main()