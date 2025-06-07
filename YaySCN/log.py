import os

def html_format(log_list, log_name):
    with open(f"Log/TempLog/{log_name}.txt", "a", encoding='utf-8') as file:
        for data in log_list:
            file.write(data)

    with open(f"Log/TempLog/{log_name}.txt", "r", encoding='utf-8') as file:
        data = file.read()
    
    return data

def html_format_2(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        return [line.strip() + "<br>" for line in file.readlines()]

discovery_log_temp = html_format_2("Log/discovery_log.txt")
nmap_log_temp = html_format_2("Log/nmap_log.txt")
sql_log_temp = html_format_2("Log/sql_log.txt")
vuln_log_temp = html_format_2("Log/vuln_log.txt")
xss_log_temp = html_format_2("Log/xss_log.txt")
url_log_temp = html_format_2("Log/url_log.txt")
ftp_log_temp = html_format_2("Log/ftp_log.txt")
ssh_log_temp = html_format_2("Log/ssh_log.txt")

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YaySCN Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center; /* Sayfa genelinde ortalama */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
        }}
        h1, h2 {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin-bottom: 10px;
            color: #333;
        }}
        h1 {{
            font-size: 2.5em;
            margin-bottom: 20px;
        }}
        h2 {{
            font-size: 1.5em;
        }}
        .log-section {{
            border: 1px solid #ccc;
            padding: 20px;
            margin: 20px auto;
            width: 60%;
            text-align: left;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            background-color: #ffffff;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .log-section:hover {{
            transform: scale(1.02);
            box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);
        }}
        p {{
            font-size: 1.1em;
            line-height: 1.6;
            color: #555;
            margin: 0;
        }}
    </style>
</head>
<body>
    <h1>Log Report</h1>
    <h2>By Yay - https://github.com/ByYay</h2>

    <div class="log-section">
        <h2>Discovery Log</h2>
        <p>{html_format(discovery_log_temp, 'discovery_log')}</p>
    </div>

    <div class="log-section">
        <h2>Hydra URL Log</h2>
        <p>{html_format(url_log_temp, 'url_log')}</p>
    </div>

    <div class="log-section">
        <h2>Hydra FTP Log</h2>
        <p>{html_format(ftp_log_temp, 'ftp_log')}</p>
    </div>

    <div class="log-section">
        <h2>Hydra SSH Log</h2>
        <p>{html_format(ssh_log_temp, 'ssh_log')}</p>
    </div>

    <div class="log-section">
        <h2>Nmap Log</h2>
        <p>{html_format(nmap_log_temp, 'nmap_log')}</p>
    </div>

    <div class="log-section">
        <h2>SQL Log</h2>
        <p>{html_format(sql_log_temp, 'sql_log')}</p>
    </div>

    <div class="log-section">
        <h2>Vulnerability Log</h2>
        <p>{html_format(vuln_log_temp, 'vuln_log')}</p>
    </div>

    <div class="log-section">
        <h2>XSS Log</h2>
        <p>{html_format(xss_log_temp, 'xss_log')}</p>
    </div>
</body>
</html>
"""

if not os.path.exists("Reports"):
    os.system("mkdir Reports")

path = 'Reports/'
file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

report_path = f"Reports/report-{file_count + 1}.html"
with open(report_path, "w", encoding="utf-8") as file:
    file.write(html)

yellow = "\033[33m"
reset = "\033[0m"
green = "\033[32m"
print(f"{green}[+] Created report. ({report_path}){reset}")
