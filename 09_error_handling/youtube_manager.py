import json

def load_date():
  try:
    with open('youtube.txt', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_data_helper(videos):
  with open('youtube.txt', 'w') as file:
    json.dump(videos, file)

def list_all_videos(videos):
  print("\n")
  print("*" * 65)
  print("\n")
  for index, video in enumerate(videos, start= 1):
    print(f"{index}. {video['name']}, Duration {video['time']}")
  print("\n")
  print("*" * 65)
  print("\n")

def add_videos(videos):
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  videos.append({'name': name, 'time': time})
  save_data_helper(videos)

def update_videos(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to update: "))
  
  if 1 <= index <= len(videos):
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[index - 1] = {'name': name, 'time': time}
    save_data_helper(videos)
  else:
    print("Invalid index selected")

def delete_videos(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to be deleted: "))
  
  if 1 <= index <= len(videos):
    del videos[index - 1]
  else:
    print("Invalid video index selected")
  

def main():
  videos = load_date()
  while True:
    print("\n YouTube  manager | choose an options ")
    print("1. List all youtube videos ")
    print("2. Add a youtube videos ")
    print("3. Update a youtube videos details ")
    print("4. Delete a youtube video ")
    print("5. Exit a app ")
    choice = input("Enter your choice: ")
    #print(videos)
    
    match choice:
      case '1':
        list_all_videos(videos)
      case '2':
        add_videos(videos)
      case '3':
        update_videos(videos)
      case '4':
        delete_videos(videos)
      case '5':
        break
      case _:
        print("\n Invalide Choice")

if __name__ == "__main__":
  main()