import os

def create_project_dir(directory):
  if not os.path.exists(directory):
    print('Creating project ' + directory)
    os.makedirs(directory)

def create_data_files(project_name, base_url):
  queue_path = project_name + '/queue.txt'
  crawled_path = project_name + '/crawled.txt'
  if not os.path.isfile(queue_path):
    write_file(queue_path, base_url)
    write_file(crawled_path, '')

def write_file(path, data):
  with open(path, 'w') as file:
    file.write(data + '\n')

def append_file(path, data):
  with open(path, 'a') as file:
    file.write(data + '\n')

def delete_file_contents(path):
  with open(path, 'w'):
    pass

def file_to_set(file_path):
  results = set()
  with open(file_path, 'rt') as file:
    for line in file:
      results.add(line.replace('\n', ''))
  return results

def set_to_file(links, file_path):
  delete_file_contents(file_path)
  for link in sorted(links):
    append_file(file_path, link)
