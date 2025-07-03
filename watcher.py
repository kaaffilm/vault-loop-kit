import os, re, requests
from github import Github

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
g = Github(GITHUB_TOKEN)
REGEX = re.compile(r'(https?://[^\s"\')]+)')
QUERY = 'language:JavaScript pushed:>2025-01-01 stars:<10'

def search_repos():
    return g.search_repositories(query=QUERY, sort='updated', order='desc')[:50]

def extract_endpoints(repo):
    endpoints = set()
    contents = repo.get_contents("")
    for file in contents:
        if file.path.endswith(('.js','.py')):
            txt = requests.get(file.download_url).text
            endpoints |= set(REGEX.findall(txt))
    return endpoints

def main():
    for repo in search_repos():
        for url in extract_endpoints(repo):
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    print(f"OK {url}")
            except:
                pass

if __name__ == "__main__":
    main()
