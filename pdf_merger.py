from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    
    for pdf in pdf_list:
        if os.path.exists(pdf):
            print(f"Merging: {pdf}")
            merger.append(pdf)
        else:
            print(f"File not found: {pdf}")
    
    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved to {output_path}")

if __name__ == "__main__":
    # List of PDF file paths (update or take from user)
    pdf_files = [
        "file1.pdf",
        "file2.pdf",
        
    ]
    
    output_file = "merged_result.pdf"
    merge_pdfs(pdf_files, output_file)
