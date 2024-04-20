import pandas as pd
import requests
import logging
import os
from concurrent.futures import ThreadPoolExecutor

class FileReader:
    def __init__(self, file_path, batch_size = 100):
        self.file_path = file_path
        self.batch_size = batch_size
        self.pdf_download_folder = 'pdf_downloads'
        self.html_download_folder = 'html_downloads'
        self.max_delay = 1
        self.setup_logging()
        self.downloaded_count = 0
        self.not_downloaded_count = 0

    def setup_logging(self):
        logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
    
    def log_status(self, br_num, status):
        logging.info(f'BRnummer:{br_num} - Status: {status}')
        if status == 'Downloadet':
            self.downloaded_count += 1
        elif status == 'Ikke Downloadet':
            self.not_downloaded_count += 1

    # Getter og setter for file_path
    def get_file_path(self):
        return self.file_path

    def set_file_path(self, file_path):
        self.file_path = file_path

    # Getter og setter for batch_size
    def get_batch_size(self):
        return self.batch_size

    def set_batch_size(self, batch_size):
        self.batch_size = batch_size

    # Getter og setter for pdf_download_folder
    def get_pdf_download_folder(self):
        return self.pdf_download_folder

    def set_pdf_download_folder(self, pdf_download_folder):
        self.pdf_download_folder = pdf_download_folder

    # Getter og setter for html_download_folder
    def get_html_download_folder(self):
        return self.html_download_folder

    def set_html_download_folder(self, html_download_folder):
        self.html_download_folder = html_download_folder

    # Getter og setter for max_delay
    def get_max_delay(self):
        return self.max_delay

    def set_max_delay(self, max_delay):
        self.max_delay = max_delay
        
    def check_and_download_urls(self, urls, folder, prefix='', name_changed=False):
        with ThreadPoolExecutor(max_workers=5) as executor:
            for br_num, url in urls.items():
                try:
                    if isinstance(url, str) and url.endswith(('.pdf', '.PDF')):  
                        response = requests.head(url, timeout=self.max_delay)
                        if name_changed:
                            file_name = f'{br_num}.html' if prefix == 'html_' else f'{br_num}.pdf'
                        else:
                            file_name = os.path.basename(url)
                    elif isinstance(url, str):
                        file_name = os.path.basename(url)
                    else:
                        print(f"Ignorerer url {url}, da den ikke er en streng.")
                        continue

                    file_path = os.path.join(folder, f'{prefix}{file_name}')
                    print(f'Prøver at downloade fra {url} for BRNum {br_num}')
                    if self.download_file(url, file_path):
                        print(f'Filen downloadet for BRNum {br_num}')
                        self.log_status(br_num, 'Downloadet')
                    else:
                        print(f'Kunne ikke downloade fra {url} for BRNum {br_num}')
                        self.log_status(br_num, 'Ikke Downloadet')
                except requests.exceptions.RequestException as e:
                    print(f'Fejl under behandling af URL {url}: {str(e)}')
                    self.not_downloaded_count += 1
                except OSError as e:
                    print(f'Fejl under håndtering af filstien for URL {url}: {str(e)}')
                    self.not_downloaded_count += 1

    def print_download_counts(self):
        print(f"Antal downloadede URL'er: {self.downloaded_count}")
        print(f"Antal ikke-downloadede URL'er: {self.not_downloaded_count}")                    

    def extract_and_download_urls(self):
        if not os.path.exists(self.pdf_download_folder):
            os.makedirs(self.pdf_download_folder)

        if not os.path.exists(self.html_download_folder):
            os.makedirs(self.html_download_folder)

        data_df = pd.read_excel(self.file_path, usecols=["BRnum", "Pdf_URL", "Report Html Address"])
        pdf_urls = data_df.set_index('BRnum')['Pdf_URL'].to_dict()
        html_urls = data_df.set_index('BRnum')['Report Html Address'].to_dict()
        
        # Download PDF URL'er i batcher
        for i in range(0, len(pdf_urls), self.batch_size):
            batch = dict(list(pdf_urls.items())[i:i+self.batch_size])
            self.check_and_download_urls(batch, self.pdf_download_folder, name_changed=True)

        # Download HTML URL'er i batcher
        for i in range(0, len(html_urls), self.batch_size):
            batch = dict(list(html_urls.items())[i:i+self.batch_size])
            self.check_and_download_urls(batch, self.html_download_folder, name_changed=True)
            
        # Udskriv antallet af downloadede og ikke-downloadede URL'er
        self.print_download_counts()

    def download_file(self, url, file_path):
        try:
            response = requests.get(url, timeout=self.max_delay)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f'Fejl under download af fil fra {url}: {str(e)}')
            return False
        except OSError as e:
            print(f'Fejl under håndtering af filstien for URL {url}: {str(e)}')
            return False
