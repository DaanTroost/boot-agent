from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content


# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "pkg"))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))

print(get_files_content("calculator", "lorem.txt"))
