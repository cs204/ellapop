extensions = {
  ".gif": "image/gif",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".pdf": "application/pdf",
  ".txt": "text/plain",
  ".zip": "application/zip"
}

extension_found = False

file_name = input("File name: ")

for extension, type_ in extensions.items():
  if file_name.endswith(extension):
    extension_found = True
    print(type_)

    break

if not extension_found:
  print("application/octet-stream")