import sqlite3
conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()

cursor.execute(""" 
  CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
  )
""")

def list_all_videos():
  cursor.execute("SELECT * FROM  videos")
  for row in cursor.fetchall():
    print(row)

def add_videos(name, time):
  cursor.execute(" INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
  conn.commit()

def update_videos(video_id, name, time):
  cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id,))
  conn.commit()

def delete_videos(video_id):
  cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  conn.commit()


def main():
  while True:
    print("\n Youtube Manager app with DB | Choose Your Option")
    print("1. List all youtube viseos")
    print("2. Add a youtube video")
    print("3. Update a youtube video")
    print("4. Delete a youtube video")
    print("5. Exit app")
    choice = input("Enter your choice: ")
    
    if choice == '1':
      list_all_videos()
    elif choice == '2':
      name = input("Enter video name: ")
      time = input("Enter video time: ")
      add_videos(name, time)
    elif choice == '3':
      video_id = input("Enter video id: ")
      name = input("Enter video name: ")
      time = input("Enter video time: ")
      update_videos(video_id, name, time)
    elif choice == '4':
      video_id = input("Enter the video number to de deleted: ")
      delete_videos(video_id)
    elif choice == '5':
      break
    else:
      print("\n Invalid choice")
  conn.close()




if __name__ == '__main__':
  main()


