def save_to_file(file_name, jobs):

  file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
  file.write("position,company,location, URL\n")

  for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']}\n")

  file.close()  #닫아야 정상 실행된다..
