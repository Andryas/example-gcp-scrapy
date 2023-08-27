
rsync -rv --exclude=.gitignore --exclude=.git --exclude=.vscode --exclude=venv/ . scraping/ 
gcloud compute scp --recurse scraping/ scraping:/home/wavrzenczak/scraping --zone us-central1-c
sudo rm -rf scraping/