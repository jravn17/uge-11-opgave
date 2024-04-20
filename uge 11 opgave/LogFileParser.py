class LogFileParser:
    @staticmethod
    def parse(log_file):
        try:
            with open(log_file, 'r') as file:
                log_content = file.readlines()

            download_status = {"Downloadet": [], "Ikke Downloadet": [], "Ugyldig URL": []}
            for line in log_content:
                parts = line.strip().split(' - ')
                if len(parts) == 2:  # Vi forventer nu to dele: URL og status
                    url, status = parts
                    if status in download_status:
                        download_status[status].append(url)
                    else:
                        download_status["Ugyldig URL"].append(url)

            # Sorter hver gruppe af URL'er
            for status, urls in download_status.items():
                download_status[status] = sorted(urls)

            return download_status
        except Exception as e:
            print(f'Fejl under parsing af logfilen: {str(e)}')
            return {}
