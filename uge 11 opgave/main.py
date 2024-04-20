from FileReader import FileReader
from LogFileParser import LogFileParser

import  tkinter as tk
from tkinter import filedialog

def main():
    #Brugeren kan selv angive filsti til excel-filen når programmet
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    
    # Opret en FileReader-instans og download data
    file_reader = FileReader(file_path)
    file_reader.extract_and_download_urls()

    # Parse logfilen og få downloadstatussen
    download_status = LogFileParser.parse("log.txt")
    
    #Tæller antallet af URL'er i logfilen udfra deres status
    download_count = len(download_status.get("Downloadet", []))
    not_downloaded_count = len(download_status.get("Ikke Downloadet", []))
    
    # Udskriv antallet af URL'er i hver kategori
    print(f"Antal URL'er downloadet: {download_count}")
    print(f"Antal URL'er Ikke downloadet: {not_downloaded_count}")


if __name__ == "__main__":
    
    main()
