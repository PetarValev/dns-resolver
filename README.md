#DNS Resolver Tool 🧩

#Overview
The DNS Resolver Tool is your go-to command-line application for quick and easy DNS queries. Perfect for network admins, developers, or anyone keen on understanding domain details, this tool lets you fetch and analyze DNS records with ease. 🌐✨

--- 

#Features 🚀
Comprehensive DNS Queries: Retrieve various DNS records including A, AAAA, CNAME, MX, NS, SOA, and TXT. 📜
User-Friendly Interface: Enjoy a clean command-line interface that presents results in an organized and readable format. 🖥️
Effortless Setup: Get up and running with a few simple commands. 🎯

---

#Installation 🛠️
Follow these steps to set up the DNS Resolver Tool:

Clone the Repository

```
git clone https://github.com/your-username/dns-resolver.git
cd dns-resolver
```
Create and Activate a Virtual Environment

On Windows:

```
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```
Install Dependencies

```
pip install -r requirements.txt
```
---

#Usage 🎉
Launch the tool and start querying DNS records:

```
python app.py
```
Enter the domain name you wish to query when prompted. The tool will display the DNS records in a clear, organized manner.

#Example 📊
```
python app.py
```
Enter the domain: example.com

Output:

A records for example.com:
  93.184.216.34

AAAA records for example.com:
  2606:5000:60::1

CNAME records for example.com:
  www.example.com
