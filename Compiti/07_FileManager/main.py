import os


dir_path = "test"
dir_content = os.listdir(dir_path)
print("\n")
print("-"*80)
print(dir_content)
list_content = []
list_date = []
list_dimension = []

for content in dir_content :
    content_path = f"{dir_path}/{content}"
    if (os.path.exists(content_path)):
        if(os.path.isdir(content_path)):
            isDir = "Directory"
            extension = ""
        else: 
            if os.path.isfile(content_path):
                isDir = "File"
                extension = os.path.splitext(content_path)[1]
        
        creation_date = os.path.getctime(content_path)
        list_date.append(creation_date)
        dimension = os.path.getsize(content_path)
        list_dimension.append(dimension)

    content_info = (content , extension , isDir , dimension ,creation_date )
    list_content.append(content_info)

while True :
    print(f"\n{list_content} \n")
    sorting_method = int(input ("Sort By :\n0 -Extension\n1 -Dimension\n2 -Creation Date"))

    if sorting_method == 0:
        extension_desired = input("Digit witch file extension are you looking for")
        for content in list_content:
            if(content[1]==extension_desired):
                print(content)
        break
    

    if sorting_method == 1 :
        list_dimension.sort()
        while len(list_content)!=0:
            for dim in list_dimension :
                for content in list_content:
                    if content[3]==dim :
                        print(content)
                        list_content.remove(content)
        break

    if sorting_method == 2 :
        list_date.sort()
        while len(list_content)!=0:
            for date in list_date :
                for content in list_content:
                    if content[4]==date:
                        print(content)
                        list_content.remove(content)
        break


print("-"*40)

                


